import random

class Exam:
    """Representation of an exam, questions, answer choices, and correck
    answers
    """

    def __init__(self, questions):
        self.questions = questions # This class questions itself?!
        # What other info do I need to store here? Like versions and stuff?

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
