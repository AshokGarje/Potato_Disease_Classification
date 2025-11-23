# Potato Disease Classification (Deep Learning + FastAPI + React)

This project is an **end-to-end Potato Disease Classification system**
using **TensorFlow/Keras**, deployed using **FastAPI (backend)** and
**React (frontend)**.

The model classifies potato leaf images into:

-   **Healthy**
-   **Early Blight**
-   **Late Blight**

## 🚀 Project Structure

    Potato-Disease-Classification/
    │-- training/
    │   └── Training.ipynb
        ├── PlantVillageDataset
    │-- backend/
    │   ├── main.py
    │   ├── model/
    │   │    └── potatoes.h5
    │-- frontend/
    │-- README.md

## Features

### ✔ Deep Learning Model

-   CNN model to classify potato diseases\
-   Three classes: Healthy, Early Blight, Late Blight

### ✔ FastAPI Backend

-   Accepts image uploads\
-   Returns JSON prediction

### ✔ React Frontend

-   Upload image\
-   Displays prediction

## How to Run

### Backend

    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    uvicorn main:app --reload

### Frontend

    cd frontend/
    npm install
    npm start
