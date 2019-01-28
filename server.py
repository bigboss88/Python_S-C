import socket
from socket import *
from protect import encrypt,decrypt
def send_log(log,addr):
	for msg in log:
		s = socket(AF_INET,SOCK_DGRAM)
		addr = (addr[0],14001)
		s.sendto(encrypt(msg).encode(),addr)
		print("Log was requested from: "+addr[0])

def main():
	print("***********Welcome to my little server thing.*********")
	host = ""
	port = 14000
	buf = 1024
	addr = (host,port)	
	UDPSock = socket(AF_INET,SOCK_DGRAM)
	UDPSock.bind(addr)
	print("Listening")
	record =[]
	iplog=[]
	while True:
		(data,addr) = UDPSock.recvfrom(buf)
		data = decrypt(data.decode())
		if data == "!@#$%^&*()":
			send_log(record,addr)
		else:
			msg = "Message("+addr[0]+")" +":"+ data
			if not iplog.__contains__(addr[0]):
				iplog.append(addr[0])
			record.append(msg)
			print(msg)
			for ip in iplog:
				s = socket(AF_INET,SOCK_DGRAM)
				addr = (ip,14001)
				en_data=encrypt(msg)
				s.sendto(en_data.encode(),addr)
			if data == "done":
				break
	UDPSock.close()
	print("All messages in last session: ")
	[print(msg) for msg in record]
	print("All ips that sent a message: ")
	[print(ip) for ip in iplog]
main()
