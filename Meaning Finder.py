from pyperclip import paste
from json import loads
from requests import get, request
from subprocess import run
# https: // api.dictionaryapi.dev/api/v2/entries/en/<word >


word = input("Enter a word")

# extract text
response_api = get(
    'https://api.dictionaryapi.dev/api/v2/entries/en/'+word)

# decode data
data = loads(response_api.text)

#Extracting definition from json
definition = data[0]['meanings'][0]['definitions'][0]['definition']



# code set a linux notifcation- this can be used as a script with a shortcut to find definition on th go
#run(['notify-send', definition])

print("Definitin :",definition)

