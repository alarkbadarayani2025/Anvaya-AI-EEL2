import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

def predict_hours(difficulty, chapters, days_left, daily_hours):
    data = np.array([[difficulty, chapters, days_left, daily_hours]])
    prediction = model.predict(data)
    return round(float(prediction[0]), 2)
