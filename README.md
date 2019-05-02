# Exam Version Generator

This application can be used to generate different exam versions from a set of
questions stored in JSON format.

A vanilla HTML/CSS/Javascript client is provided to view output. See an nice
looking sample on this repository's [Github pages
site](https://captainalan.github.io/exam-version-generator) 

## Usage

The file `create-exam.py` is the entry-point into using this project. If you
don't specify a file yourself, it it assumed all your questions are stored in
the `/questions` directory in JSON format. See "Question Format" section for
more details).

### Setup

Install dependencies using `pipenv` 
from the project's root directory:

```bash
python3 -m pipenv install
pipenv shell
```

Run the flask server:

    $ export FLASK_ENV=development
    $ flask run

### Create Multiple Versions of an Exam

(This will soon be done by a web interface)

To generate multiple versions of your exam, use the command line program.
For example, you can do something like...

```bash
python create-exam.py  --exam_length 4 --versions 2
```

The above command will create two verions of your exam, of length 4 each. Output
goes to standard output and can easily be piped in UNIX systems. To save the
output to the `client/dist` directory to display, do:

```bash
python create-exam.py  --exam_length 4 --versions 2 > client/dist/my_versions.json
```

## More Details

### Question Format

Questions are stored in JSON format and take the format:

```json
{
    "question": "Is the earth round?",
    "type": "multiple-choice",
    "choices": {
        "a": "yes",
        "b": "no",
        "c": "in a sense",
        "d": "none of your beeswax"
    },
    "correct": "c"
}
```

All the keys for the choices should be uniques (to the question). They don't
have to be letters like a, b, and c. You could do, for example:

```json
{
    "question": "Is the earth round?",
    "type": "multiple choice",
    "choices": {
        "absolutist_positive": "yes",
        "absolutist_negative": "no",
        "nuanced": "in a sense",
        "silly": "none of your beeswax"
    },
    "correct": "nuanced"
}
```

What is important is that `correct` corresponds to one of the answers' key,
otherwise students will have no chance of getting the question correct!

Feature to maybe add: allow `correct` to be an array whereby students may select
multiple correct answers.

### Running tests

I'm writing tests using the `unittest` module.

```bash
python -m unittest tests.test_basic
```

This question on [Stack Overflow](https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure) helped me figure this out.