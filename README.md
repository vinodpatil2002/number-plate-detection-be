
## 🚀 Number Plate Detection - Backend (FastAPI)  
This is the **backend** for the **Number Plate Detection** project, built using **FastAPI**. It processes uploaded images, detects vehicle number plates using **YOLOv8**, and extracts text using **OCR (PaddleOCR)**.  

---

## 📂 Project Structure  

```
backend/
 ├── app/
 │   ├── models/        # Database models (if needed)
 │   ├── routes/        # API endpoints
 │   ├── services/      # YOLO & OCR logic
 │   ├── main.py        # Main FastAPI app entry point
 │   ├── config.py      # Configuration settings
 │   ├── utils.py       # Helper functions
 │   └── __init__.py    # Package marker
 ├── requirements.txt   # Dependencies file
 ├── .gitignore         # Ignore unnecessary files
 ├── README.md          # Backend documentation
```

---

## 🔧 Installation & Setup  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/vinodpatil2002/number-plate-detection-be.git
cd backend
```

### 2️⃣ Create a Virtual Environment & Install Dependencies  
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### 3️⃣ Run the FastAPI Server  
```sh
uvicorn app.main:app --host 0.0.0.0 --port 5000 --reload
```
Now the backend will be running at **`http://127.0.0.1:5000`**  

---

## 📡 API Endpoints  

| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/detect/` | Upload an image for number plate detection |

---

## 🛠 Technologies Used  
- **FastAPI** (for backend API)  
- **YOLOv8** (for number plate detection)  
- **PaddleOCR** (for text extraction)  
- **Uvicorn** (for ASGI server)  

---

## 🤝 Contributing  
Feel free to fork this repository and submit pull requests.  

---

## 🛑 License  
This project is **open source** and available under the MIT License.  

