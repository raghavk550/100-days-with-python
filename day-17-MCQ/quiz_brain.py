class QuizBrain:
    def __init__(self, questions):
        self.ques_num = 0
        self.ques_list = questions
        self.score = 0

    def still_has_questions(self):
        return self.ques_num < len(self.ques_list)

    def next_question(self):
        current_question = self.ques_list[self.ques_num]
        self.ques_num += 1
        user_choice = input(f"Q.{self.ques_num}: {current_question.question} (True/False): ").lower()
        if user_choice == current_question.answer.lower():
            self.score += 1
            print("You got it right!")
            print(f"The correct answer was: {current_question.answer}.")
            print(f"Your current score is: {self.score}/{len(self.ques_list)}")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {current_question.answer}.")
            print(f"Your current score is: {self.score}/{len(self.ques_list)}")

        print("\n")

        if self.still_has_questions():
            self.next_question()
        else:
            print("You've completed the quiz")
            print(f"Your final score was: {self.score}/{len(self.ques_list)}")

