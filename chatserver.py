import socket 
import select 
import sys 
import re 
from _thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) != 2:
	print("correct usage: script, IP address, port number")
	sys.exit() 

In = (sys.argv[1])
a = In.split(':')
iP_addr = str(a[0])
port = int(a[1])

server.bind((ip_addr, port))
server.listen(100)
print('establishing connection')

list_of_clients = []
list_of_clients.append(server)



def clientthread(conn,addr):
	while True:
		try:
			nick = conn.recv(2048).decode('utf-8')
			nick1 = nick.strip('NICK')

			if len(nick1)<=12 and 'NICK' in nick :
				conn.sendall('OK'.encode('utf-8'))
				break
			elif len(nick1) != None:
				conn.sendall('error nick name'.encode('utf-8'))
			else:
				conn.close()
				print(addr[0]+ "no connection")
				clients.remove(conn)
				del clients[conn]
				break
		except:
				break		

	while True:
		try:
			if conn in clients:
				msg = conn.recv(2048).decode('utf-8')
				msg1 = msg.strip('MSG')

				if not msg:
					conn.close()
					print(addr[0]+ "Disconnected")
					clients.remove(conn)
					break
				elif 'MSG' not in msg:
					conn.sendall(('error message'.encode('utf-8')))
				else:
					if len(msg1)<=255:
						count=0
						for i in msg1[:-1]:
							if ord(i)<31:
								count = count + 1
							else:
								pass

						if count !=0:
							conn.sendall('no control characters'.encode('utf-8'))
						else:
							sent_message = 'message'+'nick1'+' '+ msg1[:-1]
							broadcast(sent_message,conn,nick1)
					elif len(msg1) > 255 :
						conn.sendall('error'.encode('utf-8'))
		
		except KeyboardInterrupt:
			conn.close()
			break

def broadcast(message,connection,nick1):
	for sockets in list_of_clients:
		if sockets == server:
			try:
				sockets.sendall(message.encode('utf-8'))
			except KeyboardInterrupt:
                    clients.remove(sockets)
                    break 


while True:
	conn,addr = server.accept()
	conn.sendall('Hello 1'.encode('utf-8'))
	list_of_clients.append(conn)
	print (addr[0] + "connected"

	start_new_thread(clientthread,(conn,addr))

conn.close()
server.close()

