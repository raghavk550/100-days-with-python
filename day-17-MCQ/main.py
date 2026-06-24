# class User:
#     # Constructor - It has two _ both sides so that interpreter knows that it's special function
#     def __init__(self, user_id, name):
#         self.id = user_id
#         self.name = name
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1

# user1 = User()
# # One way of adding attributes but it too hard to manage and can change in case of other object
# user1.name = "RK"
# user1.id = 1
#
# user2 = User()
# # Like here
# user2.user_name = "NK"
# user2.id = 2

# user1 = User(1, "RK")
# user2 = User(2, "NK")
#
# print(user1.followers)
# print(user2.followers)
# print(user1.following)
# print(user2.following)
#
# user2.follow(user1)
#
# print(user1.followers)
# print(user2.followers)
# print(user1.following)
# print(user2.following)

import question_model as qm, data, quiz_brain
question_bank = []
for qData in data.question_data:
    ques = qm.Question(qData["text"], qData["answer"])
    question_bank.append(ques)

quiz_brain = quiz_brain.QuizBrain(question_bank)
quiz_brain.next_question()

