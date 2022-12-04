from flask import Flask, render_template, request
from replit import db
import random
import jwt
from methods import *

db.clear()

app = Flask('app', template_folder = "templates", static_folder = "static")

for i in db:
  print(i)

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/signup')
def signup():
  signal = str(random.randint(10000, 100000))
  return render_template('signup.html', obj = signal)

@app.route('/doc')
def doctor():
  current_bucket = {}
  return render_template("doc.html")

@app.route('/getstarted', methods = ["GET", "POST"])
def metamask():
  token = request.args.get('verification_jwt')
  decoded_json = jwt.decode(token, options={"verify_signature": False})
  nullify = decoded_json["nullifier_hash"]
  flag = 0
  a = request.args.get('userWallet')
  
  for i in db.keys():
    if i == nullify:
      flag = 1
      print("in loop")
      return render_template('metamask.html', obj = db[i][0])

  if flag == 0 and request.method == "POST":
    name = request.form.get('name')
    db[nullify] = ["0xc3637Ce856bab11019b2b7505d2852750B050a2D", name, decoded_json["signal"]]
    print("here", db[nullify])
    
    return render_template('metamask.html', obj = "null")
  else:
    return render_template('metamask.html', obj = "null")

app.run(host='0.0.0.0', port=8080)
