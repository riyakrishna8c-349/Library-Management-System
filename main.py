# main.py

import sys
from books import books
from students import add_student
from issues import issue_book
from menu import status_details

students = []
issues = []

print("Welcome to the Library Management System")

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
