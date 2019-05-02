import os
from flask import Flask, jsonify, redirect, request, render_template
from exam import getQuestions, Exam

app = Flask(__name__, static_url_path='') # Serve static files

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/example')
def example(data=None):
    return render_template('example.html', data=data)

# Pass in question data to get shuffled questions
@app.route('/create-exam/<questions_file>', methods=['GET'])
def createExam(questions_file):
    try:
        # Exam questions
        qs = getQuestions(False, "./questions/" + questions_file + ".json")

        number_questions = int(request.args.get('n', len(qs)))
        seed = request.args.get('s', 0)

        myExam = Exam(qs)
    except:
        return(jsonify({ 'message': 'Failed to load questions' }))
    return jsonify(myExam.getVersion(number_questions, seed))

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)