import unittest
from exam import getQuestions, Exam

class TestCliArgs(unittest.TestCase):
    # Some variables and things to use in tests

    myGoodQuestion = {
        'question': 'Did it work?',
        'type'    : 'multiple-choice',
        'choices' : { 'a': 'yes', 'b': 'foo', 'c': 'bar', 'd': 'baz' },
        'correct' : 'a'
    }

    myBadQuestion = {
        'not_a_question': 'I do not ask questions.',
        'type'    : 'multiple-choice',
        'choices' : { 'a': 'foo', 'b': 'bar', 'c': 'baz' },
        'correct' : 'There is no right answer.'
    }

    def test_getQuestions_file_not_found(self):
        with self.assertRaises(SystemExit) as cm:
            getQuestions(defaultDirectory=False,
                filename="foo1234")
        self.assertEqual(cm.exception.code, 1)

    def test_getQuestions_blank_file(self):
        with self.assertRaises(SystemExit) as cm:
            getQuestions(defaultDirectory=False,
                filename="./tests/test_data/blank.json")
        self.assertEqual(cm.exception.code, 1)

    def test_getQuestions_bad_json(self):
        with self.assertRaises(SystemExit) as cm:
            getQuestions(defaultDirectory=False,
                filename="./tests/test_data/bad_data.json")
        self.assertEqual(cm.exception.code, 1)

    def test_getQuestions_singleton_question_file(self):
        target = [{
            'question': 'foo?',
            'type'    : 'multiple-choice',
            'choices' : { 'a': 'bar', 'b': 'biz', 'c': 'baz', 'd': 'bees' },
            'correct' : 'a'
        }]

        self.assertEqual(getQuestions(defaultDirectory="false",
            filename="./tests/test_data/one_question.json"), target)

    def test_Exam_addQuestion_good_question(self):
        myExam = Exam() 
        myExam.addQuestion(self.myGoodQuestion)
        self.assertEqual(myExam.getQuestions(), [self.myGoodQuestion])

    def test_Exam_addQuestion_bad_question(self):
        myExam = Exam() 
        try:
            myExam.addQuestion(self.myBadQuestion)
        except ValueError:
            pass
            # When input is bad, nothing should be added.
        self.assertEqual(myExam.getQuestions(), [])

    def test_Exam_removeQuestion_valid(self):
        myExam = Exam() # Seems to reuse myExam from earlier...?
        myExam.removeQuestion(search=0, questionIndex=True) 
        self.assertEqual(myExam.getQuestions(), [])

    def test_Exam_removeQuestion_invalid(self):
        pass # Gotta figure out how to write this test

if __name__ == '__main__':
    unittest.main()
