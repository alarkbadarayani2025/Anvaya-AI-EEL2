# import numpy as np
# from sklearn.linear_model import LinearRegression
# import pickle

# # Example training data
# # [difficulty, chapters, days_left, daily_hours]
# X = np.array([
#     [1, 10, 30, 3],
#     [3, 8, 10, 4],
#     [2, 5, 7, 2],
#     [3, 12, 20, 5],
#     [1, 6, 15, 2],
#     [2, 9, 12, 3]
# ])

# # Output = hours required per chapter
# y = np.array([1, 3, 2, 4, 1, 2.5])

# model = LinearRegression()
# model.fit(X, y)

# # Save model to assure that user will get know about the if model is trained or not 
# pickle.dump(model, open("model.pkl", "wb"))

# print("Model trained & saved")

# # shuffle option 
# import random
# plan = [
#     {"date": "2026-03-01", "subject": "Math", "chapter": "Integration", "hours": 2},
#     {"date": "2026-03-02", "subject": "Physics", "chapter": "Optics", "hours": 3},
#     {"date": "2026-03-03", "subject": "Chemistry", "chapter": "Polymers", "hours": 2},
# ]

# import random

# dates = [p["date"] for p in plan]
# task = [(p["subject"], p["chapter"], p["hours"]) for p in plan]


# import random

# dates = [p["date"] for p in plan]
# task = [(p["subject"], p["chapter"], p["hours"]) for p in plan]


# random.shuffle(task)

# new_plan = []

# for i in range(len(dates)):
#     new_plan.append({
#         "Date": dates[i],
#         "Subject": task[i][0],
#         "Chapter": task[i][1],
#         "Hours": task[i][2]
#     })

# print("\nShuffled Plan:\n")

# for p in new_plan:
#     print(f"{p['Date']} | {p['Subject']} | {p['Chapter']} | {p['Hours']} hrs")
    
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor

# Features:
# difficulty, chapters_total, days_left, daily_hours, revision_flag, time_pressure

X = np.array([

[1,10,30,3,0,0.1],
[2,8,20,4,0,0.2],
[3,12,10,5,0,0.4],
[1,6,15,2,0,0.2],
[2,9,12,3,0,0.3],
[3,15,7,5,0,0.6],

# revision data
[1,10,30,3,1,0.1],
[2,8,20,4,1,0.2],
[3,12,10,5,1,0.4]

])

y = np.array([
1,
2,
3,
1,
2,
3.5,
0.5,
1,
1.2
])

model = RandomForestRegressor(
n_estimators=150,
max_depth=6,
random_state=42
)

model.fit(X,y)

pickle.dump(model,open("model.pkl","wb"))

print("✅ Advanced model trained")
