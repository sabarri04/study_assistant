"""Functions for managing study-session history.

The functions in this file are intentionally incomplete. Complete the TODOs
during the appropriate assignment milestones.
"""

from __future__ import annotations
import json
from pathlib import Path
from typing import Any


def load_history(history_file: str) -> list[dict[str, Any]]:
    """Return all saved study sessions."""

    path = Path(history_file)

    if not path.exists():
        return []

    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("History file contains invalid JSON.")
        return []

    except Exception as error:
        print(f"Unable to load history: {error}")
        return []


def save_session(history_file: str, session: dict[str, Any]) -> None:
    """Append a study session to the history file."""

    history = load_history(history_file)
    history.append(session)

    with open(history_file, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)


def display_history(history: list[dict[str, Any]]) -> None:
    """Print saved sessions."""

    if not history:
        print("No study sessions found.")
        return

    print("\nStudy History")

    for i, session in enumerate(history, start=1):
        print(f"\nSession {i}")
        print(f"Date      : {session['timestamp']}")
        print(f"Topic     : {session['topic']}")
        print(f"Question  : {session['question']}")
        print(f"Notes     : {session['notes']}")


def search_history(
    history: list[dict[str, Any]],
    keyword: str,
) -> list[dict[str, Any]]:
    """Return sessions matching a keyword."""

    keyword = keyword.strip().lower()

    if not keyword:
        return history

    results = []

    for session in history:
        topic = str(session.get("topic", "")).lower()
        question = str(session.get("question", "")).lower()
        notes = str(session.get("notes", "")).lower()

        if (
            keyword in topic
            or keyword in question
            or keyword in notes
        ):
            results.append(session)

    return results


def export_session(
    session: dict[str, Any],
    export_directory: str,
) -> Path | None:
    """Export one selected study session as a Markdown file."""

    try:
        export_path = Path(export_directory)
        export_path.mkdir(parents=True, exist_ok=True)

        timestamp = str(session.get("timestamp", "session"))
        safe_timestamp = (
            timestamp.replace(":", "-")
            .replace("T", "_")
        )

        file_path = export_path / f"study_session_{safe_timestamp}.md"

        content = (
            "# Study Session\n\n"
            f"**Timestamp:** {session.get('timestamp', '')}\n\n"
            f"**Topic:** {session.get('topic', '')}\n\n"
            f"## Question\n\n"
            f"{session.get('question', '')}\n\n"
            f"## Notes\n\n"
            f"{session.get('notes', '')}\n"
        )

        file_path.write_text(content, encoding="utf-8")

        return file_path

    except OSError as error:
        print(f"Error exporting session: {error}")
        return None
