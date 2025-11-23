# menu.py

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
