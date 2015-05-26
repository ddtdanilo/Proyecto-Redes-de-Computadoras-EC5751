# Server Chat. Python 3.4.3

import sys
import socket
import threading


print("Servidor de Chat")

def Client(IP,PORT,INCOMING_CONN):
	# Create Server Socket (TCP)
	serverAddr = (IP,PORT)
	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		serverSocket.bind(serverAddr)
		serverSocket.listen(INCOMING_CONN)

		print("Configurado con el IP %s por el puerto %s" % serverAddr)
	except:
		print("Error. Puerto Ocupado")
		exit(-1)

	while True:
		# Wait for a connection
		try:
			connection,clientAddr = serverSocket.accept()
			print("\nConexion proveniente de ", clientAddr)
			threadNewConnection(connection,clientAddr)
			print("Hola")
		finally:
			# Clean up the connection
			print("Cerrando conexion con", clientAddr)
			connection.close()
			exit(-1)



def threadNewClient(IP,PORT,INCOMING_CONN):
	tClient = threading.Thread(name='client', target = Client,args=(IP,PORT,INCOMING_CONN))
	tClient.start()

def newConnection(connection,clientAddr):
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



def threadNewConnection(connection,clientAddr):
	tCliente = threading.Thread(name='cliente', target = newConnection, args=(connection,clientAddr))
	tCliente.start()
	print("Nuevo Thread entrante")



ip = str(socket.gethostbyname(socket.gethostname()))
print(ip)
#threadNewClient(ip,4440,10)
threadNewClient(ip,4439,2)
