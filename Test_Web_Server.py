# Server Chat. Python 3.4.3

import sys
import socket
import threading
from numpy  import *

print("Servidor de Chat")

def Client(IP,PORT):
	# Create Server Socket (TCP)
	serverAddr = (IP,PORT)
	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		serverSocket.bind(serverAddr)
		serverSocket.listen(4)

		print("Configurado con el IP %s por el puerto %s" % serverAddr)
	except:
		print("Error. Puerto Ocupado")
		exit(-1)

	while True:
		# Wait for a connection
		try:
			connection, clientAddr = serverSocket.accept()
			print("\nConexion proveniente de ", clientAddr)
			# Receive the data in small chunks and retransmit it
			while True:
				try:
					data = connection.recv(1024)
					if data.decode('UTF-8') == '/q': break
					# Convert to Unicode and uppercase
					dataU = data.decode('UTF-8').upper()
					print(dataU)
					# Return an Echo
					connection.sendall(dataU.encode())
				except:
					print("No hay data entrante")
					break
		finally:
			# Clean up the connection
			print("Cerrando conexion con", clientAddr)
			connection.close()
			exit(-1)

def threadNewClient(IP,PORT):
	tClient = threading.Thread(name='client', target = Client,args=(IP,PORT))
	tClient.start()


ip = str(socket.gethostbyname(socket.gethostname()))
print(ip)
threadNewClient(ip,4440)
threadNewClient(ip,4439)
