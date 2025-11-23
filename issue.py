# issues.py

def issue_book(books, issues, students):

    print("\nAvailable Books:")
    for b in books:
        print(b)

    book_id = input("\nEnter Book ID to issue: ").upper()

    # find book
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
