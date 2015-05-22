import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
puerto = int(input("Introduzca el puerto: "))
ip = input("Introduzca el ip del servidor: ")
server_address = (ip,puerto)
print('Conectando a %s por el puerto %s' % server_address)
sock.connect(server_address)

while True:
	message = sys.stdin.readline()
	message = message.encode()
	sock.sendall(message)
	# Look for the response
	amount_received = 0
	amount_expected = len(message)

	while amount_received < amount_expected:
		data = sock.recv(amount_expected)
		amount_received += len(data)
		dataU = data.decode('utf-8')# Convierto Unicode de nuevo
		print(dataU)