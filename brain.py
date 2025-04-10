# brain_master.py

class Quize:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.current_question_index = 0

    def add_question(self, question, options, answer):
        self.questions.append({
            "question": question,
            "options": options,
            "answer": answer
        })

    def start_quiz(self):
        self.score = 0
        self.current_question_index = 0
        print("Quiz started!")

    def has_next_question(self):
        return self.current_question_index < len(self.questions)

    def get_next_question(self):
        if self.has_next_question():
            return self.questions[self.current_question_index]
        else:
            return None

    def check_answer(self, user_answer):
        current_q = self.questions[self.current_question_index]
        if user_answer == current_q["answer"]:
            self.score += 1
            result = True
        else:
            result = False
        self.current_question_index += 1
        return result

    def get_score(self):
        return self.score

    def get_total_questions(self):
        return len(self.questions)

    def show_result(self):
        print(f"Your final score is {self.score}/{len(self.questions)}")

    def reset_quiz(self):
        self.score = 0
        self.current_question_index = 0