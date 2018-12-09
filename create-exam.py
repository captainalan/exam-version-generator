import argparse
from exam import getQuestions, Exam
import json

parser = argparse.ArgumentParser()
parser.add_argument("--seed", default=1, type=int,
    help="An integer to use as a seed for Python's random number module")
parser.add_argument("--versions", default=1, type=int,
    help="An integer representing the number of exam versions you want.")
args = parser.parse_args()

# Get parameters
START_SEED, NUM_VERSIONS = args.seed, args.versions

# Make Exam from questions and generate versions using starting seed
versions = []
myExam = Exam(getQuestions())
for i in range(0,NUM_VERSIONS):
    label = "version_" + str(i + 1)
    versions.append({label : myExam.getVersion(START_SEED + i)})

# Print to standard output
print(json.dumps(versions, indent=2, ensure_ascii=False))
