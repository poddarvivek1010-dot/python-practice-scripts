#  Student score project 


class StudentScore:
    # storing student's name & exam marks
    def __init__(self, name, subject, marks, grade):
        self.name = name
        self.subject = subject
        self.marks = marks
        self.grade = grade

    # function to display the student's report
    def show_report(self):
        print(f"Student Name: {self.name}")
        print(f"Subject: {self.subject}")
        print(f"Marks Scored: {self.marks} / 100")
        print(f"Grade: {self.grade}")


# creating unique objects 

student_1 = StudentScore("Alex", "Mathematics", 81, "B+" )
student_2 = StudentScore("Priya", "Physics", 92, "A" )
student_3 = StudentScore("Abhinash", "English", 73, "B")
student_4 = StudentScore("Saniya", "Computer Application", 61, "C")


# running the class functions
print("Class Exam Results...")
student_1.show_report()

print()  # for clean spacing

student_2.show_report()

print()

student_3.show_report()

print()

student_4.show_report()
