import numpy as np
import json
import pickle
from datetime import datetime, timedelta
from predict import predict_hours
from sklearn.ensemble import RandomForestRegressor

# ------------------------
# USER INPUT
# ------------------------

subject = input("Enter Subject: ")
chapters = int(input("Total Chapters: "))
difficulty = int(input("Difficulty (1 Easy - 3 Hard): "))
days_left = int(input("Days Left for Exam: "))
daily_hours = float(input("Daily Study Hours: "))

# ------------------------
# PREDICT HOURS
# ------------------------

hours_per_chapter = predict_hours(
    difficulty,
    chapters,
    days_left,
    daily_hours,
    revision_flag=0
)

# ------------------------
# AUTO TODAY DATE
# ------------------------

today = datetime.today()

schedule = []

chapter = 1

for day in range(days_left):

    date = today + timedelta(days=day)

    remaining_hours = daily_hours

    while remaining_hours >= hours_per_chapter and chapter <= chapters:

        schedule.append({
            "date": str(date.date()),
            "subject": subject,
            "chapter": f"Chapter {chapter}",
            "status": "Pending",
            "required_time": hours_per_chapter
        })

        remaining_hours -= hours_per_chapter
        chapter += 1


# ------------------------
# PRINT STUDY PLAN
# ------------------------

print("\nStudy Plan\n")
print("Date | Subject | Chapter | Status | Required Time")

for s in schedule:
    print(f"{s['date']} | {s['subject']} | {s['chapter']} | {s['status']} | {s['required_time']} hrs")

# ------------------------
# SAVE SCHEDULE
# ------------------------

with open("schedule.json","w") as f:
    json.dump(schedule,f,indent=4)

# ------------------------
# STORE DATASET
# ------------------------

revision_flag = 0
chapters_per_day = chapters / days_left
time_pressure = chapters_per_day / daily_hours

features = np.array([[

    difficulty,
    chapters,
    days_left,
    daily_hours,
    revision_flag,
    time_pressure

]])

try:
    X_old = np.load("X.npy")
    y_old = np.load("y.npy")
except:
    X_old = np.empty((0,6))
    y_old = np.array([])

duplicate = False

for row in X_old:
    if np.array_equal(row,features[0]):
        duplicate = True
        break

if not duplicate:

    X_new = np.vstack([X_old,features])
    y_new = np.append(y_old,hours_per_chapter)

    np.save("X.npy",X_new)
    np.save("y.npy",y_new)

    print("\nNew training data stored")

# ------------------------
# RETRAIN MODEL
# ------------------------

model = RandomForestRegressor(
    n_estimators=150,
    max_depth=6,
    random_state=42
)

model.fit(np.load("X.npy"),np.load("y.npy"))

pickle.dump(model,open("model.pkl","wb"))

print("Model updated")