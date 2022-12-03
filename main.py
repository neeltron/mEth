from flask import Flask, render_template, request
from replit import db

app = Flask('app', template_folder = "templates", static_folder = "static")

for i in db.keys():
  print(i)

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/doc')
def doctor():
  current_bucket = {}
  return render_template("doc.html")

@app.route('/metamask', methods = ["GET", "POST"])
def metamask():
  flag = 0
  wallet_address = "0x..."
  a = request.args.get('userWallet')
  for i in db.keys():
    if i == a:
      flag = 1
      return render_template('metamask.html', obj = db[i][0])

  if flag == 0:
    db[a] = ["a"]
    print(a)
    
    return render_template('metamask.html', obj = db[wallet_address][0])
  
  return render_template('metamask.html')

app.run(host='0.0.0.0', port=8080)