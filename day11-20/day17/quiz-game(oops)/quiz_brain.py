class QuizBrain:
  def __init__(self,ques_list):
      self.ques_no=0
      self.ques_list=ques_list
      self.score=0

  def checkansw(self, userans, correctans):
      if userans.lower()==correctans.lower():
          print("You are right!")
          self.score+=1
      else:
          print("You are wrong!")
      print(f"The current answer is {correctans}")
      self.game_score()
  def game_score(self):
      print(f"Your current score is {self.score}/{self.ques_no}")
      print("\n")

  def nextques(self):
      currentques=self.ques_list[self.ques_no]
      self.ques_no+=1
      userans=input(f"Q.no:{self.ques_no}. {currentques.text} :(True/false)? ").capitalize()
      correctans=currentques.answer
      self.checkansw(userans,correctans)


  def quesrem(self):
      return len(self.ques_list)>self.ques_no


