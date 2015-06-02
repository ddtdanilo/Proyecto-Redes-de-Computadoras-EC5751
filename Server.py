# Server Remote Plotter. Python 3.4.3
#Danilo D & George K.

import sys
import socket
import threading
from pylab import *
from numpy import arange, sin, pi
import string
from time import *
import logging

print("Servidor de Plots")

def plotSignal(tEjeY,tPrincipal,Color,Data,t,nfigure):
	'''ion()
	show()
	ax1 = fig.add_subplot(211)
	var = Data
	ax1.plot(t,var)
	ax1.grid(True)
	ax1.set_ylim( (-2,2) )
	ax1.set_ylabel(tEjeY)
	ax1.set_title(tPrincipal)
	for label in ax1.get_xticklabels():
	    label.set_color(Color)
	draw()'''
	print(Data)
	



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
		strIn = "Error. Puerto Ocupado " + str(PORT)
		logging.info("Error. Puerto Ocupado")
		exit(-1)

	while True:
		# Wait for a connection
		try:
			connection, clientAddr = serverSocket.accept()
			strNC = "\nConexion proveniente de " + str(clientAddr) + "\n"
			print(strNC)
			logging.info(strNC)
			# Receive the data in small chunks and retransmit it
			while True:
				try:
					data = connection.recv(2048)
					#print(data)
					if data != b'':
						t = arange(0.0, 1.0, 0.01)
						dataU = desempaquetar(data)
						plotSignal("Eje Y","Título",'r',dataU,t,nfigure)
						rString = "OK"
						connection.sendall(rString.encode())
						### Guardar en archivo
						strDataf = 'Data proveniente de:  '  + str(clientAddr) + '\n' + str(dataU) + '\n'
						logging.info(strDataf)
						
				except:
					print("No hay data entrante")
					break
		finally:
			# Clean up the connection
			strOut = "Cerrando conexion con " + str(clientAddr)
			print(strOut)
			logging.info(strOut)
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
logging.basicConfig(filename='dataLog.txt',level=logging.DEBUG)
Head = '\n\n\n\n' + datetime.datetime.now().strftime(" Fecha: %d/%m/%Y Hora: %H:%M:%S") + '\n'
print(Head)
logging.info(Head)
logging.info('IP de este servidor %s \n' %ip)
threadNewClient(ip,4440,'r',1)
threadNewClient(ip,4439,'b',2)
