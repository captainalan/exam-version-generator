import argparse
from exam import getQuestions, Exam
import json

parser = argparse.ArgumentParser()
parser.add_argument("--exam_length", type=int,
    help="Number of questions in the exam. Must be <= questions available.")
parser.add_argument("--questions_file", default="none", type=str,
    help="A file containing questions and answers")
parser.add_argument("--seed", default=1, type=int,
    help="An integer to use as a seed for Python's random number module")
parser.add_argument("--versions", default=1, type=int,
    help="An integer representing the number of exam versions you want.")
args = parser.parse_args()

# Get parameters
EXAM_LEN = args.exam_length
START_SEED, NUM_VERSIONS = args.seed, args.versions

# Get questions 
if args.questions_file == "none":
    questions = getQuestions(defaultDirectory=True)
else:
    # Add some check here to see if the file even exists
    questions = getQuestions(args.questions_file)

# Check if exam_len is okay
if EXAM_LEN > len(questions):
    print("Not enough questions. Please specify a shorter exam length!")
    exit(1)
else:
    # Make Exam from questions and generate versions using starting seed
    versions = []
    myExam = Exam(questions)
    for i in range(0,NUM_VERSIONS):
        label = "Version " + str(i + 1)
        versions.append({label : myExam.getVersion(EXAM_LEN, START_SEED + i)})

    # Print to standard output
    print(json.dumps(versions, indent=2, ensure_ascii=False))
