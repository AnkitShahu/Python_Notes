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





