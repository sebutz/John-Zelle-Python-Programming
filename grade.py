# grade.py
# This program accepts quiz score and prints a grade.
'''
def main():

    grades = ["F", "F", "D", "C", "B", "A"]

    points = int(input("How many points did you get? "))

    print("Your grade is", grades[points] + ".")

main()
'''

def main():

    grades = ["F", "F", "F", "F", "F", "F", "D", "C", "B", "A", "A"]

    points = int(input("How many points did you get? "))

    grade = points // 10

    print("Your grade is", grades[grade] + ".")

main()
