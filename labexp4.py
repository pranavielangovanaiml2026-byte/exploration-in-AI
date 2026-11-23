# Student Record Management with List, Tuple, Dictionary and CSV

import csv

students = [
    {"RollNo": "201", "Name": "Priya", "Department": "CSE", "Mark": 88},
    {"RollNo": "202", "Name": "Arun", "Department": "ECE", "Mark": 92},
    {"RollNo": "203", "Name": "Divya", "Department": "AIML", "Mark": 79}
]

# Tuple example: fixed course details
course = ("Java", 3)
print("Course Tuple:", course)

# Write to a text file
with open("students.txt", "w") as file:
    for student in students:
        file.write(str(student) + "\n")

# Write to a CSV file
with open("students.csv", "w", newline="") as file:
    fields = ["RollNo", "Name", "Department", "Mark"]
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(students)

# Read from the CSV file
print("\n--- Records from CSV ---")
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["RollNo"], row["Name"], row["Department"], row["Mark"])