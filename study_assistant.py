"""Main entry point for the AI Study Assistant.

Complete the TODOs gradually and create logical Git commits as the project
moves from Version 1 to Version 2.
"""

from __future__ import annotations

import json
from datetime import datetime
from typing import Any

from history import (
    display_history,
    export_session,
    load_history,
    save_session,
    search_history,
)
from prompts import APP_TITLE, format_study_prompt


# Version 1 begins with direct file-path values.
# Milestone 3 requires these values to be read from config.py.
QUESTIONS_FILE = "sample_questions.json"
HISTORY_FILE = "history.json"


def load_questions(question_file: str) -> list[dict[str, Any]]:
    """Load study questions from a JSON file.

    Milestone 2:
    Read and return the list stored in sample_questions.json.

    Milestone 4:
    Handle missing files and invalid JSON gracefully.
    """
    # TODO: Implement this function.
    return []


def select_question(
    questions: list[dict[str, Any]],
) -> dict[str, Any] | None:
    """Display available questions and return the user's selection."""
    # TODO:
    # - Display numbered questions.
    # - Ask the user to select one.
    # - Validate the input.
    return None


def complete_study_session(
    selected_question: dict[str, Any],
) -> dict[str, Any]:
    """Conduct one session and return the session record."""
    topic = str(selected_question.get("topic", "Unknown Topic"))
    question = str(selected_question.get("question", ""))

    print("\n" + format_study_prompt(topic, question))
    notes = input("\nYour explanation or reflection: ").strip()

    return {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "topic": topic,
        "question": question,
        "notes": notes,
    }


def start_study_session() -> None:
    """Run and save one study session."""
    questions = load_questions(QUESTIONS_FILE)
    if not questions:
        return

    selected_question = select_question(questions)
    if selected_question is None:
        return

    session = complete_study_session(selected_question)
    save_session(HISTORY_FILE, session)
    print("\nStudy session saved.")


def show_recent_activity(history: list[dict[str, Any]]) -> None:
    """Display the three most recent sessions when the application starts.

    Milestone 3:
    Replace the fixed value with RECENT_ACTIVITY_LIMIT from config.py.
    """
    # TODO: Implement the Recent Activity enhancement.
    pass


def run_search() -> None:
    """Search previously saved sessions."""
    history = load_history(HISTORY_FILE)
    keyword = input("Enter a keyword: ").strip()
    results = search_history(history, keyword)
    display_history(results)


def run_export() -> None:
    """Allow the user to select and export one saved session."""
    history = load_history(HISTORY_FILE)

    if not history:
        print("No study sessions are available to export.")
        return

    display_history(history)

    # TODO (Milestone 3):
    # - Ask the user to select a session.
    # - Validate the selection.
    # - Export it using export_session().
    # - Display the output path.


def display_menu() -> None:
    """Print the main application menu."""
    print(f"\n{APP_TITLE}")
    print("1. Start a study session")
    print("2. View study history")
    print("3. Search study history")
    print("4. Export a study session")
    print("5. Exit")


def main() -> None:
    """Run the menu-driven application."""
    # TODO (Milestone 3):
    # Load the history and show Recent Activity when the program starts.

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            start_study_session()
        elif choice == "2":
            display_history(load_history(HISTORY_FILE))
        elif choice == "3":
            run_search()
        elif choice == "4":
            run_export()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Please enter a valid option.")


if __name__ == "__main__":
    main()
