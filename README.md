This application can be used to generate different exam versions from a set of
questions stored in JSON format.

A vanilla HTML/CSS/Javascript client is provided to view output. This way,
normal users can copy/paste generated output for further formatting in
applications like Microsoft Word, making sure page breaks are in appropriate
places and what not. I thought about directly producing LaTeX, but ultimately
opted for the current way of doing things to keep dependencies easy.

## Usage

The file `create-exam.py` is the entry-point into using this project. It it
assumed all your questions are stored in the `/questions` directory in JSON
format (see "Question Format" below for more details)).

```bash
echo Add some instructions here, for real!
```

Contained in the `/client` directory is a simple view of the output...

## More Details

(Since I'm containing all the documentation for this project in the README, I
can put all the non-essential stuff for basic usage here...)

### Multiple Versions

(Notes on how to use multiple versions and stuff).

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

### To implement later...

- [ ] Write HTML client
- [ ] Support for images, text formatting, and other arbitrary HTML
- [ ] Specify the length of the exam; must be longer than the number of questions
- [ ] Include diagram of file layout in documentation

### Ideas to think about

Store HTML in JSON file(s)? This way images, bolded/italicized text, etc can be
used in questions, in addition to just normal plain text.

The questions folder can have some images directory or something similar...

Store the output somewhere to be retrieved and rendered by the client. Maybe
just to the client folder itself?

