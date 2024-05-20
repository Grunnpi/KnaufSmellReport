import requests as req
import argparse
from datetime import datetime
import json
from urllib.parse import quote_plus

log = 'https://api.app-synergy.tech/user/login'
createDataURL = "https://api.app-synergy.tech/report"

# partie principale
if __name__ == "__main__":
  parser=argparse.ArgumentParser(description='Ecole Direct extact process')

  # Ecole Directe cred
  parser.add_argument('--username', help='User name', type=str, required=True)
  parser.add_argument('--password', help='Pwd', type=str, required=True)

  # telegram mode
  parser.add_argument('--heure', help='Heure', type=str, default="12")
  parser.add_argument('--force', help='Force : fort, extreme', type=str, default="fort")

  parser.print_help()

  args=parser.parse_args()


  session = req.session()


  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    ,'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
    ,'Origin' : 'https://www.app-synergy.tech'
    ,'Referer' : 'https://www.app-synergy.tech/'
  }

  #  loginPayload = "email=pierre.grunnagel%40gmail.com&password=Mdpknauf%2B24&rememberMe=true"
  loginPayload = "email=" + quote_plus(str(args.username)) + "&password=" + quote_plus(str(args.password)) + "&rememberMe=true"
  print(loginPayload)
  loginResult = session.post(log, headers=headers,data=loginPayload)
  print(loginResult.text)
  loginPayload = json.loads(loginResult.text)

  token = loginPayload["token"]["value"]
  user_id = loginPayload["user"]["_id"]
  observatory = loginPayload["user"]["observatoryAffiliation"]["observatory"]["_id"]
  #print(observatory)
  #print("user_id")
  #print(observatory)
  #print("user_id")

  #print(loginPayload["token"]["value"])

  now = datetime.now()
  sToday = str(now)[:10]

  iHeure = int(args.heure)
  iHeure = iHeure - 2
  sHeure = str(iHeure)
  if ( len(sHeure) == 1 ):
    sHeure = "0" + sHeure

  payload = "contact%5BcountryPhoneCode%5D=FR&contact%5BphoneNumber%5D=&report%5Bdate%5D=" + sToday + "T" + sHeure + "%3A00%3A00.015Z&report%5Bemission%5D=6572c9e8e60b709f489f9b1c&report%5BemissionType%5D=odor&report%5BintensityLevel%5D=6&report%5BdiscomfortLevel%5D=5&report%5BnothingToReport%5D=false&_id=" + observatory + "&vigieId=" + user_id
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    ,'Content-Type' : 'application/x-www-form-urlencoded'
    ,'Origin' : 'https://www.app-synergy.tech'
    ,'Referer' : 'https://www.app-synergy.tech/'
    ,'X-Requested-With' : 'XMLHttpRequest'
    ,'Authorization' : token
  }

  print(payload)
  createDataResult = session.post(createDataURL, headers=headers,data=payload)
  print(createDataResult.text)

