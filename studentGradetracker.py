def get_grades():
    grades = {}
    print("Enter grades for each subject. Type 'done' when finished.")
    while True:
        subject = input("Subject name: ")
        if subject.lower() == 'done':
            break
        try:
            grade = float(input(f"Grade for {subject}: "))
            if grade < 0 or grade > 100:
                print("Please enter a grade between 0 and 100.")
                continue
            grades[subject] = grade
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")
    return grades

def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades.values()) / len(grades)

def main():
    print("Student Grade Tracker")
    grades = get_grades()
    if grades:
        print("\nGrades entered:")
        for subject, grade in grades.items():
            print(f"{subject}: {grade}")
        average = calculate_average(grades)
        print(f"\nAverage grade: {average:.2f}")
    else:
        print("No grades were entered.")

if __name__ == "__main__":
    main()
