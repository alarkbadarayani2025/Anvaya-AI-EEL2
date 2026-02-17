import tkinter as tk
from tkinter import ttk
from logic import collect_student_data

# -------- BACKEND FUNCTION (your logic) --------
def collect_student_data(name, daily_time, subjects_data):
    student_data = {}

    student_data["name"] = name
    student_data["daily_study_time"] = float(daily_time)

    subjects = {}

    for sub in subjects_data:
        subject_name = sub["subject_name"]
        exam_date = sub["exam_date"]
        chapters = sub["chapters"]

        subjects[subject_name] = {
            "exam_date": exam_date,
            "chapters": chapters
        }

    student_data["subjects"] = subjects

    output = "\n========== STUDENT DATA ==========\n"
    output += f"Name: {student_data['name']}\n"
    output += f"Daily Study Time: {student_data['daily_study_time']} hours\n"

    for subject, details in student_data["subjects"].items():
        output += f"\nSubject: {subject}\n"
        output += f"Exam Date: {details['exam_date']}\n"
        output += "Chapters:\n"
        for chapter in details["chapters"]:
            output += f"  - {chapter[0]} | Difficulty: {chapter[1]}\n"

    return output


# -------- MAIN WINDOW --------
root = tk.Tk()
root.title("AI Study Planner")
root.geometry("900x700")
root.configure(bg="#0f172a")

main_frame = tk.Frame(root, bg="#0f172a")
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# -------- TOP INPUT --------
tk.Label(main_frame, text="Student Name", fg="white", bg="#0f172a").pack()
name_entry = tk.Entry(main_frame, width=40)
name_entry.pack(pady=5)

tk.Label(main_frame, text="Daily Study Hours", fg="white", bg="#0f172a").pack()
time_entry = tk.Entry(main_frame, width=20)
time_entry.pack(pady=5)

tk.Label(main_frame, text="Number of Subjects", fg="white", bg="#0f172a").pack(pady=10)
num_subject_entry = tk.Entry(main_frame, width=10)
num_subject_entry.pack()

subjects_container = tk.Frame(main_frame, bg="#0f172a")
subjects_container.pack(pady=20)

subject_blocks = []


# -------- CREATE SUBJECT BLOCKS --------
def create_subject_blocks():
    for widget in subjects_container.winfo_children():
        widget.destroy()

    subject_blocks.clear()

    n = int(num_subject_entry.get())

    for i in range(n):
        frame = tk.LabelFrame(subjects_container, text=f"Subject {i+1}", bg="#1e293b", fg="white", padx=10, pady=10)
        frame.pack(fill="x", pady=10)

        tk.Label(frame, text="Subject Name", bg="#1e293b", fg="white").grid(row=0, column=0)
        subject_entry = tk.Entry(frame)
        subject_entry.grid(row=0, column=1)

        tk.Label(frame, text="Exam Date", bg="#1e293b", fg="white").grid(row=1, column=0)
        exam_entry = tk.Entry(frame)
        exam_entry.grid(row=1, column=1)

        tk.Label(frame, text="Number of Chapters", bg="#1e293b", fg="white").grid(row=2, column=0)
        chapter_count_entry = tk.Entry(frame)
        chapter_count_entry.grid(row=2, column=1)

        chapter_container = tk.Frame(frame, bg="#1e293b")
        chapter_container.grid(row=4, column=0, columnspan=2)

        chapters_inputs = []

        def create_chapters(container=chapter_container, count_entry=chapter_count_entry, store=chapters_inputs):
            for w in container.winfo_children():
                w.destroy()
            store.clear()

            c = int(count_entry.get())

            for j in range(c):
                tk.Label(container, text=f"Chapter {j+1}", bg="#1e293b", fg="white").grid(row=j, column=0)

                chap_entry = tk.Entry(container)
                chap_entry.grid(row=j, column=1)

                diff = ttk.Combobox(container, values=["Easy", "Medium", "Hard"], width=10)
                diff.grid(row=j, column=2)

                store.append((chap_entry, diff))

        tk.Button(frame, text="Create Chapters", command=create_chapters, bg="#38bdf8").grid(row=3, column=0, columnspan=2, pady=5)

        subject_blocks.append({
            "subject": subject_entry,
            "exam": exam_entry,
            "chapters": chapters_inputs
        })


tk.Button(main_frame, text="Create Subjects", command=create_subject_blocks, bg="#22c55e").pack(pady=10)


# -------- GENERATE RESULT --------
def generate_result():
    subjects_list = []

    for block in subject_blocks:
        subject_name = block["subject"].get()
        exam_date = block["exam"].get()

        chapters = []
        for chap_entry, diff in block["chapters"]:
            chapters.append((chap_entry.get(), diff.get()))

        subjects_list.append({
            "subject_name": subject_name,
            "exam_date": exam_date,
            "chapters": chapters
        })

    result = collect_student_data(
        name_entry.get(),
        time_entry.get(),
        subjects_list
    )

    output_box.delete("1.0", "end")
    output_box.insert("end", result)


tk.Button(main_frame, text="Generate Study Plan", command=generate_result, bg="#f59e0b").pack(pady=20)

# -------- OUTPUT BOX --------
output_box = tk.Text(main_frame, height=12, width=100)
output_box.pack()

root.mainloop()
