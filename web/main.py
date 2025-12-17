from fastapi import FastAPI, Request, Form, HTTPException, BackgroundTasks
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
import sys
import re
import uuid
from typing import Dict

# Add the parent directory of TiktokCrawler to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from TiktokCrawler import downloader

app = FastAPI()

# In-memory "database" to store task status and results
tasks: Dict[str, Dict] = {}

# --- Background Task Functions ---
def cleanup_file(filepath: str):
    """
    Deletes a file from the filesystem.
    """
    try:
        os.remove(filepath)
        print(f"Successfully cleaned up temporary file: {filepath}")
    except OSError as e:
        print(f"Error cleaning up file {filepath}: {e}")

def process_video_request(task_id: str, url: str):
    """
    Runs in the background to download the video to a temp file.
    """
    try:
        success, result, video_title = downloader.download_video_to_temp(url, task_id)
        if success:
            tasks[task_id] = {
                "status": "complete",
                "filepath": result,
                "video_title": video_title
            }
        else:
            tasks[task_id] = {"status": "failed", "error": result}
    except Exception as e:
        tasks[task_id] = {"status": "failed", "error": f"An unexpected error occurred: {str(e)}"}


# --- API Endpoints ---
app.mount("/static", StaticFiles(directory="web/static"), name="static")
templates = Jinja2Templates(directory="web/templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/request-download")
async def request_download(background_tasks: BackgroundTasks, url: str = Form(...)):
    """
    Accepts a URL, creates a task, and starts the background download.
    """
    task_id = str(uuid.uuid4())
    tasks[task_id] = {"status": "processing"}
    background_tasks.add_task(process_video_request, task_id, url)
    return JSONResponse({"success": True, "task_id": task_id})

@app.get("/task-status/{task_id}")
async def get_task_status(task_id: str):
    """
    Allows the frontend to poll for the status of a task.
    """
    task = tasks.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return JSONResponse(task)

@app.get("/stream-video/{task_id}")
async def stream_video(task_id: str, background_tasks: BackgroundTasks):
    """
    Serves the downloaded video file from disk and schedules it for deletion.
    """
    task = tasks.get(task_id)
    if not task or task.get("status") != "complete":
        raise HTTPException(status_code=404, detail="Video not ready or task failed")

    filepath = task.get("filepath")
    video_title = task.get("video_title", "video")

    if not filepath or not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="Downloaded file not found on server.")
        
    # Sanitize the title for the filename
    clean_title = re.sub(r'[^a-zA-Z0-9_.-]', '_', video_title)
    filename = f"{clean_title}.mp4"

    # Schedule the file for deletion after the response is sent
    background_tasks.add_task(cleanup_file, filepath)

    return FileResponse(
        path=filepath,
        media_type='video/mp4',
        filename=filename
    )

