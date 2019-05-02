from flask import Flask, redirect, request
app = Flask(__name__, static_url_path='') # Serve static files

@app.route('/')
def hello_world():
    return redirect("/index.html", code=302)