import socket
import time

#Constants
HEADERSIZE = 10
HOST = '127.0.0.1'
PORT = 5002
#Class for connection
class CONNECTION():
	def __init__(self,host,port):
		self.host = host
		self.port = int(port)


print('''Connection to an address(Test)
        -------------------------------
''')
ans = input('IP ADDRESS:')
ans2 = input('PORT NUMBER:')
complete = CONNECTION(ans, ans2)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(complete.host, complete.port)
s.connect((complete.host, complete.port))



while True:

	full_msg = ''
	new_msg = True
	while True:
		msg = s.recv(16)
		if new_msg:
			print(f'new message length: {msg[:HEADERSIZE]}')
			msglen = int(msg[:HEADERSIZE])
			new_msg = False

		full_msg += msg.decode('utf-8')

		if len(full_msg) -HEADERSIZE == msglen:
			print("Full Message Recieved")
			print(full_msg[HEADERSIZE:])
			new_msg = True
			full_msg = ''

	print(full_msg)
