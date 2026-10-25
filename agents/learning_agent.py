
import json
from pathlib import Path


class LearningAgent:
    def __init__(self):
        self.data_file = (
            Path(__file__).resolve().parent.parent
            / "data"
            / "questions.json"
        )
        self.questions = self.load_questions()

    def load_questions(self):
        try:
            with self.data_file.open("r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Questions file missing or invalid.")
            return []

    
    
    def answer_question(self, user_question):
        search_text = user_question.lower().strip()
        search_text = search_text.rstrip("?!., ")

        # First, check for an exact topic match
        for item in self.questions:
            if search_text == item["topic"].lower():
                self.show_answer(item)
                return

        # Next, check topic keywords
        for item in self.questions:
            keywords = item.get("keywords", [])

            if any(
                search_text == keyword.lower()
                for keyword in keywords
            ):
                self.show_answer(item)
                return

        # Finally, search inside questions and keywords
        search_words = set(search_text.split())

        best_match = None
        best_score = 0

        for item in self.questions:
            searchable_text = (
                item["topic"] + " "
                + item["question"] + " "
                + " ".join(item.get("keywords", []))
            ).lower()

            searchable_words = set(searchable_text.split())
            score = len(search_words & searchable_words)

            if score > best_score:
                best_score = score
                best_match = item

        if best_match and best_score >= 1:
            self.show_answer(best_match)
        else:
            print("\nSorry, I could not find a matching answer.")
            print("Try a Python topic such as Functions, Lists or OOP.")

    def show_answer(self, item):
        print("\nTopic:", item["topic"])
        print("Question:", item["question"])
        print("Answer:", item["answer"])
