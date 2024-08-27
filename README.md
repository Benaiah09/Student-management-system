# Student-management-system
Assignment 2 (BSE 2210)

# Student Management System

Welcome to the Student Management System! This repository provides a simple command-line application for managing student information. 

## Overview

This application allows users to:

- **Add** new students
- **Update** existing student information
- **Delete** students
- **View** all students

The application is built with three main classes:

1. **`Student`**: Represents individual students.
2. **`StudentRepository`**: Manages the storage and retrieval of student objects.
3. **`StudentManagementSystem`**: Handles operations related to student management and provides an interface for user interaction.

## Functionality

### Classes

1. **`Student`**
    - **Attributes**:
        - `id` (int): Unique identifier for the student.
        - `name` (str): Name of the student.
        - `age` (int): Age of the student.
        - `major` (str): Major field of study.
    - **Methods**:
        - `update(name=None, age=None, major=None)`: Updates the student's information.
        - `__str__()`: Provides a string representation of the student's details.

2. **`StudentRepository`**
    - **Attributes**:
        - `students` (dict): A dictionary storing students by their ID.
    - **Methods**:
        - `add(student)`: Adds a student to the repository.
        - `remove(student_id)`: Removes a student from the repository by their ID.
        - `get_all()`: Retrieves a list of all students in the repository.

3. **`StudentManagementSystem`**
    - **Attributes**:
        - `repository` (StudentRepository): An instance of `StudentRepository` for data management.
    - **Methods**:
        - `add_student(id, name, age, major)`: Creates and adds a new student to the system.
        - `delete_student(student_id)`: Deletes a student from the system.
        - `update_student(student_id, name=None, age=None, major=None)`: Updates an existing student's information.
        - `show_all_students()`: Displays all students currently in the system.

## How to Use

1. **Run the Program**:
    - Execute the script using a Python interpreter.
    ```bash
    python student_management_system.py
    ```

2. **Interacting with the Menu**:
    - The program will present a text-based menu with the following options:
        - **Add Student**: Input the student ID, name, age, and major.
        - **Update Student**: Input the student ID and the details you want to update. Leave fields blank to keep the current values.
        - **Delete Student**: Input the student ID to remove them from the system.
        - **Show All Students**: Displays the list of all students currently in the system.
        - **Exit**: Exit the application.

3. **Example Usage**:
    - To add a student, select option `1` and enter the required details.
    - To update a student, select option `2`, enter the student's ID, and provide any new details.
    - To delete a student, select option `3` and enter the student's ID.
    - To view all students, select option `4`.

