import unittest
from validation import Validation


class TestValidation(unittest.TestCase):
        def test_validate_user_name(self):
                correct_user_name = "Fedor"
                self.assertTrue(Validation.validate_user_name(correct_user_name))
                incorrect_user_name = "F"
                self.assertFalse(Validation.validate_user_name(incorrect_user_name))
                with self.assertRaises(TypeError):
                        Validation.validate_user_name(1)

        def test_check_name_uniqueness(self):
                correct_user_name = "Евлампий Евстрахович"
                self.assertTrue(Validation.check_name_uniqueness(correct_user_name))
                incorrect_user_name = "Администратор"
                self.assertFalse(Validation.check_name_uniqueness(incorrect_user_name))
                with self.assertRaises(TypeError):
                        Validation.check_name_uniqueness(21)

        def test_validate_question(self):
                correct_question = "Сколько будет 2+2*2?"
                self.assertTrue(Validation.validate_question(correct_question))
                incorrect_question = "33?"
                self.assertFalse(Validation.validate_question(incorrect_question))
                with self.assertRaises(TypeError):
                        Validation.validate_question(321)

        def test_validate_answer(self):
                correct_answer = "6"
                self.assertTrue(Validation.validate_answer(correct_answer))
                incorrect_answer = ""
                self.assertFalse(Validation.validate_answer(incorrect_answer))
                with self.assertRaises(TypeError):
                        Validation.validate_answer(4315)

if __name__ == "__main__":
 unittest.main()
