import json, os
from dotenv import load_dotenv
import requests as req

load_dotenv()
def env(var: str): return os.getenv(var)

log = 'https://odometric-synergy.com/api/controller/ObservatoryRiversideController/logToObservatory'
pwd = 'https://odometric-synergy.com/api/controller/AccessController/checkPassword'
logpwd = 'https://odometric-synergy.com/api/controller/ObservatoryRiversideController/logToObservatoryWithPassword'

fullLog = f'https://odometric-synergy.com/api/controller/ObservatoryRiversideController/logToObservator?observatory_id={env("observatory_id")}&username={env("username_report")}'
fullPwd = f'https://odometric-synergy.com/api/controller/AccessController/checkPassword?password={env("PASSWORD")}'
fullLogpwd = f'https://odometric-synergy.com/api/controller/ObservatoryRiversideController/logToObservatoryWithPassword?observatory_id={env("observatory_id")}&riverside_id={env("riverside_id")}&password={env("PASSWORD")}'

payload = {
  'observatory_id': {env("observatory_id")},
  'username': env('username_report')
}
session = req.session()

# session.request('POST', fullLog, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'})
# session.request('POST', fullPwd, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'})
# session.request('POST', fullLogpwd, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'})

print(
  env('username_report'),
  env('password_report'),
  env('observatory_id'),
  env('riverside_id'),
)
