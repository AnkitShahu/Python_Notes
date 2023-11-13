import requests
import json
import time
db= []
for i in range(5):
    time.sleep(.1)
    url = "https://randomuser.me/api/"
    r = requests.get(url)
    jsondata = r.content
    # print(jsondata)
    list_i = json.loads(jsondata)
    # print(list_i)
    # print(type(list_i))
    sam_d = {}

    x = list_i['results']
    for i in x:
        # print(i['name']['first'])
        # print(i['name']['last'])
        # print(i['location']['city'])
        # print(i['location']['state'])
        # print(i['location']['country'])
        # db.append(i['name']['first'])
        # num = 1
        # num=num+1
        # name = 'name'+ str(num)
        # city = 'city'+ str(num)
        sam_d.update({'name': (i['name']['first'] +' '+ i['name']['last']), 'city': i['location']['city'], 'state': i['location']['state'], 'country': i['location']['country'] })
        # print(sam_d)
        db.append(sam_d)
print(db)




#------------optimize-------------

import requests
import time

db = []

for _ in range(5):
    time.sleep(0.1)
    url = "https://randomuser.me/api/"
    r = requests.get(url)
    data = r.json()

    for result in data['results']:
        user_data = {
            'name': f"{result['name']['first']} {result['name']['last']}",
            'city': result['location']['city'],
            'state': result['location']['state'],
            'country': result['location']['country']
        }
        db.append(user_data)

print(db)