import json
import os
import re
import string

def getQuestions(defaultDirectory=True, filename=""):
    """Read in questions from json files in the questions folder by
    default, or from a specified file"""

    questions = []

    def getFileContents(filename):
        try:
            with open(filename, "r") as file:
                question_data = json.load(file)
                questions.extend(question_data["data"])
        except json.decoder.JSONDecodeError:
            print("Bad data! Check the file of questions you specified?")
            return []
        except FileNotFoundError:
            return [] # should complain loudly, not just return a blank list

    if defaultDirectory==True:
        # Get all the valid JSON files in the questions directory
        json_ext = re.compile(r".*\.json")
        question_filenames = filter(json_ext.search, os.listdir("questions"))

        for filename in question_filenames:
            myFileName = "./questions/" + filename
            getFileContents(myFileName)
    else:
        # Handle user specified file
        getFileContents(filename) 

    return questions
