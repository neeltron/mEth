from flask import Flask, render_template, request
from replit import db
import random
import jwt

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

import requests
import random

url = "https://api.nftport.xyz/v0/mints/customizable/batch"
mint_to_address = "0xc3637Ce856bab11019b2b7505d2852750B050a2D"

prescription = {
  'wallet' : mint_to_address,
  'medicines' : {
    'Oxycodone' : 1,
    'Adderall' : 10,
    'Xanax' : 5,
  }
}



@app.route('/savePrescription', methods=['POST'])
def execute_prescription():
  try:
    prescription = request.get_json()
    wallet_to_mint = prescription['wallet']
    medicines = prescription['medicines']
    final_prescription = []
    for key in medicines:
      final_prescription.append(
        {
          "mint_to_address": wallet_to_mint,
          "token_id": get_token_id(medicines['key'], wallet_to_mint),
          "quantity": medicines['key']['quantity'],
          "metadata_uri": get_metadata(medicines['key'])
        }
      )
    print(final_prescription)
    return None
    
  except:
    return e

def get_token_id(medicine_name, wallet_address):
  token = str(len(medicine_name))
  token += str(randint(100000, 999999))
  token += wallet_address
  return token

def get_metadata(medicine_name):
  return medicine_uri_dictionary['medicine_name']

def mint_prescripton(medicines):
  payload = {
      "tokens": medicines,
      "chain": "polygon",
      "contract_address": "0x17cea1861b7c7db303cfbe44640348dfc4bf74f2"
  }
  headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "14c1db65-1bfb-4ac9-b367-c8cc322415d4"
  }
  #response = requests.post(url, json=payload, headers=headers)
  return response


#print(response.text)

medicine_uri_dictionary = {
  'Oxycodone': 'ipfs://bafkreiazyva324ym27vbwzx4d4sfzo6htpopszw6cq5otfbjnsjcvr6rey',
  'Adderall': 'ipfs://bafkreiazyva324ym27vbwzx4d4sfzo6htpopszw6cq5otfbjnsjcvr6rey',
  'Xanax': 'ipfs://bafkreiazyva324ym27vbwzx4d4sfzo6htpopszw6cq5otfbjnsjcvr6rey'  
}



app.run(host='0.0.0.0', port=8080)
