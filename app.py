from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle
import random
from datetime import datetime

app = Flask(__name__)

# Load ML model
model = pickle.load(open("model.pkl", "rb"))

difficulty_map = {
    "Easy": 1,
    "Medium": 2,
    "Hard": 3
}

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate_plan", methods=["POST"])
def generate_plan():
    data = request.json

    student_name = data["name"]
    daily_hours = float(data["hours"])
    subjects = data["subjects"]

    plan = []

    for sub in subjects:
        subject_name = sub["name"]
        exam_date = datetime.strptime(sub["exam"], "%Y-%m-%d")
        days_left = (exam_date - datetime.today()).days
        if days_left <= 0:
            days_left = 1

        chapters = sub["chapters"]

        for ch in chapters:
            diff = 2   # default medium
            hours = model.predict(
                np.array([[diff, len(chapters), days_left, daily_hours]])
            )[0]

            plan.append({
                "Date": "Auto",
                "Subject": subject_name,
                "Chapter": ch["name"],
                "Hours": round(float(hours), 2)
            })

    random.shuffle(plan)

    return jsonify(plan)


if __name__ == "__main__":
    app.run(debug=True)