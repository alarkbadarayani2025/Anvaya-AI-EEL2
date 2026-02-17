def collect_student_data(name, daily_time, subjects_data):
    student_data = {}

    student_data["name"] = name
    student_data["daily_study_time"] = float(daily_time)

    subjects = {}

    # subjects_data will come from GUI
    # format: list of dictionaries

    for sub in subjects_data:
        subject_name = sub["subject_name"]
        exam_date = sub["exam_date"]
        chapters = sub["chapters"]

        subjects[subject_name] = {
            "exam_date": exam_date,
            "chapters": chapters
        }

    student_data["subjects"] = subjects

    # Now create output text (instead of print)
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
