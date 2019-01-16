from socket import *
def encrypt(string):
	out =[]
	[out.append(chr(ord(c)+12)) for c in string]
	return "".join(out)

def main():
	target = input("Enter target ip addr: ")
	port = 14000
	addr = (target,port)
	UDPSock = socket(AF_INET,SOCK_DGRAM)
	key = "Aggnog"
	while True:
		data = input("Enter Message to send!: ")
		data = encrypt(data)
		UDPSock.sendto(data.encode(),addr)
		if data == "done":
			break
	sUDPSock.close

main()

