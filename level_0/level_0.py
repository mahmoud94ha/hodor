#!/usr/bin/python3
"""script that votes 1024 times for 3247 user
"""

import requests
failures = 0
success = 0

print("Starting program...")

URL = 'http://158.69.76.135/level0.php'
user_data = {
    'id': '3247',
    'holdthedoor': 'Submit',
}

for _ in range(2):
    r = requests.post(URL, data=user_data)
    if (r.status_code == 200):
        success += 1
    else:
        failures += 1

print("you voted {} times for {} user".format(success, user_data['id']))
print("Successes → {}\nFailures → {}".format(success, failures))
