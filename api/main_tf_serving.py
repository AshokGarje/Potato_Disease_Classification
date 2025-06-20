from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import requests

# Initialize FastAPI app
app = FastAPI()

# CORS setup (optional but useful if using frontend like React)
origins = ["http://localhost", "http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model prediction endpoint
endpoint = "http://localhost:8501/v1/models/potato_model:predict"

# Class labels
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

# Ping route
@app.get("/ping")
async def ping():
    return {"message": "Hello, I am alive"}

# Convert uploaded image to numpy array
def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

# Predict route
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)

    json_data = {
        "instances": img_batch.tolist()
    }

    response = requests.post(endpoint, json=json_data)

    # Debug response
    print("STATUS CODE:", response.status_code)
    print("RESPONSE JSON:", response.json())

    if response.status_code != 200 or "predictions" not in response.json():
        return {
            "error": "Something went wrong with the model prediction",
            "details": response.json()
        }

    prediction = np.array(response.json()["predictions"][0])
    predicted_class = CLASS_NAMES[np.argmax(prediction)]
    confidence = np.max(prediction)

    return {
        "class": predicted_class,
        "confidence": float(confidence)
    }

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host='192.168.1.159', port=8001)
