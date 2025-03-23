import torch
import cv2
import numpy as np
from ultralytics import YOLO
from app.utils.image_utils import read_image

# Load YOLOv8 model
model = YOLO("models/yolov8n.pt")


def detect_number_plate(image_bytes: bytes):
    img = read_image(image_bytes)

    # Run YOLO detection
    results = model(img)

    # Extract bounding box of the number plate
    for result in results:
        for box in result.boxes.xyxy:  # Get coordinates
            x1, y1, x2, y2 = map(int, box[:4])
            plate_img = img[y1:y2, x1:x2]  # Crop the plate region
            return plate_img  # Return cropped image

    return None  # No plate detected
