# Library-Management-System

Overview of the Project:

The Library Management System (LMS) is a Python-based console application designed to help schools and libraries manage books, students, and book-issuing processes.
It provides an easy-to-use menu interface, allowing users to add students, issue books, and view system status.This project is built using modular, object-oriented Python, making the structure clean, readable, and easy to expand.

Features:
View all available books ,Track book availability (Available / Issued)
Add/register students ,Store student details such as name, class, ID, and phone number
Issue books to registered students , Maintain detailed issue records with dates
Contains separate modules for Books,Students,Issue records,Book manager,Student manager,Issue manager,Menu system ,Utility functions

Technologies used:
Language	Python 3
Paradigm	OOP (Object-Oriented Programming)
Development Tools	VS Code / PyCharm / IDLE
Data Structures	Classes, Lists, Dictionaries


Installation & Running
python --version
git clone <your-repository-link>
cd library_system
python main.py
--- Menu ---
1. Add Student
2. Issue Book
3. Status Details
4. Exit

Instructions for testing
Test 1: Add Student
Select option 1
Enter valid information
Student should appear in the student list

Test 2: Issue a Book
Select option 2
Enter a valid Book ID
Enter a valid Student ID
Check if book status changes to Issued

Test 3: Issue an Already Issued Book
Try issuing the same book again

System should display:
"Book already issued!"

Test 4: Invalid Student ID
Enter a student ID not in the system
Should display:
"No student found with that ID!"

Test 5: View Status
Choose option 3
Verify:
Book list
Student list
Issue records

<img width="581" height="209" alt="image" src="https://github.com/user-attachments/assets/94bbae41-8c9c-4db2-b2d5-e53e0729ceee" />

<img width="1028" height="236" alt="image" src="https://github.com/user-attachments/assets/6b473177-181d-4879-a8cc-bcd8611e0491" />

<img width="500" height="64" alt="image" src="https://github.com/user-attachments/assets/f1666ec4-e65f-42b4-9027-5538a712c07d" />

<img width="1430" height="352" alt="image" src="https://github.com/user-attachments/assets/296629ba-abae-43ec-a82f-0be287461994" />







