class Student:
    """Represents a student management system."""

    # Stores all student objects
    students = []

    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    @classmethod
    def add_students(cls,name,roll_no,marks):
        """Create and add a new student."""
        student = Student(name,roll_no,marks)
        cls.students.append(student)

    @classmethod
    def display_all_students(cls):
        """Display all student records."""
        for student in cls.students:
            print(student.name,student.roll_no,student.marks)
            print()

    @classmethod
    def find_topper(cls):
        """Find and display the topper student."""
        topper = cls.students[0]

        for student in cls.students:
            if student.marks > topper.marks:
                topper = student

        print("--Topper Details--")
        print("Topper name:",topper.name)
        print("Roll no:",topper.roll_no)
        print("Marks:",topper.marks)

    @classmethod
    def average_marks(cls):
        """Calculate and display average marks."""
        total = 0

        for student in cls.students:
            total += student.marks

        average = total/len(cls.students)

        print(f"Average marks:{average}")

    @classmethod
    def search_by_rollno(cls,rollno):
        """Search a student using roll number."""
        found = False

        for student in cls.students:
            if student.roll_no == rollno:
                found = True
                print(f"That rollno belongs to {student.name}")
                break

        if not found:
            print("We don't have student with that roll no")


# Default student records
Student.students = [
    Student("Maneesh",101,85),
    Student("Rahul",102,90),
    Student("Kiran",103,80)
]

while True:

    # Display menu options
    print("1.Add student\n2.Display all students\n3.Show Topper\n4.Show avg marks\n5.Search by rollno\n6.Exit")

    choose = int(input("Choose what you want: "))

    # Add a new student
    if choose == 1:
        name = input("Enter name of the student: ")
        roll_no = int(input("Enter roll no of student: "))
        marks = int(input("Enter the marks: "))

        Student.add_students(name=name,roll_no=roll_no,marks=marks)

        print("Added successfully!")

    # Display all students
    elif choose == 2:
        Student.display_all_students()

    # Show topper details
    elif choose == 3:
        Student.find_topper()

    # Show average marks
    elif choose == 4:
        Student.average_marks()

    # Search student by roll number
    elif choose == 5:
        input_rollno = int(input("Enter the roll no: "))
        Student.search_by_rollno(input_rollno)

    # Exit program
    elif choose == 6:
        print("Exiting...")
        break

    else:
        print("Please choose between the available options!")