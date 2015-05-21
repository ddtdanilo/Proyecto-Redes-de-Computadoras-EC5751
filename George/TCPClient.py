from socket import *

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input lowercase sentence:')
clientSocket.send(bytes(sentence, 'UTF-8'))
modiefiedSentence = clientSocket.recv(2048).decode('UTF-8')
print('From Server:', modiefiedSentence)
clientSocket.close()
input("Presione enter para cerrar")
