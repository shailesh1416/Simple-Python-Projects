from pyperclip import paste
from json import loads
from requests import get, request
from subprocess import run
# https: // api.dictionaryapi.dev/api/v2/entries/en/<word >


word = 'school'

# extract data
response_api = get(
    'https://api.dictionaryapi.dev/api/v2/entries/en/'+word)

# decode data

data = loads(response_api.text)
definition = data[0]['meanings'][0]['definitions'][0]['definition']

run(['notify-send', definition])
