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

    def test_singleton_question_file(self):
        target = [{
            'question': 'foo?',
            'type'    : 'multiple-choice',
            'choices' : { 'a': 'bar', 'b': 'biz', 'c': 'baz', 'd': 'bees' },
            'correct' : 'a'
        }]

        self.assertEqual(getQuestions(defaultDirectory="false",
            filename="./tests/test_data/one_question.json"), target)

if __name__ == '__main__':
    unittest.main()
