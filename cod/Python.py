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