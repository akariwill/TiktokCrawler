from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="TiktokCrawler",
    version="0.1.0",
    author="WildanJR",
    description="A simple TikTok video downloader.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WildanJR/TiktokCrawler",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "tiktok-crawler=app.cli:main",
        ],
    },
)
