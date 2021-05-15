import requests
import os
import random
import string
import json
from time import sleep

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'http://www.palapaloungelg.ga/login.php'

names = json.loads(open('names.json').read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))

	username = name.lower() + name_extra + '@gmail.com'
	password = ''.join(random.choice(chars) for i in range(8))
	url2 = "http://www.palapaloungelg.ga/login.php?email={}&password={}&signIn=Sign+in&rmShown=1".format(username,password)

	requests.post(url2, allow_redirects=False)

	print('Sending username {} and Password {}'.format(username, password))
