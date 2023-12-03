from authorisation_window import AuthorisationWindow
from answer import Answer
import json
from json import JSONEncoder


def class_to_dict(obj):
    return obj.__dict__

answers = [Answer('8', False), Answer('6', True), Answer('12', False)]
answer = Answer('8', False)

answerJSONData = json.dumps(answers, indent=4, default=class_to_dict)
print(answerJSONData)



#authorisation_window = AuthorisationWindow()











