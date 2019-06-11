import json

with open('inshorts.json') as json_data:
    jsonData = json.load(json_data)

for i in jsonData:
    print (i['Title']+'\n')