import requests
import random

url = "https://api.nftport.xyz/v0/mints/customizable/batch"
mint_to_address = "0xc3637Ce856bab11019b2b7505d2852750B050a2D"

# {
#   'wallet' : ""
#   'medicines' : {
#     'medicine_1' : Quant
#   }
# }

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
  'Oxycodone': 'ipfs://bafkreiazyva324ym27vbwzx4d4sfzo6htpopszw6cq5otfbjnsjcvr6rey'
  
}


def check_validity()