# Server Remote Plotter. Python 3.4.3
#Danilo D & George K.

import sys
import socket
import threading
from pylab import *
from numpy import arange, sin, pi
import string
from time import *

print("Servidor de Plots")

def plotSignal(tEjeY,tPrincipal,Color,Data,t,nfigure):
	ion()
	show()
	if nfigure == 1:
		fig = figure(1)
		ax1 = fig.add_subplot(211)
	else:
		if nfigure == 2:
			fig = figure(2)
			ax2 = fig.add_subplot(212)
	draw()
	'''if nfigure == 1:
		ax1 = fig.add_subplot(211)
		var = Data
		ax1.plot(t,var)
		ax1.grid(True)
		ax1.set_ylim( (-2,2) )
		ax1.set_ylabel(tEjeY)
		ax1.set_title(tPrincipal)
		for label in ax1.get_xticklabels():
		    label.set_color(Color)
		draw()
	if nfigure == 2:
		ax2 = fig.add_subplot(212)
		var = Data
		ax2.plot(t,var)
		ax2.grid(Truqe)
		ax2.set_ylim( (-2,2) )
		ax2.set_ylabel(tEjeY)
		ax2.set_title(tPrincipal)
		for label in ax2.get_xticklabels():
		    label.set_color(Color)
		draw()'''



def desempaquetar(byte_array):
	varstr = byte_array.decode()
	newstr = varstr.replace("[", "")
	newstr = newstr.replace("]", "")
	var = [float(s) for s in newstr.split()]
	return var

def Client(IP,PORT,Color_Plot,nfigure):
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
					if data != b'':
						t = arange(0.0, 1.0, 0.01)
						dataU = desempaquetar(data)
						plotSignal("Eje Y","Título",'r',dataU,t,nfigure)
				except:
					print("No hay data entrante")
					break
		finally:
			# Clean up the connection
			print("Cerrando conexion con", clientAddr)
			connection.close()
			exit(-1)

def threadNewClient(IP,PORT,Color_Plot,nfigure):
	tClient = threading.Thread(name='client', target = Client,args=(IP,PORT,Color_Plot,nfigure))
	tClient.start()


def empaquetar(float_array):
	varbyte = str(float_array).encode()
	return varbyte


ip = str(socket.gethostbyname(socket.gethostname()))
print(ip)
threadNewClient(ip,4440,'r',1)
threadNewClient(ip,4439,'b',2)
