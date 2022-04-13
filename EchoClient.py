import socket

socket = socket.socket()
socket.connect(('127.0.0.1',12345))
while True:
    str = input("S: ")
    socket.send(str.encode());
    if str in "Byebye":
        break
    print ("N:",socket.recv(1024).decode())
socket.close()