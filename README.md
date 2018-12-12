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

First, make sure everything is set up.

```bash
python3 -m pipenv install
pipenv shell
```
Now, you can be sure all dependencies are met. To generate multipe versions of
your exam, do something like:

```bash
python create-exam.py  --exam_length 4 --versions 2
```

The above command will create two verions of your exam, of length 4 each. Output
goes to standard output and can easily be piped in UNIX systems. To save the
output to the `client/dist` directory to display, do:

```bash
python create-exam.py  --exam_length 4 --versions 2 > client/dist/my_versions.json
```

Assuming you have [node](https://nodejs.org) installed, from this project's root
directory:

```bash
cd client
npm install
cd ..
```

Start a HTTP server to view the output we generated with Python in a
more useful to humans way:

```bash
node client/server.js
```

Now, navigate to https://localhost:5000/static to see the result!

## More Details

(Since I'm containing all the documentation for this project in the README, I
can put all the non-essential stuff for basic usage here...)

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


## Notes for the developer (me)

A useful page: [Deploying a subfolder to Github
Pages](https://gist.github.com/cobyism/4730490)

### Running tests

I'm writing tests using the `unittest` module.

It can be ta little bit tricky to test modules with test directory this-and-that.
Read more on [Stack Overflow](https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure).

```bash
python -m unittest tests.test_basic
```

### To implement later...

- [ ] Write more useful usage instructions
- [ ] Write client
    - [x] Basic structure
    - [x] Dist directory to Github pages
    - [x] Set up simple Express site
    - [x] Make things look nice on the sample with Bootstrap
    - [x] Use ordered lists when applicable, so HTML is properly structured
    - [ ] User friendly forms for entering question data
- [x] Support for images, text formatting, and other arbitrary HTML
- [x] Specify the length of the exam; must be longer than the number of questions
- [ ] Include diagram of file layout in documentation
- [ ] Allow user to specify input file/directory
- [x] Add deploy script for Github pages

### Tests to write

- [ ] Bad JSON data
- [ ] Blank data file
- [ ] File not found

### Ideas to think about

The questions folder can have some images directory or something similar...

Store the output somewhere to be retrieved and rendered by the client. Maybe
just to the client folder itself?

Real world exam stuff: Sometimes groups of questions have to go
together. For example, there might be some dataset that a few
questions, whose orders matter, are associated with. One possible way
to solve this is to store these things together as a unit in
JSON. Exam lengths then must be calculated with some sort of
"weighting" wherein multi-part questions will have more weight than
single, stand-alone questions.

