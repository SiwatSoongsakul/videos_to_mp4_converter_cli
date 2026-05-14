# 🎬 Video to MP4 Parallel Converter: CLI Automation
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![FFmpeg](https://img.shields.io/badge/FFmpeg-%23007808.svg?style=for-the-badge&logo=ffmpeg&logoColor=white)
![CLI](https://img.shields.io/badge/CLI-black?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

> **Effortlessly convert batch videos with real-time progress monitoring.**

## 📄 Executive Summary

## 📊 Workflow Diagram

## 🧩 Problem & Context

In professional video production, inconsistent codecs are a major bottleneck. Software like Adobe Premiere Pro often suffers from performance lags or crashes when handling unsupported or non-standard video formats.

While working on my own online programming course, I encountered this exact issue. Initially, I relied on cloud-based converters, but I quickly hit daily usage limits, which severely throttled my workflow and delayed the project.

**Solution:** 
* **Engineered a Local CLI Automation Tool:** Developed a high-performance converter using `ffmpeg` and `Python's ThreadPoolExecutor`. This allows for concurrent batch processing to H.264 MP4 (Premiere-ready) format, significantly reducing transcoding time.
* **Containerized the Workflow:** Implemented `Docker` to ensure environment consistency across different machines, making the tool easily shareable and scalable within a team.

**Outcome:**
I can now convert entire batches of high-quality video locally—bypassing cloud limits, ensuring format consistency, and significantly speeding up my production pipeline.

## 🧰 Tech Stack
**Core Technologies**
* 🐍 **Language:** Python 3.11+
* 🎥 **Engine:** FFmpeg (The industry-standard multimedia framework for transcoding)
* 🐋 **Containerization:** Docker (for consistent environment and easy development)

**Python Libraries**
* **Typer/Rich:** For building beautiful and intuitive Command Line Interface (CLI) with progress bars.
* **Concurrent.futures:** To handle multi-threaded parallel processing.
* **Pathlib:** For modern and robust file system path manipulations.

**Development Tools**
* **Pyproject.toml:** For modern Python packaging and dependency management.
* **Git:** For version control and branching workflow.

## 📂 Project Structure

```
.
├── app/                # app folder
│   ├── __init__.py     # empty file marked 'app' as a Python package
│   └── converter.py    # main logic for conversion
├── .dockerignore       # optimize build context by excluding unnecessary files
├── .gitignore          # excludes unnecessary files from version control
├── Dockerfile          # blueprint for creating image
├── pyproject.toml      # cli entry-point configuration
└── README.md           # YOU ARE HERE!
```

## ✅ System Requirements

## 🖥️ User Guide

## 🔥 Skills Demonstrated

## 💡 What I've Learned

## 🚀 Future Improvements