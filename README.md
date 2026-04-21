Project Description

The Online Quiz System is a web-based application developed using Python and Flask. It allows users to take a quiz consisting of multiple-choice questions related to Python programming. The system automatically evaluates the answers and displays the final score. The results are also stored in a CSV file for future reference.

Features
Multiple-choice quiz with 15 Python-related questions
User name input
Timer functionality (auto submit after 60 seconds)
Automatic evaluation of answers
Score display after submission
Result storage using CSV file
Simple and user-friendly interface
Technologies Used
Python
Flask (Web Framework)
HTML
CSS
JavaScript (for timer)
Project Structure
quiz_project/
│── app.py
│── result.csv
└── templates/
    ├── index.html
    └── result.html
How to Run the Project
Install Flask:
pip install flask
Run the application:
python app.py
Open a web browser and go to:
http://127.0.0.1:5000/
How It Works
The user enters their name on the quiz page.
The system displays multiple-choice questions.
The user selects answers and submits the quiz.
A timer runs in the background and auto-submits when time ends.
The system evaluates the answers and calculates the score.
The result is displayed along with the user's name and score.
The result is stored in a CSV file.
Output
Quiz page displaying questions and options
Result page showing user name and score
Learning Outcome
Understanding of Flask framework
Handling form data in web applications
Implementation of frontend using HTML and CSS
Backend logic using Python
File handling using CSV
Author Abirami.P
