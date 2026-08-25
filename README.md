# 🎯 FocusTrack AI

> **Real-time AI focus and productivity monitoring using computer vision and machine learning.**

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?logo=opencv&logoColor=white)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-0097A7)](https://ai.google.dev/edge/mediapipe/solutions/guide)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Computer%20Vision-111111)](https://docs.ultralytics.com/)

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

## 🛠️ Technology Stack

Python · OpenCV · MediaPipe · YOLOv8 · Streamlit · SQLite · Plotly

## 🏗️ Pipeline

```text
Camera → Face/Eye/Head Detection → Behavioral Signals → Focus Score → Analytics Dashboard
```

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

Dashboard:

```bash
streamlit run dashboard/dashboard.py
```

## 📌 Portfolio Value

This project demonstrates practical computer vision, real-time signal processing, model integration, data persistence and user-facing analytics.

## 👤 Author

**Aizaz Ur Rahman** — Python Developer & AI/ML Engineer

[GitHub](https://github.com/aizaz512) · [All Projects](https://github.com/aizaz512?tab=repositories)

---

⭐ Star the project if you find it useful.

## License

MIT
