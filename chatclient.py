import socket
import select
import sys
import re 
from _thread import *

if len(sys.argv)!=3:
    print("Correct usage: script,IP address, port number,nickname")
    sys.exit()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


In = (sys.argv[1])
a=In.split(':')
ip_addr=str(a[0])
port=int(a[1])
nick=str(sys.argv[2])


server.connect((ip_addr, port))

first_msg=server.recv(2048).decode('utf-8')

print(first_msg)

nick = 'NICK ' + nick


server.sendall(nick.encode('utf-8'))

ok_message=server.recv(2048).decode('utf-8')
print(ok_message)
if ok_message == "OK":
    pass
elif ok_message == "nick name":
    
    print('sorry you are disconnected ')
    sys.exit()
    
    



while True:
    socket_list=[sys.stdin, server]
    

    read_sockets,write_sockets,error_sockets=select.select(socket_list,[],[])
   
    for sockets in read_sockets:
        if sockets == server:
            message = sockets.recv(2048).decode('utf-8')
            print(message)
        else:
            message=sys.stdin.readline()
            
            message = 'MSG '+ message
            if message == '\n':
                continue
            else:
                server.sendall(message.encode('utf-8'))
                sys.stdout.write(message)
                sys.stdout.flush()
                
server.close()
