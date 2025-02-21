class User:
    def __init__(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email

    def get_user_info(self):
        return f"{self.name}, username: {self.username}, email: {self.email}"

class Course:
    def __init__(self, course_name, start_date, domain, number_of_classes):
        self.course_name = course_name
        self.start_date = start_date
        self.domain = domain
        self.number_of_classes = number_of_classes
        self.instructor = None
        self.students = []
        self.homework = []

    def get_course_info(self):
        print(f"Course: {self.course_name}\n"
             f"Start Date: {self.start_date}\n"
             f"Domain: {self.domain}\n"
             f"Classes: {self.number_of_classes}\n"
             f"Instructor: {self.instructor.get_instructor_info()}")
        print("Students:")
        for student in self.students:
            print(student.get_student_info())
        print("Homework:")
        for hw in self.homework:
            print(hw.get_homework_info())

    def add_instructor(self, instructor):
        self.instructor = instructor

    def add_student(self, student):
        self.students.append(student)

    def add_homework(self, hw):
         self.homework.append(hw)

class Homework:
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def get_homework_info(self):
        return f"{self.title}, Description: {self.description}"

class Student(User):
    def __init__(self, name, username, email):
        super().__init__(name, username, email)
        self.enrolled_courses = []

    def enroll(self, course):
        self.enrolled_courses.append(course)
        course.add_student(self)

    def get_student_info(self):
        return f"{self.get_user_info()}, enrolled courses: {[course.course_name for course in self.enrolled_courses]}"

class Instructor(User):
    def __init__(self, name, username, email):
        super().__init__(name, username, email)
        self.course_taught = None

    def start_teaching(self, course):
        self.course_taught = course
        course.add_instructor(self)

    def create_homework(self, title, description):
        if self.course_taught:
            hw = Homework(title, description)
            self.course_taught.add_homework(hw)

    def get_instructor_info(self):
        course_name = self.course_taught.course_name if self.course_taught else "No course assigned"
        return f"{self.get_user_info()}, teaching: {course_name}"

# Example
front_end_pro = Course("Front-end Pro", "2023-09-21", "Management", 1)
data_analytics_pro = Course("Data Analytics Pro", "2024-12-20", "Management", 4)

instructor = Instructor("Volodymyr Ivasiuk", "v_ivasuik", "v_ivasiuk@gmail.com")
instructor.start_teaching(data_analytics_pro)

student1 = Student("Michael Gubariev", "m_gubariev", "michael@gmail.com")
student2 = Student("Anna Bilchenko", "a_bilchenko", "anna@gmail.com")
student3 = Student("Ilya Prodan", "i_prodan", "ilya@gmail.com")

student1.enroll(front_end_pro)
student1.enroll(data_analytics_pro)
student2.enroll(data_analytics_pro)
student3.enroll(data_analytics_pro)

instructor.create_homework("Основи Python", "На занятті обговорюється основи програмування мовою Python...")
instructor.create_homework("Python. Функції", "На занятті викладач пояснює основи функцій у Python...")
instructor.create_homework("Python. Класи", "На занятті з Python викладач розглядає основи об'єктно-орієнтованого програмування (ООП)...")

data_analytics_pro.get_course_info()
