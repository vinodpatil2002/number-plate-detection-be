import easyocr
import cv2

reader = easyocr.Reader(["en"], gpu=False)  # Disable GPU to reduce RAM usage



def extract_text(plate_img):
    gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)
    result = reader.readtext(gray)

    return " ".join([text[1] for text in result]) if result else "No plate detected"
