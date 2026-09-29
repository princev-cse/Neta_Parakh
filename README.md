# Neta Parakh

### Know the Work. Compare the Performance. Make Your Choice.

## 1. About the Project

Neta Parakh is a Python-based village development and leader performance information system.

The main purpose of this project is to maintain a record of development works carried out in a village. People can view what works have been completed, which leader is associated with the work, and other details related to the work.

The public can also provide ratings and feedback on recorded works. During election time, people can view and compare the available information and public feedback about different leaders.

The system provides information in an organized way so that people can make their own decision based on the available records.

---

## 2. Problem Statement

In villages, people may not have all the information about development works carried out over the previous years in one place.

It can be difficult to remember which works were completed, which leader was associated with them, and how people felt about those works.

Neta Parakh provides a simple system to store development work records and public feedback in one place. This information can be viewed and compared during the election period.

---

## 3. Objectives

- To maintain records of village development works.
- To provide information about different leaders and their associated works.
- To collect public ratings and feedback on recorded works.
- To store feedback for future reference.
- To calculate total points and average ratings from recorded feedback.
- To provide a simple comparison of recorded information about leaders.
- To help people access organized information before making their own decision.

---

## 4. Main Modules

### Public Module

The public user can:

- View leaders
- View development works
- Give ratings and feedback
- Compare leaders
- Return to the main menu

### Leader Module

The leader can:

- View profile
- View their development works
- Logout

### Admin Module

The admin can:

- View all development works
- View public feedback
- Logout

---

## 5. Technologies Used

- Python
- Functions
- Lists
- Dictionaries
- File Handling
- Modular Programming
- `ast.literal_eval()` for reading stored feedback data

---

## 6. Data Storage

The project uses a text file to store public feedback.

### feedback.txt

Feedback is stored in dictionary format.

Example:

{'work_id': 1, 'leader': 'Rahul Kumar', 'rating': 8, 'feedback': 'Good work'}

The stored feedback is loaded when the program starts so that previous feedback can also be used during leader comparison.

---

## 7. How the System Works

1. The program starts from the main menu.
2. The user selects Public, Leader, Admin, or Exit.
3. Public users can view leaders and development works.
4. Public users can give ratings and feedback for a work.
5. Feedback is stored in `feedback.txt`.
6. The Admin can view the stored works and feedback.
7. The Comparison module calculates total points and average ratings from recorded feedback.
8. The comparison results are displayed for the available leaders.

---

## 8. Project Structure

NetaParakh/
│
├── main.py
├── leader.py
├── works.py
├── feedback.py
├── comparison.py
├── file_handler.py
├── feedback.txt
├── README.md
└── statement.md

---

## 9. Description of Files

### main.py

Contains the main menu and connects the different modules of the project.

### leader.py

Contains leader information and functions for viewing leader profiles.

### works.py

Contains development work records and functions for viewing works.

### feedback.py

Handles public ratings and feedback.

### comparison.py

Calculates total points, average ratings, and rated works for comparison.

### file_handler.py

Handles saving and loading feedback data from the text file.

### feedback.txt

Stores the feedback submitted by public users.

---

## 10. How to Run

### Step 1

Install Python on the computer.

### Step 2

Open the `NetaParakh` project folder in VS Code.

### Step 3

Open the terminal in VS Code.

### Step 4

Run the following command:

python main.py

### Step 5

Select the required option from the main menu.

---

## 11. Testing

The following features were tested:

- Main menu navigation
- Public module
- Leader profile viewing
- Viewing development works
- Giving ratings and feedback
- Saving feedback to file
- Loading previously saved feedback
- Admin feedback viewing
- Leader comparison
- Returning between menus

---

## 12. Non-Functional Requirements

### Usability

The system uses simple menus and options so that users can easily navigate through the application.

### Reliability

Feedback is stored in a file so that previously submitted feedback can be loaded again when the program is restarted.

### Maintainability

The project is divided into multiple Python files and modules, making the code easier to understand and modify.

### Performance

The system uses simple Python data structures and file handling, allowing the operations to be performed quickly for the intended project scale.

---

## 13. Future Scope

The project can be improved in the future by adding:

- Graphical User Interface (GUI)
- Database storage
- User authentication
- More detailed development work records
- Search and filtering
- Online access
- Data visualization and reports

---

## 14. Conclusion

Neta Parakh demonstrates how Python can be used to create a simple village development and public feedback management system.

The project maintains development work records, collects public feedback, stores the information using file handling, and provides a comparison based on recorded ratings.

The system is designed to provide organized information so that people can review the available records and make their own decision.
