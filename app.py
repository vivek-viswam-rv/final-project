from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os

# Load the saved model
model = joblib.load("final_model.joblib")

# Initialize FastAPI app
app = FastAPI()

# Define the request body
class PredictionInput(BaseModel):
    Alcohol: float
    MalicAcid: float
    Ash: float
    AlcalinityOfAsh: float
    Magnesium: float
    TotalPhenols: float
    Flavanoids: float
    NonflavanoidPhenols: float
    Proanthocyanins: float
    ColorIntensity: float
    Hue: float
    OD280_OD315: float
    Proline: float

# Define a route for health check
@app.get("/")
def read_root():
    return {"message": "Wine Classification Model API is running"}

# Define a prediction route
@app.post("/predict")
def predict(input_data: PredictionInput):
    # Convert input data to a format suitable for the model
    features = np.array([[input_data.Alcohol, input_data.MalicAcid, input_data.Ash,
                           input_data.AlcalinityOfAsh, input_data.Magnesium,
                           input_data.TotalPhenols, input_data.Flavanoids,
                           input_data.NonflavanoidPhenols, input_data.Proanthocyanins,
                           input_data.ColorIntensity, input_data.Hue,
                           input_data.OD280_OD315, input_data.Proline]])

    # Make prediction
    prediction = model.predict(features)

    return {"prediction": int(prediction[0])}

# Ensure the app binds to Heroku's $PORT
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # Get the PORT from environment
    uvicorn.run(app, host="0.0.0.0", port=port)
