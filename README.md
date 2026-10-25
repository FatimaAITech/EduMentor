# EduMentor — Smart Learning Agent

EduMentor is a Python-based learning assistant designed to help students learn Python, practice quizzes, prepare for technical interviews, and track their learning progress.

## Features

- **Python Learning Agent:** Helps users explore Python topics and find relevant learning information.
- **Quiz Agent:** Provides multiple-choice quizzes and calculates scores.
- **Interview Preparation:** Offers Python interview questions and checks answers.
- **Progress Tracker:** Records quiz and interview results and displays learning progress.
- **Weak Topic Analysis:** Identifies topics that may need more practice.
- **JSON Data Storage:** Stores questions and learning history in JSON files.

## Technologies Used

- Python
- JSON
- Object-oriented programming
- File handling
- Git and GitHub

## Project Structure

```text
EduMentor/
├── agents/
│   ├── learning_agent.py
│   ├── quiz_agent.py
│   ├── interview_agent.py
│   └── progress_tracker.py
├── data/
│   ├── questions.json
│   ├── quiz_questions.json
│   └── interview_questions.json
├── utils/
│   └── file_handler.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd EduMentor
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python main.py
```

## How to Use

1. Run the application.
2. Select an option from the main menu.
3. Ask a Python learning question, take a quiz, or practice interview questions.
4. Open the progress tracker to review your results.

## Data and Privacy

EduMentor uses JSON files for question banks and learning history. Personal student data and local progress history should not be committed to the public repository.

## Future Improvements

- Automated unit tests
- More Python quiz questions
- Improved topic-wise analytics
- Better input validation and error handling
- A graphical user interface

## Author

Created as a Python learning and portfolio project.