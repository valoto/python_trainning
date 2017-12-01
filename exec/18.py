import json, os, sys
from datetime import datetime

dic = {
        "nome":"FULANO",
        "email":"fulano@fulano.com",
        "data":datetime.now().strftime('%d-%m-%Y')
        }

#print(dic['data'])
#print(datetime.now().strftime('%d-%m-%Y'))
#dic['data'] = 

string = json.dumps(dic)

with open('18.json', 'w') as f:
    f.write(string)

print(dic)

#print(os.system('cat 18.json & cls'))
