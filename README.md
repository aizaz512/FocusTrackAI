# 🎯 FocusTrack AI

> **Real-time AI focus and productivity monitoring using computer vision and machine learning.**

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?logo=opencv&logoColor=white)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-0097A7?logo=google&logoColor=white)](https://ai.google.dev/edge/mediapipe/solutions/guide)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Computer%20Vision-111111)](https://docs.ultralytics.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)

## 🎯 Overview

FocusTrack AI is a computer-vision application that analyzes visual attention signals in real time and converts them into focus and productivity insights.

## ✨ Features

- 👤 Face detection and face mesh
- 👁️ Eye tracking
- 😉 Blink detection
- 😴 Sleep/fatigue detection
- 🧭 Head-pose estimation
- 📱 Phone detection
- 📊 Focus score
- 🗄️ SQLite analytics storage
- 📈 Interactive dashboard

## 🔄 Computer Vision Pipeline

```text
Camera
  ↓
Face / Eye / Head Detection
  ↓
Behavioral Signals
  ↓
Focus & Fatigue Analysis
  ↓
Focus Score
  ↓
Analytics Dashboard
```

## 🛠️ Technology Stack

| Area | Technology |
|---|---|
| Language | Python |
| Computer Vision | OpenCV |
| Face & Landmark Detection | MediaPipe |
| Object Detection | YOLOv8 |
| Dashboard | Streamlit |
| Database | SQLite |
| Visualization | Plotly |

## 🚀 Quick Start

```bash
git clone https://github.com/aizaz512/FocusTrackAI.git
cd FocusTrackAI
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

Launch the dashboard:

```bash
streamlit run dashboard/dashboard.py
```

## 💼 Portfolio Value

This project demonstrates practical computer vision, real-time signal processing, model integration, data persistence and user-facing analytics in one end-to-end application.

## 🔮 Future Improvements

- Real-time performance optimization
- More robust fatigue estimation
- Improved model calibration
- Automated testing
- Production deployment
- Privacy-focused local processing

## 👤 Author

**Aizaz Ur Rahman** — Python Developer & AI/ML Engineer

[GitHub](https://github.com/aizaz512) · [All Projects](https://github.com/aizaz512?tab=repositories)

---

⭐ Star the project if you find it useful.

## License

MIT