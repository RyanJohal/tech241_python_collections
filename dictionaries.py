# Dictionaries

# Key - Value pairs

# Key is the name/reference, Value is the data stored

# Making a dictionary

student_1 = {
    "name": "ryan",
    "stream": "devops",
    "completed_lessons": 4,
    "completed_lessons_names": ["variables", "git", "data_types"]
}

print(student_1)

# How to access

print(student_1["stream"])
print(student_1["completed_lessons_names"][0])

# Changing a value

student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])

student_1["completed_lessons_names"].remove("data_types")
print(student_1["completed_lessons_names"])

# Dictionary methods

print(student_1.keys())
print(student_1.values())

