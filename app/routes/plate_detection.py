from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.services.yolo_service import detect_number_plate
from app.services.ocr_service import extract_text


router = APIRouter(prefix="/detect", tags=["Plate Detection"])


@router.post("/")
async def detect_plate(image: UploadFile = File(...)):
    try:
        plate_image = detect_number_plate(await image.read())  # Detect & crop plate
        if plate_image is None:
            return JSONResponse(content={"error": "No plate detected"}, status_code=400)

        text = extract_text(plate_image)  # Extract text from plate
        return {"number_plate": text}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
