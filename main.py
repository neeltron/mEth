from flask import Flask, render_template
from replit import db

app = Flask('app', template_folder = "templates", static_folder = "static")

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/doc')
def doctor():
  current_bucket = {}
  return render_template("doc.html")

@app.route('/metamask')
def metamask():
  return render_template('metamask.html')

app.run(host='0.0.0.0', port=8080)