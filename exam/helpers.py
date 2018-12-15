import json
import os
import re
import string
import sys

def getQuestions(defaultDirectory=True, filename=""):
    """Read in questions from json files in the questions folder by
    default, or from a specified file. Return an array of `dict`s.
    """

    questions = []

    def getFileContents(f):
        try:
            with open(f, "r") as file:
                question_data = json.load(file)
                questions.extend(question_data["data"])
        except FileNotFoundError:
            print("The file {} was not found.".format(f))
            sys.exit(1)
        except ValueError:
            print("Decoding JSON has failed.")
            sys.exit(1)

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
