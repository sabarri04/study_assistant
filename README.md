# AI Study Assistant

**Student Name:** SABARRINATH S  
**Roll Number:** AM.SC.P2CSN26017  

## Project Overview

## Project Overview

The AI Study Assistant is a Python-based console application that helps users practise study topics through guided question-and-answer sessions. It allows users to select questions, record their own explanations, save study history, search previous sessions, and export selected sessions as Markdown files.

## Implemented Features

- Load study questions from a JSON file
- Menu-driven interface
- Complete guided study sessions
- Save study history to history.json
- Display previous study sessions
- Search study history using keywords
- Export study sessions as Markdown
- Display recent study activity
- Read configuration values from config.py

## Project Structure

```text
study_assistant/
├── study_assistant.py
├── prompts.py
├── history.py
├── config.py
├── sample_questions.json
├── requirements.txt
├── README.md
└── .env.example
```

## Installation and Setup


1. Clone the repository.

2. Create a virtual environment.

Windows

python -m venv venv

venv\Scripts\activate

Linux/macOS

python3 -m venv venv

source venv/bin/activate

3. Install dependencies.

pip install -r requirements.txt

## Running the Application


Run the application using:

python study_assistant.py

## Generated Files

The following files are generated while the application is running:

- history.json
- exports/

These files are generated automatically and should not be committed to Git. They are excluded using .gitignore.

## Version Summary

### Version 1


- Load questions from JSON
- Complete study sessions
- Save study history
- Display study history
- Menu-driven interface

### Version 2


- Search study history
- Export study sessions as Markdown
- Display recent activity
- Read configuration values from config.py
- Improved repository organisation

## Notes

- Do not include real API keys, passwords or access tokens.
- Complete the milestones in order.
- Maintain a meaningful Git history throughout development.
