from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for ques in question_data:
    text=ques['question']
    answer=ques['correct_answer']
    new_q=Question(text,answer)
    question_bank.append(new_q)
quiz=QuizBrain(question_bank)
while(quiz.quesrem()):
 quiz.nextques()
print("Well done! You've completed the quiz ")
print(f"Your final score is {quiz.score}/{len(question_bank)}")
{}

