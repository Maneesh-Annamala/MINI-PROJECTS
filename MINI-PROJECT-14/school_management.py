class School:
    def __init__(self,name):
        self.name = name
        self.teachers = []
        
        self.classrooms = []

    def find_teacher(self,teacher_id):
        for teacher in self.teachers:
            if teacher.teacher_id == teacher_id:
                return teacher
        return None
    
    def find_student(self,student_id):
        for cls in self.classrooms:
            student = cls.find_student(student_id)
            if student:
                return student
        return None
    
    def add_classroom_and_teacher(self,classroom):
        teacher = self.find_teacher(classroom.teacher.teacher_id)
        if not teacher:
            return False
        for class_r in self.classrooms:
            if class_r.class_name == classroom.class_name or class_r.teacher.teacher_id == classroom.teacher.teacher_id:
                return False
        self.classrooms.append(classroom)
        return True

    def add_teacher(self,teacher):
        found = self.find_teacher(teacher.teacher_id)
        if found:
            return False
        self.teachers.append(teacher)
        return True
    
    def add_student(self,student,classroom_name):
        for std in self.classrooms:
            if std.class_name == classroom_name:
                for s in std.students:
                    if s.student_id == student.student_id:
                        return False
                std.students.append(student)
                return True
      
    def transfer_student(self,student_id,old_classroom_name,new_classroom_name):
        for std in self.classrooms:
            if std.class_name == old_classroom_name:
                for s in std.students:
                    if s.student_id == student_id:
                        for new in self.classrooms:
                            if new.class_name == new_classroom_name:
                                for n in new.students:
                                    if n.student_id == student_id:
                                        return False
                                std.students.remove(s)
                                new.students.append(s)
                                return True
        return False

    def show_school(self):
        print(f"School Name: {self.name}\n")
        if not self.classrooms:
            print("Right now School is not structered")
        else:
            for s in self.classrooms:
                print(f"Class Teacher of {s.class_name}:{s.teacher.teacher_name}\n")
                for index,std in enumerate(s.students ,start=1):
                    print(f"{index} | {std.student_id} | {std.student_name}")

    def show_classroom(self,class_name):
        
        found = False
        for cls in self.classrooms:
            if cls.class_name == class_name:
                found = True
                for index,s in enumerate(cls.students,start=1):
                    print(f"{index} | {s.student_id} | {s.student_name}")
        if not found:
            print("There is no class with that name")           

class Classroom:
    def __init__(self,class_name,teacher):
        self.class_name = class_name
        self.teacher = teacher
        self.students = []

    def find_student(self,student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return False

class Student:
    def __init__(self,student_name,student_id):
        self.student_name = student_name
        self.student_id = student_id

class Teacher:
    def __init__(self,teacher_name,teacher_id):
        self.teacher_name = teacher_name
        self.teacher_id = teacher_id

school = School("Chandra E.M School")

while True:
    print("1.add student\n2.add teacher\n3.add classroom and assign teacher\n4.Transfer student\n5.find teacher\n6.find student" \
    "\n7.Show School Data\n8.Show classroom\n9.Exit")
    try:
        choose = int(input("Choose (1-10): "))
    except ValueError:
        print("Enter only numbers")
        continue
    if choose == 1:
        student_id = int(input("Enter id of the student: "))
        student_name = input("Enter the name of the student: ").title()
        student = Student(student_id=student_id,student_name=student_name)
        class_name = input("Enter the class name: ").upper()
        if school.add_student(student,class_name):
            print("Student is added successfully!")
        else:
            print("Something went wrong!")

    elif choose == 2:
        teacher_name = input("Enter the name of the teacher: ")
        try:
            teacher_id = int(input("Enter the id of the teacher: "))
        except ValueError:
            print("Id must be in integers")
            continue
        teacher = Teacher(teacher_name,teacher_id)
        if school.add_teacher(teacher):
            print("Teacher is added successfully")
        else:
            print("We already have the teacher with that name")
    
    elif choose == 3:
        class_name = input("Enter the name of the class: ").title()
        teacher_name = input("Enter the name of the teacher: ").title()
        try:
            teacher_id = int(input("Enter the id of the teacher: "))
        except ValueError:
            print("ID must be in integers")
            continue
        teacher = Teacher(teacher_id=teacher_id,teacher_name=teacher_name)
        classroom = Classroom(class_name,teacher=teacher)
        if school.add_classroom_and_teacher(classroom):
            print("Classroom is added and teacher is assigned successfully!")
        else:
            print("Something went wrong!")
        
    elif choose == 4:
        try:
            student_id = int(input("Enter the id of the student: "))
        except ValueError:
            print("ID must be in integers")
            continue
        old_class = input("Enter the name of the old class: ").upper()
        new_class = input("Enter the name of the new class: ").upper()
        if school.transfer_student(student_id=student_id,old_classroom_name=old_class,new_classroom_name=new_class):
            print(f"Student transfered successfully from {old_class} to {new_class}")
        else:
            print("Something went wrong!")
    
    elif choose == 5:
        try:
            teacher_id = int(input("Enter the id: "))
        except ValueError:
            print("ID must be in integers")
            continue
        teach = school.find_teacher(teacher_id)
        if teach:
            print(f"The name of the teacher with {teacher_id} is {teach.teacher_name}")
        else:
            print("We don't have teacher with that ID")

    elif choose == 6:
        try:
            student_id = int(input("Enter the id: "))
        except ValueError:
            print("ID must be in integers")
            continue
        std = school.find_student(student_id)
        if std:
            print(f"The name of the student with {student_id} is {std.student_name}")
        else:
            print("There is no student with that ID")

    elif choose == 7:
        school.show_school()
    elif choose == 8:
        class_name = input("Enter the name of the class: ").upper()
        school.show_classroom(class_name)

    elif choose == 9:
        print("Exiting...")
        break

    else:
        print("Choose only between thoose numbers only")

