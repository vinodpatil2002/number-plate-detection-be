import cv2
import numpy as np
import io
from PIL import Image

def read_image(image_bytes):
    """ Reads and converts image bytes to OpenCV format """
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    return np.array(image)

def preprocess_plate(plate_img):
    """ Preprocess number plate before OCR (grayscale + thresholding) """
    gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh
