# Server Remote Plotter. Python 3.4.3
#Danilo D & George K.

import sys
import socket
import threading
import string
from pylab import figure, show
from numpy import arange, sin, pi

print("Servidor de Plots")

def desempaquetar(byte_array):
	varstr = byte_array.decode()
	newstr = varstr.replace("[", "")
	newstr = newstr.replace("]", "")
	var = [float(s) for s in newstr.split()]
	return var

def Client(IP,PORT,Color_Plot):
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
					data = connection.recv(2048)
					#print(data)
					dataU = desempaquetar(data)
					print(dataU)
					#Plot

					t = arange(0.0, 1.0, 0.01)
					fig = figure(1)
					ax1 = fig.add_subplot(211)
					ax1.plot(t,var)
					ax1.grid(True)
					ax1.set_ylim( (-2,2) )
					ax1.set_ylabel('V(t)')
					ax1.set_title('Señal Adquirida por ' + clientAddr)
					for label in ax1.get_xticklabels():
					    label.set_color(Color_Plot)

					# Return an Echo

					strSend = "OK"
					connection.sendall(strSend.encode())
				except:
					print("No hay data entrante")
					break
		finally:
			# Clean up the connection
			print("Cerrando conexion con", clientAddr)
			connection.close()
			exit(-1)

def threadNewClient(IP,PORT,Color_Plot):
	tClient = threading.Thread(name='client', target = Client,args=(IP,PORT,Color_Plot))
	tClient.start()


def empaquetar(float_array):
	varbyte = str(float_array).encode()
	return varbyte

ip = str(socket.gethostbyname(socket.gethostname()))
print(ip)
threadNewClient(ip,4440,'r')
threadNewClient(ip,4439,'b')
