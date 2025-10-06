from datetime import datetime
import pandas as pd

class Exam:
    id = int
    name = str
    solved = datetime
    result = str
    teacher_id = int
    def __init__(self, id, name, solved, result, teacher_id):
        self.id = id
        self.name = name
        self.solved = solved
        self.result = result
        self.teacher_id = teacher_id


exams = [
    Exam(1, "Mathe Algebra", datetime(2025, 5, 21, 10, 0), result = "5.8", teacher_id = 1),
    Exam(2, "Geschichte 1.Weltkrieg", datetime(2025, 5, 21, 10, 0), result = "3.45", teacher_id = 1),
    Exam(3, "Deutsch Aufsatz schreiben", datetime(2025, 5, 21, 10, 0), result = "4.5", teacher_id = 2)
]

exam_data = [
    {
        "id": exam.id,
        "name": exam.name,
        "solved": exam.solved,
        "result": exam.result,
        "teacher_id": exam.teacher_id
    }
    for exam in exams
]

df = pd.DataFrame(exam_data)
csv_path  = 'exams.csv'
df.to_csv(csv_path, index = False)
print (csv_path)