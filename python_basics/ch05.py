# class Result10:
#     def __init__(self,name,phone, email, pass_year10):
#         self.name = name
#         self.phone = phone
#         self.email = email
#         self.pass_year10 = pass_year10


#     def display(self):
#           print(f"{self.name} {self.phone} {self.email} {self.pass_year10}")

# class Result12(Result10):
#     def __init__(self,name,phone, email, pass_year10,pass_year12, percentage12):
#               super().__init__(name,phone, email, pass_year10)
#               self.pass_year12 = pass_year12
#               self.percentage12 = percentage12

#     def display(self):
#         super().display()
#         print(f"{self.pass_year12}, {self.percentage12}")

# class ResultBE(Result12):
#     def __init__(self,name,phone, email, pass_year10,pass_year12, percentage12,branch , university, bepercentage):
#         super().__init__(name,phone, email, pass_year10,pass_year12, percentage12)
#         self.branch = branch
#         self.university = university
#         self.bepercentage = bepercentage

#     def display(self):
#         super().display()
#         print(f"{self.branch}, {self.university}, {self.bepercentage}")



# s1 = Result10("aman",2324234234,"aman@gmail.com", 2019)
# s2 = Result12("mohit", 98657863,"mohit@gmail.com", 2019, 2021, 89)

# b3 = ResultBE("Rohit", 98657863,"rohit@gmail.com", 2019, 2021, 79, "abc", "xyz", 89)


# s1.display()
# s2.display()
# b3.display()


# class A:
#     a = 10
#     b = 20

#     def __init__(self,c,d):
#         self.c = c
#         self.d = d


# class B(A):
#     a = 1000
#     @classmethod
#     def display(cls):
#         print(f"{cls.a}")

# class C(A):
#     a = 2000

# obj1 = B(30,40)
# obj2 = C(50,60)
# print(obj1.a)
# print(obj1.b)
# print(obj1.c)
# print(obj1.d)
# print(obj2.a)
# print(obj2.b)
# print(obj2.c)
# print(obj2.d)


#q1

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_person_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")

# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id

#     def display_student_info(self):
#         self.display_person_info()
#         print(f"Student ID: {self.student_id}")

# class Teacher(Person):
#     def __init__(self, name, age, employee_id, subject):
#         super().__init__(name, age)
#         self.employee_id = employee_id
#         self.subject_expert = subject

#     def display_teacher_info(self):
#         self.display_person_info()
#         print(f"Teacher ID: {self.employee_id}")
#         print(f"Subject: {self.subject}")

# class Academic:
#     def __init__(self, subject, marks):
#         self.subject = subject
#         self.marks = marks

#     def display_academic_info(self):
#         print(f"Academic Subject: {self.subject}")
#         print(f"Marks: {self.marks}")

# class Sports:
#     def __init__(self, sport_name, level):
#         self.sport_name = sport_name
#         self.level = level

#     def display_sports_info(self):
#         print(f"Sport: {self.sport_name}")
#         print(f"Level: {self.level}")


        

# class AllRounderStudent(Student, Academic, Sports):
  
#     def __init__(self, name, age, student_id, subject, marks, sport_name, level):
#         Student.__init__(self, name, age, student_id)
#         Academic.__init__(self, subject, marks)
#         Sports.__init__(self, sport_name, level)

#     def display_all_info(self):
        
#         self.display_student_info()
#         self.display_academic_info()
#         self.display_sports_info()
      


# ars = AllRounderStudent("Aman", 20, 136, "Mathematics", 95, "Cricket", "State")

# ars.display_all_info()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no


class Academic:
    def __init__(self, course=None, cgpa=None):
        self.course = course
        self.cgpa = cgpa


class Sports:
    def __init__(self, sport_name=None, level=None):
        self.sport_name = sport_name
        self.level = level


class AllRounderStudent(Student, Academic, Sports):
    def __init__(self, name, age, roll_no, is_academic=False, is_sports=False,
                 course=None, cgpa=None,
                 sport_name=None, level=None):

        super().__init__(name, age, roll_no)

        if is_academic:
            Academic.__init__(self, course, cgpa)

        if is_sports:
            Sports.__init__(self, sport_name, level)

        self.is_academic = is_academic
        self.is_sports = is_sports

    def display_profile(self):
        print("Student Profile : ")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)

        if self.is_academic:
            print("Course:", self.course)
            print("CGPA:", self.cgpa)

        if self.is_sports:
            print("Sport:", self.sport_name)
            print("Level:", self.level)

        if self.is_academic and self.is_sports:
            print("The student is an allrounder")


student1 = AllRounderStudent(
    name="Rahul",
    age=20,
    roll_no=101,
    is_academic=True,
    is_sports=True,
    course="B.Tech",
    cgpa=8.7,
    sport_name="Football",
    level="State"
)

student1.display_profile()




