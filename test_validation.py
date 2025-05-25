import unittest

import validation
from validation import Validation


class TestValidation(unittest.TestCase):
        def test_validate_user_name(self):
                correct_user_name = "Fedor"
                self.assertTrue(Validation.validate_user_name(correct_user_name))
                incorrect_user_name = "F"
                self.assertFalse(Validation.validate_user_name(incorrect_user_name))
                with self.assertRaises(TypeError):
                        validation.Validation(1)

if __name__ == "__main__":
 unittest.main()