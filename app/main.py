from fastapi import FastAPI
from app.routes.plate_detection import router as plate_detection_router

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Number Plate Detector API (YOLO + EasyOCR)")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (you can restrict it to your frontend URL)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include routes
app.include_router(plate_detection_router)


@app.get("/")
def root():
    return {"message": "Welcome to the Number Plate Detector API"}
