import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    setImage(file);
    setPreview(URL.createObjectURL(file));
    setResult(null);
  };

  const handlePredict = async () => {
    if (!image) return;
    setLoading(true);

    const formData = new FormData();
    formData.append("file", image);

    try {
      const response = await axios.post(
        "http://localhost:8000/predict",
        formData,
        { headers: { "Content-Type": "multipart/form-data" } }
      );
      setResult(response.data);
    } catch (error) {
      console.error(error);
    }
    setLoading(false);
  };

  return (
    <div className="app-container">
      <h1 className="title">🌱 Potato Disease Classifier</h1>
      <p className="subtitle">Upload a leaf image and detect the disease.</p>

      <div className="card">
        <label className="upload-box">
          <input
            type="file"
            accept="image/*"
            onChange={handleImageChange}
            hidden
          />
          <span className="upload-text">📁 Click to Select Image</span>
        </label>

        {preview && (
          <div className="image-preview">
            <img src={preview} alt="preview" />
          </div>
        )}

        <button
          className="predict-btn"
          onClick={handlePredict}
          disabled={loading}
        >
          {loading ? "Predicting..." : "🔍 Predict Disease"}
        </button>

        {result && (
          <div className="result-box">
            <h3>Prediction: <span>{result.class}</span></h3>
            <p>Confidence: <strong>{result.confidence}%</strong></p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
