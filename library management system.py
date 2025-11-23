import sys

books = [
    {"Book": "The Prodigy", "Author": "Marie", "Book_ID": "30AAB", "Genre": "Autobiography", "Status": "Available"},
    {"Book": "His Duchess", "Author": "shaer", "Book_ID": "03AAC", "Genre": "Romance", "Status": "Available"},
    {"Book": "Care", "Author": "Marie", "Book_ID": "36AAF", "Genre": "Mystery", "Status": "Available"},
    {"Book": "Mend", "Author": "ezra", "Book_ID": "27AAG", "Genre": "Thriller", "Status": "Available"},
    {"Book": "Knox", "Author": "Fera", "Book_ID": "29AAA", "Genre": "Horror", "Status": "Available"},
    {"Book": "Etheral", "Author": "Era rexon", "Book_ID": "29AAM", "Genre": "Fiction", "Status": "Available"},
]

students = []
issues = []

print("Welcome to the Library Management System")

# adding new student 
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
    print(students)
    return students


def issue_book(books, issues, students):

# checking if book is available
    print("\nAvailable Books:")
    for b in books:
        print(b)

    book_id = input("\nEnter Book ID to issue: ").upper()

    
    book = next((b for b in books if b["Book_ID"] == book_id), None)

    if not book:
        print("Invalid book ID!")
        return books, issues

    if book["Status"] != "Available":
        print("Book already issued!")
        return books, issues

    print("\nRegistered Students:")
    for s in students:
        print(s)

    student_id = input("\nStudent ID who is taking the book: ")
    
    if not student_id.isdigit():
        print("Invalid ID format!")
        return books, issues

    student_id = int(student_id)

    # find student
    student = next((s for s in students if s["ID"] == student_id), None)

    if not student:
        print("No student found with that ID!")
        return books, issues

    issue_date = input("Issue date (YYYY-MM-DD): ")
    return_date = input("Return date (YYYY-MM-DD): ")

   
    book["Status"] = "Issued"

    issues.append({
        "Student_ID": student_id,
        "Book_ID": book_id,
        "Issue_Date": issue_date,
        "Return_Date": return_date,
        "Status": "Issued"
    })

    print(f"\nBook {book_id} issued to student {student_id}.")
    return books, issues

def status_details(students, issues, books):

    print("\n--- Books Status ---")
    for b in books:
        print(b)

    print("\n--- Students ---")
    if len(students) == 0:
        print("No students registered.")
    else:
        for s in students:
            print(s)

    print("\n--- Issued Books ---")
    if len(issues) == 0:
        print("No books issued.")
    else:
        for i in issues:
            print(i)

while True:
    print("\n--- Menu ---")
    print("1. Add Student")
    print("2. Issue Book")
    print("3. Status Details")
    print("4. Exit\n")

    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Enter a valid number!")
        continue

    if choice == 1:
        students = add_student(students)

    elif choice == 2:
        books, issues = issue_book(books, issues, students)

    elif choice == 3:
        status_details(students, issues, books)

    elif choice == 4:
        print("Goodbye!")
        sys.exit()

    else:
        print("Invalid choice! Try again.")
