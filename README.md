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



ProtectYourChildren/
│── arduino/child_safety.ino        # Arduino firmware (servo + buzzer + ultrasonic)
│── ai/child_safety_ai.py           # YOLOv8 real-time detection + serial comm
│── gui/app.py                      # Streamlit GUI (upload images)
│── model/yolov8n.pt                # YOLO weights (place here or download externally)
│── results/sample.jpg
│── project_results/confusion_matrix.png
│── project_results/correct_vs_incorrect.png
│── project_results/metrics.png
│── requirements.txt
│── README.md
│── LICENSE


# ai/child_safety_ai.py
import cv2
import serial
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("model/yolov8n.pt")

# Connect to Arduino (update COM port or /dev/ttyUSB0 for Linux)
arduino = serial.Serial(port="COM3", baudrate=9600, timeout=1)

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    annotated = results[0].plot()

    # Check detections
    danger = False
    for box in results[0].boxes:
        cls = int(box.cls[0])
        label = model.names[cls]
        if label in ["person", "knife", "scissors"]:
            danger = True

    # Send signal to Arduino
    if danger:
        arduino.write(b'1')  # Close window / trigger buzzer
    else:
        arduino.write(b'0')

    cv2.imshow("Protect Your Children", annotated)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




// arduino/child_safety.ino
#include <Servo.h>

Servo myservo;
int buzzer = 7;
int servoPin = 6;

void setup() {
  Serial.begin(9600);
  myservo.attach(servoPin);
  pinMode(buzzer, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char signal = Serial.read();

    if (signal == '1') {
      // Danger detected → close window + buzzer
      myservo.write(0);      // rotate servo to close
      digitalWrite(buzzer, HIGH);
      delay(500);
      digitalWrite(buzzer, LOW);
    } 
    else if (signal == '0') {
      // Safe → keep window open
      myservo.write(90);     // neutral position
      digitalWrite(buzzer, LOW);
    }
  }
}



streamlit
ultralytics
opencv-python
pillow
numpy
pyserial


👤 Authors
Ahmed (Egypt) — AI & ML Developer
