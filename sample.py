import json

def load_student_data(course):
    with open("students.json", 'r') as file:
        data = json.load(file)

        for student_key, value in data.items():
                print(value['course'])
    

print(load_student_data("python"))