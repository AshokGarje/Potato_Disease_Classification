from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from PIL import Image
import tensorflow as tf

app = FastAPI()

# CORS so frontend can talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your trained model
MODEL_PATH = "models/potatoes.h5"
model = tf.keras.models.load_model(MODEL_PATH, compile=False)


# Class names
class_names = ["Early Blight", "Late Blight", "Healthy"]

def preprocess_image(image: Image.Image):
    image = image.resize((256, 256))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(file.file)
    processed = preprocess_image(image)

    prediction = model.predict(processed)
    class_idx = np.argmax(prediction)
    confidence = float(np.max(prediction))

    return {
        "class": class_names[class_idx],
        "confidence": round(confidence * 100, 2)
    }


@app.get("/")
def home():
    return {"message": "Potato Disease Detection Backend Running"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
