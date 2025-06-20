# Potato Disease Classification

This project focuses on building a machine learning model to classify potato leaf diseases using image classification techniques. 
It aims to help farmers and agricultural specialists identify diseases early and take corrective action.

## Objective

To develop a robust classification model that can detect and classify common potato leaf diseases from images using deep learning techniques.

##  Dataset

The dataset consists of potato leaf images categorized into the following classes:

 **Early Blight**
 **Late Blight**
 **Healthy**

Each class contains images captured under varying conditions to simulate real-world scenarios.

## Technologies Used

- Python
- TensorFlow / Keras
- NumPy, Pandas
- Matplotlib, Seaborn
- Scikit-learn
- OpenCV (for image preprocessing)

##  Model Workflow

1. **Data Loading & Preprocessing**
   - Image resizing
   - Normalization
   - Data augmentation

2. **Model Building**
   - CNN architecture (Custom or pre-trained like ResNet/VGG)
   - Loss function: Categorical Crossentropy
   - Optimizer: Adam

3. **Model Evaluation**
   - Accuracy, precision, recall, F1-score
   - Confusion matrix

4. **Deployment (optional)**
   - Model saved using `model.save()` or `joblib`

## Results

- Training Accuracy: ~XX%
- Validation Accuracy: ~XX%
- Confusion matrix shows strong performance across all classes.
