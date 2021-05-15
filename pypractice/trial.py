import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'http://www.palapaloungelg.ga/login.php?email=ijj&password=kltrylktyrlt&signIn=Sign+in&rmShown=1'
url2 = 'http://www.palapaloungelg.ga/login.php?email=ijj&password=kltrylktyrlt&signIn=Sign+in&rmShown=1'
names = json.loads(open('names.json').read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))

	username = name.lower() + name_extra + '@gmail.com'
	password = ''.join(random.choice(chars) for i in range(8))
	url2 = "http://www.palapaloungelg.ga/login.php?email={}&password={}&signIn=Sign+in&rmShown=1".format(username,password)
	print('Sending Login to {}'.format(url2))
