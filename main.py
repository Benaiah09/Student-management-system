class Student:
    """Represents a student with an ID, name, age, and major."""
    def __init__(self, id, name, age, major):
        self.id = id
        self.name = name
        self.age = age
        self.major = major

    def update(self, name=None, age=None, major=None):
        """Update the student's information."""
        if name:
            self.name = name
        if age:
            self.age = age
        if major:
            self.major = major

    def __str__(self):
        """Return a string representation of the student."""
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Major: {self.major}"

class StudentRepository:
    """Manages the storage and retrieval of students."""
    def __init__(self):
        self.students = {}

    def add(self, student):
        """Add a student to the repository."""
        self.students[student.id] = student

    def remove(self, student_id):
        """Remove a student from the repository by ID."""
        self.students.pop(student_id, None)

    def get_all(self):
        """Retrieve all students from the repository."""
        return list(self.students.values())

class StudentManagementSystem:
    """Handles operations related to student management."""
    def __init__(self, repository):
        self.repository = repository

    def add_student(self, id, name, age, major):
        """Add a new student to the system."""
        student = Student(id, name, age, major)
        self.repository.add(student)

    def delete_student(self, student_id):
        """Delete a student from the system."""
        self.repository.remove(student_id)

    def update_student(self, student_id, name=None, age=None, major=None):
        """Update an existing student's information."""
        student = self.repository.students.get(student_id)
        if student:
            student.update(name, age, major)

    def show_all_students(self):
        """Display all students in the system."""
        for student in self.repository.get_all():
            print(student)

def menu():
    """Provides a text-based menu for user interaction with the student management system."""
    repository = StudentRepository()
    system = StudentManagementSystem(repository)

    while True:
        print("\n1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Show All Students")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            id = int(input("Enter ID: "))
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            major = input("Enter major: ")
            system.add_student(id, name, age, major)
        elif choice == '2':
            id = int(input("Enter ID of student to update: "))
            name = input("Enter new name (leave blank to keep current): ")
            age = input("Enter new age (leave blank to keep current): ")
            major = input("Enter new major (leave blank to keep current): ")
            system.update_student(id, name if name else None, int(age) if age else None, major if major else None)
        elif choice == '3':
            id = int(input("Enter ID of student to delete: "))
            system.delete_student(id)
        elif choice == '4':
            system.show_all_students()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    menu()
