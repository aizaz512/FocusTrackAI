# 🎯 FocusTrack AI

> **Real-time computer-vision system for analyzing visual attention and turning behavioral signals into focus and productivity insights.**

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?logo=opencv&logoColor=white)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-0097A7?logo=google&logoColor=white)](https://ai.google.dev/edge/mediapipe/solutions/guide)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Computer%20Vision-111111)](https://docs.ultralytics.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![CI](https://img.shields.io/github/actions/workflow/status/aizaz512/FocusTrackAI/python.yml?label=CI)](https://github.com/aizaz512/FocusTrackAI/actions)

## Overview

FocusTrack AI uses a laptop camera and computer-vision components to estimate visual-attention signals in real time. Those signals are combined into a focus score and stored for analytics.

## Features

- Face detection and face mesh
- Eye tracking
- Blink detection
- Sleep/fatigue signal detection
- Head-pose estimation
- Mobile-phone detection with YOLOv8
- Focus score calculation
- SQLite analytics storage
- Interactive Streamlit dashboard

## Computer Vision Pipeline

```text
Laptop Camera
      ↓
Face / Eye / Head Detection
      ↓
Behavioral Signals
      ↓
Focus & Fatigue Analysis
      ↓
Focus Score
      ↓
SQLite Analytics
      ↓
Dashboard
```

## Repository Structure

```text
FocusTrackAI/
├── .github/workflows/     # CI automation
├── dashboard/             # Streamlit dashboard
├── database/              # SQLite persistence
├── src/                   # Computer-vision and analysis modules
│   ├── analytics.py
│   ├── camera.py
│   ├── eye_tracker.py
│   ├── face_detector.py
│   ├── face_mesh.py
│   ├── focus_analyzer.py
│   ├── head_pose.py
│   └── phone_detector.py
├── main.py                # Application entry point
├── requirements.txt
├── test_analytics.py
├── test_database.py
└── yolov8n.pt              # YOLO model weights
```

## Tech Stack

| Area | Technology |
|---|---|
| Language | Python |
| Computer vision | OpenCV |
| Face landmarks | MediaPipe |
| Object detection | YOLOv8 |
| Dashboard | Streamlit |
| Database | SQLite |
| Visualization | Plotly |
| CI | GitHub Actions |

## Quick Start

```bash
git clone https://github.com/aizaz512/FocusTrackAI.git
cd FocusTrackAI
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

Dashboard:

```powershell
streamlit run dashboard/dashboard.py
```

> Camera access is required for the real-time computer-vision workflow.

## Portfolio Value

This project demonstrates practical computer vision, real-time signal processing, multi-model integration, persistence, testing, CI, and user-facing analytics in one end-to-end application.

## Status

**Active portfolio project.** The core real-time pipeline and analytics workflow are implemented. Future work focuses on performance, calibration, stronger fatigue estimation, privacy controls, automated testing, and production deployment.

## Roadmap

- [x] Face/eye/head tracking
- [x] Blink and fatigue signals
- [x] Phone detection
- [x] Focus scoring
- [x] SQLite analytics
- [x] Dashboard
- [x] Basic tests
- [x] GitHub Actions CI
- [ ] Improved calibration
- [ ] Expanded automated tests
- [ ] Privacy controls and documentation
- [ ] Production deployment

## Author

**Sahibzada Aizaz Ur Rahman**  
Python Developer | AI/ML Engineer

- GitHub: https://github.com/aizaz512
- Portfolio: https://github.com/aizaz512/sahibzada-portfolio

## License

MIT
