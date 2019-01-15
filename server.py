from socket import *
print("***********Welcome to my little server thing.It aint much but it's honest work*********")
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
    msg = "Message("+addr[0]+")" +":"+ data.decode()
    if not iplog.__contains__(addr[0]):
        iplog.append(addr[0])
    record.append(msg)
    print(msg)
    if data.decode() == "done":
        break
UDPSock.close()
print("All messages in last session: ")
[print(msg) for msg in record]
print("All ips that sent a message: ")
[print(ip) for ip in iplog]