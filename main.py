import json, os
from dotenv import load_dotenv
import requests as req
import argparse
from datetime import datetime

load_dotenv()
def env(var: str): return os.getenv(var)

log = 'https://odometric-synergy.com/api/controller/ObservatoryRiversideController/logToObservatory'
pwd = 'https://odometric-synergy.com/api/controller/AccessController/checkPassword'
logpwd = 'https://odometric-synergy.com/api/controller/ObservatoryRiversideController/logToObservatoryWithPassword'
createDataURL = "https://odometric-synergy.com/api/controller/ObservatoryDataController/createData"

# partie principale
if __name__ == "__main__":
  parser=argparse.ArgumentParser(description='Ecole Direct extact process')

  # Ecole Directe cred
  parser.add_argument('--observatory_id', help='Obs ID', type=str, required=True)
  parser.add_argument('--riverside_id', help='Riverside ID', type=str, required=True)

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
    ,'Host' : 'odometric-synergy.com'
    ,'Origin' : 'https://odometric-synergy.com'
    ,'Referer' : 'https://odometric-synergy.com/observatoire/knauf-insulation/knauf-insulation/obsLogin'
    ,'X-Requested-With' : 'XMLHttpRequest'
  }

  loginResult = session.post(log, headers=headers,data="observatory_id="+str(args.observatory_id)+"&username="+str(args.username))
  print(loginResult.text)
  # print(session.cookies)

  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    ,'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
    ,'Host' : 'odometric-synergy.com'
    ,'Origin' : 'https://odometric-synergy.com'
    ,'Referer' : 'https://odometric-synergy.com/observatoire/knauf-insulation/knauf-insulation/password'
    ,'X-Requested-With' : 'XMLHttpRequest'
  }

  checkPasswordResult = session.post(pwd, headers=headers,data="password="+str(args.password))
  print(checkPasswordResult.text)
  # print(session.cookies)

  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    ,'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
    ,'Host' : 'odometric-synergy.com'
    ,'Origin' : 'https://odometric-synergy.com'
    ,'Referer' : 'https://odometric-synergy.com/observatoire/knauf-insulation/knauf-insulation/password'
    ,'X-Requested-With' : 'XMLHttpRequest'
  }
  checkWithPasswordResult = session.post(logpwd, headers=headers,data="observatory_id="+str(args.observatory_id)+"&riverside_id="+str(args.riverside_id)+"&password="+str(args.password))
  print(checkWithPasswordResult.text)

  now = datetime.now()
  print(str(now)[:10])

  # print(session.cookies)
  payload = 'observatory_id=' + str(args.observatory_id)
  payload += '&riverside_id=' + str(args.riverside_id)
  payload += '&is_unavailable=false'
  payload += "&date=" + str(now)[:10] + "+" + str(args.heure) + "%3A00"
  payload += '&is_sick=false'
  payload += '&is_odor=true'
  payload += '&odor_id=8b55b5c9-caa5-4019-8dd1-9edd931ea0e6' # odeur chimique

  if ( args.force == "fort "):
    payload += '&inconvenience_id=6b36a8bc-97c4-4e12-97e4-676df425d630'
    payload += '&intensity_id=9379a96f-0e26-425e-ad7c-6704e86a3f33'
  else:
    payload += '&inconvenience_id=956be207-c5ac-4d4f-a952-a80835dda4ed'
    payload += '&intensity_id=faf7c7e2-b7ce-4269-9043-99f43c75b6e2'


  payload += '&inconvenience_value='
  payload += '&comment='
  payload += '&from_date='
  payload += '&to_date='
  payload += '&is_noise=false'
  payload += '&noise_id='


  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    ,'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
    ,'Host' : 'odometric-synergy.com'
    ,'Origin' : 'https://odometric-synergy.com'
    ,'Referer' : 'https://odometric-synergy.com/observatoire/knauf-insulation/knauf-insulation/obsObservation'
    ,'X-Requested-With' : 'XMLHttpRequest'
  }
  print(payload)
  createDataResult = session.post(createDataURL, headers=headers,data=payload)
  print(createDataResult.text)

