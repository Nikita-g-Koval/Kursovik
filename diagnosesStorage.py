from diagnosis import Diagnosis


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
        
    def calculate_diagnose(self, questions_count, right_answers_count):
        right_answers_percentage = right_answers_count * 100 / questions_count
        result = self.Diagnoses[0]
        match right_answers_percentage:
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
