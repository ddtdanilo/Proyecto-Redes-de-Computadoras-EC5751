# Client Chat. Python 3.4.3

import sys
import socket


print('Cliente de Chat. Envie "/q" para salir')

# Create Client Socket (TCP)
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the Socket to the port where the Server is listening
PORT = int(input("Introduzca el puerto: "))
IP = input("Introduzca el IP del servidor: ")
serverAddr = (IP,PORT)
print("Conectando a %s por el puerto %s" % serverAddr)
clientSocket.connect(serverAddr)

while True:
	# Send message
	msg = input("Yo: ").encode()
	clientSocket.sendall(msg)

	# Look for the response
	amount_received = 0
	amount_expected = len(msg)
	while amount_received < amount_expected:
		data = clientSocket.recv(amount_expected)
		if not data:
			# Close the Client Socket and exit
			clientSocket.close()
			exit(-1)
		amount_received += len(data)
		dataU = data.decode('UTF-8') # Convert to Unicode
		print("Servidor:", dataU)
