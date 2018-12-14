import unittest
from exam import getQuestions, Exam

class TestCliArgs(unittest.TestCase):

    def test_get_questions_file_not_found(self):
        with self.assertRaises(SystemExit) as cm:
            getQuestions(defaultDirectory=False,
                filename="foo1234")
        self.assertEqual(cm.exception.code, 1)

    def test_get_questions_blank_file(self):
        with self.assertRaises(SystemExit) as cm:
            getQuestions(defaultDirectory=False,
                filename="./tests/test_data/blank.json")
        self.assertEqual(cm.exception.code, 1)

    def test_get_questions_bad_json(self):
        with self.assertRaises(SystemExit) as cm:
            getQuestions(defaultDirectory=False,
                filename="./tests/test_data/bad_data.json")
        self.assertEqual(cm.exception.code, 1)

    def test_singleton_question_file(self):
        target = [{
            'question': 'foo?',
            'type'    : 'multiple-choice',
            'choices' : { 'a': 'bar', 'b': 'biz', 'c': 'baz', 'd': 'bees' },
            'correct' : 'a'
        }]

        self.assertEqual(getQuestions(defaultDirectory="false",
            filename="./tests/test_data/one_question.json"), target)

    def test_add_question(self):
        # Start with blank exam
        myExam = Exam() 
        pass # Write this!

    def test_remove_question_valid(self):
        pass # Write this!

    def test_remove_question_invalid(self):
        """Try to remove a question that doesn't exist."""
        pass 

if __name__ == '__main__':
    unittest.main()
