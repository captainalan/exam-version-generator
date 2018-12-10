let root = document.getElementById("exams-elem");

/* JSON generated with create-exam.py */
const VERSIONS_DIR = "my_versions.json";

/* Sometimes, I refer to these via index. For example, I'll label my first
 * answer choice 'a', the second 'b', and so on. */
const LETTER_CHOICES = "abcde"

// Fetch JSON data
async function getVersions() {
  fetch(VERSIONS_DIR)
  .then(res => {
    if (!res.ok) {
      throw Error(res.statusText);
    }
    return res.json();
  })
  .then(myJSON => {
    root.innerHTML = Exams(myJSON);
  })
  .catch(error => {
    console.log(error);
    return {};
  });
}

// Render exams
const Exams = elem => elem.reduce((acc, version) => acc + Version(version), "");

// Render version
const Version = elem => {
  let versionName = Object.keys(elem)[0];

  let questions = elem[versionName].questions.reduce((acc, question) => {
    return acc + Question(question);
  }, "");

  let answers = elem[versionName].answers.reduce((acc, answer, index) => {
    return acc + `q${index + 1}. ${LETTER_CHOICES[answer]}<br>`
  }, "");

  toReturn = "<div class='exam-version' id='" + versionName + "'>"
           +   "<h2>" + versionName + "</h2>"
           +   "<h3>Questions</h3>"
           +    questions
           +   "<h3>Answers</h3>"
           +    answers
           + "</div>";
  return toReturn;
}

// Render question
const Question = elem => {
  let toReturn = "";

  let answerBlock = `
    <div class='answer-block'>
       ${elem.choices.reduce((acc, choice, index) => {
         return acc 
           + "<div> (" + LETTER_CHOICES[index] + ") " + choice + "</div>"
       }, "")} 
    </div>`

  toReturn = `
    <div class='question'> ${elem.id}. ${elem.question}
      ${answerBlock}
    </div>`;
  return toReturn;
}

// Call Functions, Do Stuff!
getVersions()
