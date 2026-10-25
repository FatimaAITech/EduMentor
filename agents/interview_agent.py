import random
import json
from pathlib import Path


class InterviewAgent:
    def __init__(self):
        base_path = Path(__file__).resolve().parent.parent

        self.questions_file = (
            base_path / "data" / "interview_questions.json"
        )
        self.progress_file = base_path / "data" / "progress.json"

    def load_questions(self):
        try:
            with self.questions_file.open(
                "r", encoding="utf-8"
            ) as file:
                questions = json.load(file)

            if not isinstance(questions, list):
                print("Interview questions must be a list.")
                return []

            return questions

        except (FileNotFoundError, json.JSONDecodeError):
            print("Interview questions file is missing or invalid.")
            return []

    def start_interview(self):
        questions = self.load_questions()

        if not questions:
            print("No interview questions available.")
            return

        print("\n===== INTERVIEW PREPARATION =====")
        print("1. Beginner")
        print("2. Intermediate")
        print("3. Advanced")
        print("4. Mixed difficulty")

        choice = input("Choose difficulty: ").strip()

        difficulty_map = {
            "1": "Beginner",
            "2": "Intermediate",
            "3": "Advanced"
        }

        if choice in difficulty_map:
            selected_level = difficulty_map[choice]
            questions = [
                q for q in questions
                if q.get("difficulty") == selected_level
            ]
        elif choice != "4":
            print("Invalid choice.")
            return

        if not questions:
            print("No questions found for this difficulty.")
            return

        try:
            count = int(input(
                f"How many questions? (1-{len(questions)}): "
            ))
        except ValueError:
            print("Please enter a valid number.")
            return

        if count < 1 or count > len(questions):
            print("Number is outside the available question range.")
            return

        random.shuffle(questions)

        score = 0
        asked_questions = questions[:count]

        for number, item in enumerate(asked_questions, start=1):
            print(f"\nQuestion {number}/{count}")
            print("Topic:", item["topic"])
            print("Difficulty:", item["difficulty"])
            print(item["question"])

            user_answer = input("Your answer: ").strip()

            if not user_answer:
                print("No answer entered.")
            else:
                print("\nSuggested answer:")
                print(item["answer"])

                keywords = item.get("keywords", [])
                answer_lower = user_answer.lower()

                matched = sum(
                    1 for keyword in keywords
                    if keyword.lower() in answer_lower
                )

                if keywords and matched == len(keywords):
                    print("\nGood! Your answer includes the key concepts.")
                    score += 1
                else:
                    print(
                        "\nReview the suggested answer "
                        "and compare the key concepts."
                    )

            print("-" * 35)

        total = len(asked_questions)
        percentage = score / total * 100

        print("\n===== INTERVIEW RESULT =====")
        print(f"Key-concept score: {score}/{total}")
        print(f"Percentage: {percentage:.1f}%")
        print("Note: This is a basic keyword score, not an AI evaluation.")

        self.save_result(score, total, percentage)

    def save_result(self, score, total, percentage):
        try:
            if self.progress_file.exists():
                with self.progress_file.open(
                    "r", encoding="utf-8"
                ) as file:
                    results = json.load(file)

                if not isinstance(results, list):
                    results = []
            else:
                results = []

        except (json.JSONDecodeError, OSError):
            results = []

        results.append({
            "activity": "Interview Practice",
            "score": score,
            "total": total,
            "percentage": round(percentage, 1)
        })

        try:
            with self.progress_file.open(
                "w", encoding="utf-8"
            ) as file:
                json.dump(results, file, indent=4)

            print("Interview progress saved successfully!")

        except OSError:
            print("Warning: Could not save interview progress.")
