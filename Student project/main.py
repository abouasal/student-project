from student.grades import*
from student.status import*
def main():
    name = input("enter student name: ")
    grades = []
    for i in range (3):
        while True:
            try:
                grade = float (input(f"enter grade for subject {i+1}: "))
                if 0 <= grade <= 20:
                   grades.append(grade)
                   break
                print("grade must be between 0 and 20")
            except ValueError:
                print("please enter a valid number")
    avg = average(grades)
    max_grade = maximum(grades)
    min_grade = minimum(grades)
    result = check_status(avg)
    print("\n--- Student Report ---")
    print("Name:",name)
    print("Grades:",grades)
    print("Average:",avg)
    print("Highest Grade:",max_grade)
    print("Lowest Grade:",min_grade)
    print("Status:",result)
if __name__ == "__main__":
    main()   


