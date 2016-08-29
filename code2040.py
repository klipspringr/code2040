# some code to get modules working
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# module that makes HTTP requests easy!
import requests

new_req = requests.post("http://challenge.code2040.org/api/prefix", data={'token': 'abfa1dcb4c71b9fd3f790440b332f76c'})
req = new_req.json()

prefix = req['prefix']
array = req['array']
array_wo_prefix = []

# only add strings that don't have the the prefix to array_wo_prefix
for i in range(len(array)):
	if array[i][:len(prefix)] != prefix:
		array_wo_prefix.append(str(array[i]))

payload = {'token': 'abfa1dcb4c71b9fd3f790440b332f76c', 'array': array_wo_prefix}

# ensure that the content type of the payload is JSON, otherwise it will not be sent as a dictionary!!
check = requests.post("http://challenge.code2040.org/api/prefix/validate", json=payload)
