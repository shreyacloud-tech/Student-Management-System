# Student Management System

A Python-based command-line application for managing student records. The system allows users to add, view, search, update, and delete student information through a simple interactive menu.

## Features

* Add new student records
* View all student records
* Search for a student
* Update student information
* Delete student records
* Interactive command-line menu
* Input validation
* Simple and easy-to-use interface

## Technologies Used

* Python

## Project Structure

```text
Student-Management-System/
│
├── main.py
└── README.md
```

## How the Project Works

The application uses a menu-driven approach.

When the program starts, the user can select an operation:

```text
===== STUDENT MANAGEMENT SYSTEM =====

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
```

The selected operation is performed, and the menu is displayed again until the user chooses to exit.

## Menu Options

### 1. Add Student

Allows the user to enter student information and add a new student record.

Example:

```text
Enter Student ID: 101
Enter Student Name: Shreya
Enter Student Age: 23
Enter Student Course: Information Technology
```

### 2. View Students

Displays all student records currently stored in the application.

Example:

```text
===== STUDENT RECORDS =====

ID: 101
Name: Shreya
Age: 23
Course: Information Technology
```

### 3. Search Student

Allows the user to search for a student using their student ID.

Example:

```text
Enter Student ID to search: 101

Student Found
ID: 101
Name: Shreya
Age: 23
Course: Information Technology
```

### 4. Update Student

Allows the user to modify information belonging to an existing student.

### 5. Delete Student

Allows the user to remove a student record using the student ID.

### 6. Exit

Closes the application safely.

## Python Concepts Used

This project demonstrates the following Python concepts:

* Variables
* Data types
* Strings
* Integers
* Lists
* Dictionaries
* Functions
* Function parameters
* Return values
* `if`, `elif`, and `else`
* `for` loops
* `while` loops
* `break`
* User input using `input()`
* Type conversion
* Searching data
* Updating data
* Deleting data
* Menu-driven programs

## Example

```text
===== STUDENT MANAGEMENT SYSTEM =====

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit

Enter your choice: 1

Enter Student ID: 101
Enter Student Name: Shreya
Enter Student Age: 23
Enter Student Course: Information Technology

Student added successfully!
```

## Installation

### 1. Install Python

Make sure Python is installed on your computer.

Check the Python version:

```bash
python --version
```

### 2. Clone or Download the Project

Download or clone this repository to your computer.

### 3. Navigate to the Project Folder

```bash
cd Student-Management-System
```

## How to Run

Run the following command:

```bash
python main.py
```

The Student Management System menu will appear in the terminal.

## What I Learned

Through this project, I practiced building a complete command-line application using Python.

The project helped strengthen my understanding of functions, loops, conditional statements, lists, dictionaries, user input, searching, updating, and deleting data.

It also helped me understand how multiple Python concepts can be combined to create a functional application instead of writing isolated programs.

## Future Improvements

Possible improvements include:

* Store student records permanently using JSON or a database
* Add student marks and grades
* Calculate student averages
* Add login/authentication
* Add sorting and filtering
* Add CSV import/export
* Build a graphical user interface
* Connect the application to a database
* Deploy the application as a web application

## Author

Salla Shreya

## Project Status

Completed
---

## Docker

This application is containerized using Docker.

### Build the Docker Image

```bash
docker build -t student-management-system .
```

### Run the Docker Container

```bash
docker run -it student-management-system
```

The Docker container provides a consistent Python 3.12 environment for running the application.

---

## Continuous Integration

This project uses GitHub Actions for Continuous Integration (CI).

The GitHub Actions workflow automatically:

- Checks out the source code
- Sets up Python 3.12
- Checks Python syntax
- Builds the Docker image

The workflow file is located at:

```text
.github/workflows/ci.yml
```

Every push to the `main` branch triggers the CI workflow automatically.

---

## Technologies Used

- Python
- JSON
- Git
- GitHub
- Docker
- GitHub Actions

---

## Project Structure

```text
Student-Management-System/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── .gitignore
├── Dockerfile
├── main.py
├── README.md
├── requirements.txt
└── students.json
```

---

## How to Run the Project

### Run Locally

```bash
python main.py
```

### Run Using Docker

```bash
docker build -t student-management-system .
docker run -it student-management-system
```

---

## CI Status

GitHub Actions successfully checks the Python syntax and builds the Docker image whenever changes are pushed to the `main` branch.