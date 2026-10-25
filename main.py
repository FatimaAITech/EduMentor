from agents.interview_agent import InterviewAgent
from agents.learning_agent import LearningAgent
from agents.quiz_agent import QuizAgent
from agents.progress_tracker import ProgressTracker

def main():
    learning_agent = LearningAgent()
    quiz_agent = QuizAgent()
    interview_agent = InterviewAgent()
    progress_tracker = ProgressTracker()

    print("=" * 35)
    print("       EDUMENTOR")
    print("    Smart Learning Agent")
    print("=" * 35)

    while True:
        print("1. Ask a Python question")
        print("2. Take a Python quiz")
        print("3. Interview preparation")
        print("4. Student progress tracker")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            question = input(
                "Enter a topic or question: "
            ).strip()

            if question:
                learning_agent.answer_question(question)
            else:
                print("Please enter a question.")

        elif choice == "2":
            quiz_agent.run_quiz()

        elif choice == "3":
             interview_agent.start_interview()
             
        elif choice == "4":
             progress_tracker.show_progress()
             
        elif choice == "5":
             print("Keep learning! Goodbye.")     
             break     

        else:
            print("Invalid choice. Please select 1, 2 , 3 or 4.")


if __name__ == "__main__":
    main()
