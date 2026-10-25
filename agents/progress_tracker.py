
import json
from pathlib import Path


class ProgressTracker:
    def __init__(self):
        base_path = Path(__file__).resolve().parent.parent
        self.progress_file = base_path / "data" / "progress.json"
        self.questions_file = base_path / "data" / "interview_questions.json"

    def load_history(self):
        if not self.progress_file.exists():
            return []

        try:
            with self.progress_file.open("r", encoding="utf-8") as file:
                history = json.load(file)

            if isinstance(history, list):
                return history

            return []

        except (json.JSONDecodeError, OSError):
            print("Could not read progress history.")
            return []

    def show_progress(self):
        history = self.load_history()

        print("\n===== STUDENT PROGRESS TRACKER =====")

        if not history:
            print("No saved progress found yet.")
            print("Take a quiz or interview practice first.")
            return

        total_attempts = len(history)
        percentages = [
            item["percentage"]
            for item in history
            if isinstance(item.get("percentage"), (int, float))
        ]

        print("Total saved attempts:", total_attempts)

        if percentages:
            average = sum(percentages) / len(percentages)
            print(f"Average performance: {average:.1f}%")
            print(f"Best result: {max(percentages):.1f}%")
            print(f"Lowest result: {min(percentages):.1f}%")

        print("\n===== ACTIVITY HISTORY =====")

        for number, item in enumerate(history, start=1):
            activity = item.get("activity", "Unknown activity")
            score = item.get("score", 0)
            total = item.get("total", 0)
            percentage = item.get("percentage", 0)

            print(
                f"{number}. {activity}: "
                f"{score}/{total} ({percentage}%)"
            )

        self.show_weak_topics()

    
    def show_weak_topics(self):
        history = self.load_history()
        topic_stats = {}

        for item in history:
            questions = item.get("questions", [])

            for question in questions:
                topic = question.get("topic")
                correct = question.get("correct")

                if not topic:
                    continue

                if topic not in topic_stats:
                    topic_stats[topic] = {
                        "correct": 0,
                        "total": 0
                    }

                topic_stats[topic]["total"] += 1

                if correct is True:
                    topic_stats[topic]["correct"] += 1

        print("\n===== TOPIC PERFORMANCE =====")

        if not topic_stats:
            print("No question-level history yet.")
            print("Complete a new quiz to track your topics.")
            return

        print("\nTopics to review (below 70%):")

        weak_found = False

        for topic, stats in sorted(topic_stats.items()):
            total = stats["total"]
            correct = stats["correct"]
            percentage = correct / total * 100

            print(
                f"{topic}: {correct}/{total} correct "
                f"({percentage:.1f}%)"
            )

            if percentage < 70:
                weak_found = True

        if not weak_found:
            print("No weak topics in recorded quiz attempts.")
