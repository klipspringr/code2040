# some code to get modules working
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# module that makes HTTP requests easy!
import requests

req = requests.post("http://challenge.code2040.org/api/haystack", data={'token': 'abfa1dcb4c71b9fd3f790440b332f76c'}).json()
# data gets returned in req.content, so we'll find the needle in the haystack there when converted to json

needle = req['needle']
haystack = req['haystack']

for i in range(len(haystack)):
	if haystack[i] == needle:
		needle_int = i

req = requests.post("http://challenge.code2040.org/api/haystack/validate", data={'token': 'abfa1dcb4c71b9fd3f790440b332f76c', 'needle': needle_int})