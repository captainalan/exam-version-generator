Generate multiple choice exams from questions organized by topic.

## Usage

(Easy to follow usage instructions)

## More Details

### Getting Help

### Multiple Versions

(Notes on how to use multiple versions and stuff).

### Question Format

Questions are stored in JSON format and take the format:

```
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

```
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


(Put a diagram of the file layout here)

### To implement later...

[ ] Specify the length of the exam; must be longer than the number of questions

