# 🛡️ Protect Your Children — AI + IoT Child Safety System

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](#)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-0A0A0A?logo=ultralytics)](#)
[![Arduino](https://img.shields.io/badge/Arduino-Mega-00979D?logo=arduino&logoColor=white)](#)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?logo=opencv&logoColor=white)](#)
[![Streamlit](https://img.shields.io/badge/Streamlit-GUI-FF4B4B?logo=streamlit&logoColor=white)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Protect Your Children** is an AI + IoT prototype that detects children near dangerous zones (e.g., windows, balconies) or holding sharp objects.  
> It triggers **alerts/actuators** via Arduino to prevent accidents.

---

## 📑 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Results](#-results)
- [GUI](#-gui)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Python Code (AI)](#-python-code-ai)
- [Arduino Code (IoT)](#-arduino-code-iot)
- [Requirements](#-requirements)
- [Authors](#-authors)
- [License](#-license)

---

## 🔎 Overview
This project combines **Computer Vision (YOLOv8)** with **IoT (Arduino)** to:
- Detect children near windows/balconies.
- Detect sharp objects (e.g., knife, scissors).
- Trigger Arduino **servo + buzzer** to close the window or raise an alarm.
- Provide an **easy-to-use GUI (Streamlit)** for image-based testing.

⚠️ **Note:** This is for educational and prototyping purposes only. It is not a certified safety device.

---

## ✨ Features
- Real-time detection with **YOLOv8**.  
- Simple web GUI built with **Streamlit** (no camera required).  
- Upload an image → get detection results instantly.  
- Bounding boxes drawn on the image.  
- Object list with confidence scores.  

---

## 🎬 Results
- **Sample Detection**  
  ![Sample Detection](results/sample.jpg)

- **Confusion Matrix**  
  ![Confusion Matrix](project_results/confusion_matrix.png)

- **Correct vs Incorrect Predictions**  
  ![Correct vs Incorrect](project_results/correct_vs_incorrect.png)

- **Model Performance Metrics**  
  ![metrics](project_results/metrics.png)

---

## 🖼 GUI
A lightweight GUI built with **Streamlit**:  

- Upload an image (JPG/PNG).  
- The AI model processes it with YOLOv8.  
- The system returns the annotated image + detected objects.  

Example interface:  
![GUI Demo](results/gui_demo.png)

---

## 🚀 Quick Start

### 1) Clone & Install
```bash
git clone https://github.com/Ahmed-3411/Protect-Your-Children.git
cd Protect-Your-Children
pip install -r requirements.txt
