import random

class Exam:
    """Representation of an exam, questions, answer choices, and correct
    answers
    """

    def __init__(self, questions=[]):
        self.questions = questions # This class questions itself?!
        # What other info do I need to store here? Like versions and stuff?

    def addQuestion(self, question):
        """Add a question to this Exam."""
        if type(question) != dict:
            raise TypeError("Question should be a dict.")

        keys = question.keys()
        # Check to make sure entries for all necessary keys are present.
        necessary = ["question", "correct"]
        for n in necessary:
            if n not in keys:
                raise ValueError("No question in keys.")
        self.questions.append(question)

    def removeQuestion(self, search, questionIndex=False):
        """Attempt to remove a question from this exam as specified by an 
        index or (sub)string. Remove question as specified index 
        OR the first question such that `search` matches the value of key question" 
        """
        if questionIndex == True and\
            type(search) == int and search < len(self.questions):
                print("Initiating removal of search={}".format(search))
                del self.questions[search]
                print("After trying to delete i={}, var questions is: {}".format(search, self.questions))
        elif questionIndex == False:
            # Search questions for string `search`
            pass
        else:
            raise ValueError("Bad input.")

    def getQuestions(self):
        return self.questions

    def getVersion(self, length, seed=1):
        """Generate an exam version from the questions based on seed

        For individual versions, store the question and answer choice orderings
        by using lists. Correct answers are indicated by (integer) indices.
        """

        random.seed(seed)
        shuffled_questions = random.sample(self.questions, k=len(self.questions))

        # Set name to seed number if it isn't specified
        version = { # Return data as a dictionary
            "questions":  [],
            "answers": []
        }

        for i in range(0, length):

            # Save some typing
            this_question = shuffled_questions[i]

            question = {
                "id": "q" + str(i + 1), # Start question numbering from 1
                "question": this_question["question"],
                "choices": [],
            }

            # Answer choices for current question are shuffled dict values
            choices = random.sample(
                    list(this_question["choices"].keys()),
                    k=len(this_question["choices"]))

            # Choices presented as list
            question["choices"]\
                = [ this_question["choices"][key] for key in choices ]

            # Correct answer is an index; store in version
            version["answers"].append(\
                question["choices"].index(this_question["choices"]\
                [this_question["correct"]]))

            version["questions"].append(question)

        return version
