# some code to get modules working
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# module that makes HTTP requests easy!
import requests

req = requests.post("http://challenge.code2040.org/api/reverse", data={'token': 'abfa1dcb4c71b9fd3f790440b332f76c'})
# data gets returned in req.content, so we'll reverse it there

reversed_word = ''

print(req.content)

for i in range(len(req.content)):
	reversed_word = req.content[i] + reversed_word

print(reversed_word)

new_req = requests.post("http://challenge.code2040.org/api/reverse/validate", data={'token': 'abfa1dcb4c71b9fd3f790440b332f76c', 'string': reversed_word})