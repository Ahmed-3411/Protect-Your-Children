# 🛡️ Protect Your Children — AI + IoT Child Safety System

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](#)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-0A0A0A?logo=ultralytics)](#)
[![Arduino](https://img.shields.io/badge/Arduino-Mega-00979D?logo=arduino&logoColor=white)](#)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?logo=opencv&logoColor=white)](#)
[![Streamlit](https://img.shields.io/badge/Streamlit-Optional-FF4B4B?logo=streamlit&logoColor=white)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **EN:** An intelligent safety system that detects children near windows or holding sharp objects and triggers alarms/actuators.  
> **AR:** نظام ذكي لحماية الأطفال عبر الرؤية الحاسوبية والتحكم بالأجهزة (Arduino) لإطلاق تنبيه وإغلاق النافذة عند الاقتراب أو عند اكتشاف أداة حادة.

---

## 📑 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Project Structure](#-project-structure)
- [Hardware](#-hardware)
- [Wiring (Arduino Mega)](#-wiring-arduino-mega)
- [Software Requirements](#-software-requirements)
- [Quick Start](#-quick-start)
- [GUI (Optional)](#-gui-optional)
- [Notebook Demo](#-notebook-demo)
- [Model Weights & Dataset](#-model-weights--dataset)
- [Training (Custom Data)](#-training-custom-data)
- [Evaluation](#-evaluation)
- [Troubleshooting](#-troubleshooting)
- [Security & Privacy](#-security--privacy)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Authors](#-authors)

---

## 🔎 Overview
The project combines **AI (YOLOv8)** with **IoT (Arduino)** to:
- Detect **children** near risky zones (e.g., windows, balconies).
- Detect **sharp objects** (e.g., knife/scissors).
- Trigger **alarm** and **servo** to close a window or notify guardians.

> Intended for **education and prototyping**. Not a certified safety device.

---

## ✨ Features
- Real-time video inference using **YOLOv8**.
- Hardware control: **Ultrasonic** distance sensing, **Buzzer** alarm, **Servo** actuation.
- Serial integration: AI → Arduino to trigger actions (`'1'` close / `'0'` open).
- Optional **GUI (Streamlit)** and **Jupyter Notebook** demo.
- Clear, modular repo structure ready for GitHub.

---

## 🎬 Demo
Add your media under `results/` and reference them here:

- **GIF:**  
  ![Demo](results/demo.gif)
- **Screenshots:**  
  ![Detection](results/sample.jpg)

---

## 🗂 Project Structure
