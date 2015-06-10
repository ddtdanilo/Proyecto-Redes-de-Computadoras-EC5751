# Server Remote Plotter. Python 3.4.3
#Danilo D & George K.

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import sys
import socket
import threading
from pylab import *
from numpy import arange, sin, pi
import string
from time import *
import logging

print("Servidor de Plots")

def plotSignal(tEjeY,tPrincipal,Color,Data,t,nfigure,IP,Contador):
	fig, ax = plt.subplots()
	ax.plot(t,Data)
	ax.set_xlabel('t(s)')
	ax.set_ylabel('voltaje (mV)')
	ax.set_title('Data entrante desde: %s' %str(IP))
	#dImage = "" + str(IP) + " " + str(Contador) + ".png"
	#hFecha = datetime.datetime.now().strftime(" Fecha: %d/%m/%Y Hora: %H:%M:%S")
	fig.savefig("Registro/" + str(IP) + " " + str(Contador)  + ".png")
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
	Contador = 1

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
						plotSignal("Eje Y","Título",'r',dataU,t,nfigure,clientAddr,Contador)
						Contador = Contador + 1
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
threadNewClient(ip,4444,'r',1)
threadNewClient(ip,4445,'b',2)
