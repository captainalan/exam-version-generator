import unittest
from exam import getQuestions, Exam

class TestCliArgs(unittest.TestCase):

    def test_get_questions_default(self):
        """Does the function run with no errors?"""
        self.assertTrue(getQuestions())

    def test_get_questions_file_not_found(self):
        """Should output an error message..."""
        self.assertEqual(getQuestions("foo1234"), [])
        # ...assumption of course is we don't have some file called foo1234

    def test_get_questions_blank_file(self):
        self.assertEqual(getQuestions(defaultDirectory=False,
            filename="./tests/test_data/blank.json"), [])

    def test_exam_len_too_long(self):
        """Error message when there are too many questions requested."""
        pass # Write a test later to do this...

if __name__ == '__main__':
    unittest.main()
