# Client Plotter. Python 3.4.3

from time import *
from pylab import figure, show
from numpy import arange, sin, pi
import string
import sys
import socket


def empaquetar(float_array):
	varstr = str(float_array).encode()
	return varstr



print('Cliente de Plots.')

# Create Client Socket (TCP)
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the Socket to the port where the Server is listening
PORT = int(input("Introduzca el puerto: "))
#IP = input("Introduzca el IP del servidor: ")
serverAddr = ('192.168.1.31',PORT)
print("Conectando a %s por el puerto %s" % serverAddr)
clientSocket.connect(serverAddr)
desfase = 0

while True:
	# Send message
	#input("Presione enter para continuar")
	
	t = arange(0.0, 1.0, 0.01)
	var = sin(2*pi*t + desfase)
	desfase = desfase + 0.1
	msg = empaquetar(var)
	#print(msg)
	clientSocket.sendall(msg)
	print("Enviado el paquete")
	sleep(1)


	






