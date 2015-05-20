import socket
import sys
import time
import threading
import hashlib


def Cliente(ip,puerto):
	# Crea el Socket de TCP/IP
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Enlace del socket
	DireccionServidor = (ip,puerto)
	print('Configurado con el IP %s por el puerto %s' %DireccionServidor)
	try:
		sock.bind(DireccionServidor)
		sock.listen(1)
	except:
		print("Error. Puerto Ocupado")
		exit(-1)
	while True:
		# Wait for a connection
		#print('waiting for a connection')
		try:
			connection,client_address = sock.accept()
			print('\nConexion proveniente de: ', client_address)
			# Receive the data in small chunks and retransmit it
			while True:
				try:
					data = connection.recv(1024)
					dataU = data.decode('utf-8').upper()# Convierto Unicode de nuevo
					print(dataU)
					#Devuelvo un Echo
					connection.sendall(dataU.encode())
				except:
					print("No hay data entrante")
					break
		finally:
			# Clean up the connection
			print("Cerrando conexion")
			connection.close()
	
		return

def threadNuevoC(ip,puerto):
	tCliente = threading.Thread(name='cliente', target = Cliente,args=(ip,puerto))
	tCliente.start()

threadNuevoC('localhost',4440)
threadNuevoC('localhost',4439)

