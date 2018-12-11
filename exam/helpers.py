import json
import os
import re
import string

def getQuestions(defaultDirectory=True):
    """Read in questions from json files in the questions folder by
    default, or from a specified file"""

    questions = []

    if defaultDirectory==True:
        # Get all the valid JSON files in the questions directory
        json_ext = re.compile(r".*\.json")
        question_filenames = filter(json_ext.search, os.listdir("questions"))

        for filename in question_filenames:
            with open("./questions/" + filename, "r") as file:
                question_data = json.load(file)
                questions.extend(question_data["data"])
            # Add some checks for the quality of the questions
    else:
        # Add stuff here to handle user specified file
        pass

    return questions
