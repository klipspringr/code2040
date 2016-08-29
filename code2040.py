# some code to get modules working
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# module that makes HTTP requests easy!
import requests
import json

# module that will help with converting ISO 8601 to a Python datetime object
import dateutil.parser
import datetime

req = requests.post("http://challenge.code2040.org/api/dating", data={'token': 'abfa1dcb4c71b9fd3f790440b332f76c'}).json()

# grab the ISO 6801 datestamp and convert to python datetime object
old_time = dateutil.parser.parse(req['datestamp'])

# add the interval to the initial datestamp, and create a new one
new_time = old_time + datetime.timedelta(seconds=req['interval'])

# the format wanted by the API is somewhat ambiguous. though a valid ISO 6801 may end in either "+00:00" or 
# "Z", the API will only accept a string ending in "Z". so, if the string does not end with "Z", replace it.
if new_time.isoformat()[-6:] == "+00:00":
	new_time = new_time.isoformat()[:-6] + 'Z'
else:
	new_time = new_time.isoformat()

payload = {'token': 'abfa1dcb4c71b9fd3f790440b332f76c', 'datestamp':new_time}

# ensure that the content type of the payload is JSON, otherwise it will not be sent as a dictionary!!
check = requests.post("http://challenge.code2040.org/api/dating/validate", json=payload)