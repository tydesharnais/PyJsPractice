import socket
import time

HEADERSIZE = 10

host = '127.0.0.1'
port = 5002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

while True:
	clientsocket, address = s.accept()
	print(f'Connection from: {address}')

	msg = 'Welcome to the server!'
	msg = f'{len(msg):<{HEADERSIZE}}' + msg

	clientsocket.send(bytes(msg, 'utf-8'))

	while True: #Buffer stream / Login info etc.. while loop
		time.sleep(3)
		msg = f'The current time is {time.time()}'
		msg = f'{len(msg):<{HEADERSIZE}}' + msg
		clientsocket.send(bytes(msg, 'utf-8'))
