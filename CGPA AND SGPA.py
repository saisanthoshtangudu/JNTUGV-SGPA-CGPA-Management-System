
# JNTUGV SGPA & CGPA Management System

import os
import glob

GRADE_POINTS = {
    "A+": 10,
    "A": 9,
    "B": 8,
    "C": 7,
    "D": 6,
    "E": 5,
    "F": 0
}

FILE_NAME = "student_records.txt"


def calculate_sgpa(subjects):
    total_credits = 0
    total_points = 0

    for subject in subjects:
        total_credits += subject["credits"]
        total_points += subject["credits"] * subject["grade_point"]

    if total_credits == 0:
        return 0

    return total_points / total_credits


def calculate_cgpa(sgpa_list):
    if len(sgpa_list) == 0:
        return 0

    return sum(sgpa_list) / len(sgpa_list)


def add_student():
    print("\n===== ADD STUDENT =====")

    roll_no = input("Enter Roll Number: ").upper()
    name = input("Enter Student Name: ")

    # create a safe filename from the student name
    safe_name = name.strip().replace(" ", "_") if name.strip() else "unknown"
    file_name = f"{safe_name}_record.txt"

    semesters = int(input("Enter Number of Semesters: "))

    sgpa_list = []

    with open(file_name, "a") as file:

        file.write("\n")
        file.write("=" * 50 + "\n")
        file.write(f"Roll Number : {roll_no}\n")
        file.write(f"Student Name: {name}\n")

        for sem in range(1, semesters + 1):

            print(f"\nSemester {sem}")

            num_subjects = int(input("Enter Number of Subjects: "))

            subjects = []

            for i in range(1, num_subjects + 1):

                print(f"\nSubject {i}")

                subject_name = input("Enter Subject Name: ")

                while True:
                    grade = input(
                        "Enter Grade (A+, A, B, C, D, E, F): "
                    ).upper()

                    if grade in GRADE_POINTS:
                        break

                    print("Invalid Grade! Try Again.")

                credits = int(input("Enter Credits: "))

                subjects.append({
                    "name": subject_name,
                    "grade": grade,
                    "credits": credits,
                    "grade_point": GRADE_POINTS[grade]
                })

            sgpa = calculate_sgpa(subjects)
            sgpa_list.append(sgpa)

            file.write(f"\nSemester {sem}\n")

            for s in subjects:
                file.write(
                    f"{s['name']} | Grade: {s['grade']} | Credits: {s['credits']}\n"
                )

            file.write(f"SGPA Semester {sem}: {sgpa:.2f}\n")

            print(f"Semester {sem} SGPA = {sgpa:.2f}")

        cgpa = calculate_cgpa(sgpa_list)

        file.write(f"\nFinal CGPA: {cgpa:.2f}\n")
        file.write("=" * 50 + "\n")

    print("\nStudent Record Saved Successfully.")
    print(f"CGPA = {cgpa:.2f}")


def view_records():
    print("\n===== STUDENT RECORDS =====")

    name = input("Enter Student Name (leave blank to show all): ").strip()

    if name == "":
        files = glob.glob("*_record.txt")

        if not files:
            print("No Records Found.")
            return

        for fname in files:
            print(f"\n--- {fname} ---\n")
            with open(fname, "r") as f:
                print(f.read())

    else:
        safe_name = name.replace(" ", "_")
        fname = f"{safe_name}_record.txt"

        try:
            with open(fname, "r") as file:
                data = file.read()

                if data.strip() == "":
                    print("No Records Found.")
                else:
                    print(data)

        except FileNotFoundError:
            print("No Record File Found.")


def search_student():
    print("\n===== SEARCH STUDENT =====")
    name = input("Enter Student Name (leave blank to search all): ").strip()
    roll = input("Enter Roll Number: ").upper()

    files_to_search = []

    if name:
        safe_name = name.replace(" ", "_")
        files_to_search = [f"{safe_name}_record.txt"]
    else:
        files_to_search = glob.glob("*_record.txt")

    found = False

    for fname in files_to_search:
        try:
            with open(fname, "r") as file:
                lines = file.readlines()

            for i in range(len(lines)):
                if f"Roll Number : {roll}" in lines[i]:
                    found = True
                    print(f"\nStudent Found in {fname}\n")

                    j = i

                    while j < len(lines):
                        print(lines[j], end="")

                        if "=" * 50 in lines[j] and j != i:
                            break

                        j += 1

                    break

            if found:
                break

        except FileNotFoundError:
            continue

    if not found:
        print("Student Record Not Found.")


def main():

    while True:

        print("\n")
        print("===== JNTUGV SGPA & CGPA MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Records")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_records()

        elif choice == "3":
            search_student()

        elif choice == "4":
            print("Thank You")
            break

        else:
            print("Invalid Choice")


main()
