from random import random


class User:
    def __init__(self, name):
        self.name = name
        self.rightAnswersCount = 0


class Diagnosis:
    def __init__(self, grade):
        self.grade = grade

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

class DiagnosesStorage:
    def __init__(self):
        self.Diagnoses = [
            Diagnosis("Кретин"),
            Diagnosis("Идиот"),
            Diagnosis("Дурак"),
            Diagnosis("Нормальный"),
            Diagnosis("Талант"),
            Diagnosis("Гений")
        ]
    def CalculateDiagnose(self, questionsCount, rightAnswersCount):
        rightAnswersPercentage = rightAnswersCount * 100 / questionsCount
        result = self.Diagnoses[0]
        match rightAnswersPercentage:
            case item if item > 0 and item <= 20:
                result = self.Diagnoses[1]
            case item if item > 20 and item <= 40:
                result = self.Diagnoses[2]
            case item if item > 40 and item <= 60:
                result = self.Diagnoses[3]
            case item if item > 60 and item <= 80:
                result = self.Diagnoses[4]
            case item if item > 80:
                result = self.Diagnoses[5]
        return  result;


class QuestionStorage:
    questions =[]
    questionsCount = questions.count()

    def __init__(self, questions):
        self.questions = questions

    def AddQuestion(self, question):
        self.questions.Append(question)

    def RemoveQuestion(self, id):
        del self.questions[id-1]

    def Shuffle(self, questions):
        result = questions[:]
        list_length = len(result)
        for i in range(list_length):
            index_aleatory = random.randint(0, list_length - 1)
            temp = result[i]
            result[i] = result[index_aleatory]
            result[index_aleatory] = temp
        # Возвращаем список
        return result




