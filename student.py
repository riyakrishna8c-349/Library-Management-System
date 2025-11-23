# students.py

def add_student(students):
    name = input("Student's full name: ")
    class_no = int(input("Class (number): "))
    sid = int(input("Student ID: "))
    phone = int(input("Phone number: "))

    students.append({
        "Name": name,
        "Class": class_no,
        "ID": sid,
        "Phone": phone
    })

    print(f"{name} added successfully!")
    return students
