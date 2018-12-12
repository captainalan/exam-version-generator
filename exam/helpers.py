import json
import os
import re
import string

def getQuestions(defaultDirectory=True, filename=""):
    """Read in questions from json files in the questions folder by
    default, or from a specified file"""

    questions = []

    def getFileContents(file):
        question_data = json.load(file)
        questions.extend(question_data["data"])

    if defaultDirectory==True:
        # Get all the valid JSON files in the questions directory
        json_ext = re.compile(r".*\.json")
        question_filenames = filter(json_ext.search, os.listdir("questions"))

        for filename in question_filenames:
            try:
                with open("./questions/" + filename, "r") as file:
                    getFileContents(file)
            except:
                pass
                # Add some checks for the quality of the questions
                # Handle not JSON or not well formed files
    else:
        # Handle user specified file
        try:
            with open(filename, "r") as file:
                getFileContents(file) 
        except json.decoder.JSONDecodeError:
            print("Bad data! Check the file of questions you specified?")
            return []
        except FileNotFoundError:
            return [] # should complain loudly, not just return a blank list

    return questions
