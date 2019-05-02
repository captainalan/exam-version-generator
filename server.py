import os
from flask import Flask, redirect, request, render_template
app = Flask(__name__, static_url_path='') # Serve static files

@app.route('/')
def index():
    return render_template("index.html")

# Pass in data as argument to render in example
@app.route('/example')
def example(data=None):
    return render_template('example.html', data=data)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)