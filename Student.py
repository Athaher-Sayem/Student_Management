class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)


class Student:
    def __init__(self, student_id, name, department):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = False
        StudentDatabase.add_student(self)

    def enroll_student(self):
        if self.__is_enrolled:
            print(f"Error: {self.__name} is already enrolled.")
        else:
            self.__is_enrolled = True
            print(f"Student enrolled successfully: ID: {self.__student_id}, Name: {self.__name}, Department: {self.__department}")

    def drop_student(self):
        if not self.__is_enrolled:
            print(f"Error: {self.__name} is not enrolled.")
        else:
            self.__is_enrolled = False
            print(f"Student dropped successfully: ID: {self.__student_id}, Name: {self.__name}, Department: {self.__department}")

    def view_student_info(self):
        status = "Enrolled" if self.__is_enrolled else "Not Enrolled"
        print(f"ID: {self.__student_id}, Name: {self.__name}, Department: {self.__department}, Status: {status}")

    def get_student_id(self):
        return self.__student_id


def menu():
    while True:
        print("\n--- Student Database Menu ---")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Enroll Student")
        print("4. Drop Student")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":  
            sid = input("Enter Student ID: ").strip()
            name = input("Enter Student Name: ").strip()
            dept = input("Enter Department: ").strip()
            Student(sid, name, dept)
            print(f"New student added: ID: {sid}, Name: {name}, Department: {dept}")

        elif choice == "2": 
            if not StudentDatabase.student_list:
                print("No students in database.")
            else:
                for student in StudentDatabase.student_list:
                    student.view_student_info()

        elif choice == "3": 
            sid = input("Enter Student ID to enroll: ").strip()
            student_found = False
            for student in StudentDatabase.student_list:
                if student.get_student_id() == sid:
                    student.enroll_student()
                    student_found = True
                    break
            if not student_found:
                print("Error: Invalid Student ID.")

        elif choice == "4": 
            sid = input("Enter Student ID to drop: ").strip()
            student_found = False
            for student in StudentDatabase.student_list:
                if student.get_student_id() == sid:
                    student.drop_student()
                    student_found = True
                    break
            if not student_found:
                print("Error: Invalid Student ID.")

        elif choice == "5": 
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")


s1 = Student("S101", "Athaher Sayem", "CSE")
s2 = Student("S102", "John Doe", "EEE")
s3 = Student("S103", "Jane Smith", "BBA")

menu()


