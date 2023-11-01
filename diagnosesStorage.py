import diagnosis


class DiagnosesStorage:
    def __init__(self):
        self.Diagnoses = [
            diagnosis("Кретин"),
            diagnosis("Идиот"),
            diagnosis("Дурак"),
            diagnosis("Нормальный"),
            diagnosis("Талант"),
            diagnosis("Гений")
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
        return result
