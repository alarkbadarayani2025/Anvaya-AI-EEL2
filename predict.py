# import pickle
# import numpy as np

# model = pickle.load(open("model.pkl", "rb"))

# def predict_hours(difficulty, chapters, days_left, daily_hours):
#     data = np.array([[difficulty, chapters, days_left, daily_hours]])
#     prediction = model.predict(data)
#     return round(float(prediction[0]), 2)

import pickle
import numpy as np

model = pickle.load(open("model.pkl","rb"))

def predict_hours(difficulty, chapters_total, days_left, daily_hours, revision_flag):

    chapters_per_day = chapters_total / days_left

    time_pressure = chapters_per_day / daily_hours

    data = np.array([[

        difficulty,
        chapters_total,
        days_left,
        daily_hours,
        revision_flag,
        time_pressure

    ]])

    hours = model.predict(data)[0]

    hours = round(float(hours),2)

    if hours < 0.5:
        hours = 0.5

    return hours
