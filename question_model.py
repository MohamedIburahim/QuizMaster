class Question:
    def __init__(self,text,answer):
        self.text = text
        self.answer = answer
#instance creation
question = Question("2+3=5","True")
print(question.text)