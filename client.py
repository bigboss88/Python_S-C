from socket import *
target = input("Enter target ip addr: ")
port = 14000
addr = (target,port)
UDPSock = socket(AF_INET,SOCK_DGRAM)
while True:
    data = input("Enter Message to send!: ")
    UDPSock.sendto(str.encode(data),addr)
    if data == "done":
        break
UDPSock.close