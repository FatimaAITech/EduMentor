
import json
import random
from pathlib import Path


class QuizAgent:
    def __init__(self):
        base_path = Path(__file__).resolve().parent.parent

        self.questions_file = (
            base_path / "data" / "quiz_questions.json"
        )
        self.progress_file = (
            base_path / "data" / "progress.json"
        )

    def load_questions(self):
        try:
            with self.questions_file.open(
                "r", encoding="utf-8"
            ) as file:
                questions = json.load(file)

            if not isinstance(questions, list):
                print("Quiz data must be a list.")
                return []

            return questions

        except (FileNotFoundError, json.JSONDecodeError):
            print("Quiz questions file is missing or invalid.")
            return []

    
    def run_quiz(self):
        questions = self.load_questions()

        if not questions:
            print("No quiz questions available.")
            return

        import random
        random.shuffle(questions)

        score = 0
        total = len(questions)
        question_results = []

        print("\n===== EDUMENTOR QUIZ =====")
        print("Answer each question using A, B, C or D.")

        for number, item in enumerate(questions, start=1):
            print(f"\nQuestion {number}/{total}")
            print("Topic:", item["topic"])
            print(item["question"])

            for option, text in item["options"].items():
                print(f"{option}. {text}")

            user_answer = input("Your answer: ").strip().upper()
            correct_answer = item["answer"].upper()

            is_correct = user_answer == correct_answer

            if is_correct:
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
                print("Correct answer:", item["options"][correct_answer])

            question_results.append({
                "topic": item["topic"],
                "question": item["question"],
                "correct": is_correct
            })

        percentage = score / total * 100

        print("\n===== QUIZ RESULT =====")
        print(f"Score: {score}/{total}")
        print(f"Percentage: {percentage:.1f}%")

        self.save_result(score, total, percentage)

        self.save_question_results(question_results)

    def save_question_results(self, question_results):
        try:
            if self.progress_file.exists():
                with self.progress_file.open(
                    "r", encoding="utf-8"
                ) as file:
                    history = json.load(file)

                if not isinstance(history, list):
                    history = []
            else:
                history = []

        except (json.JSONDecodeError, OSError):
            history = []

        history.append({
            "activity": "Quiz Question Details",
            "questions": question_results
        })

        try:
            with self.progress_file.open(
                "w", encoding="utf-8"
            ) as file:
                json.dump(history, file, indent=4)

            print("Question-level results saved successfully!")

        except OSError:
            print("Warning: Could not save question-level results.")


        # self.save_result(score, total, percentage)

    
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
            "activity": "Python Quiz",
            "quiz": "Python Quiz",
            "score": score,
            "total": total,
            "percentage": round(percentage, 1)
        })

        try:
            with self.progress_file.open(
                "w", encoding="utf-8"
            ) as file:
                json.dump(results, file, indent=4)

            print("Quiz result saved successfully!")

        except OSError:
            print("Warning: Could not save quiz result.")
