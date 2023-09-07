import socket as s

HOST= 'localhost'
PORT= 2424
sck=s.socket(s.AF_INET,s.SOCK_STREAM)
sck.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR,1)
sck.bind((HOST,PORT))

print("Connection waiting")

sck.listen()
conn,addr=sck.accept()
print("Connection from {}:{}".format(addr[0],addr[1]))
conn.sendall("Hi buddy lets talk".encode())
data = conn.recv(1024)

while data:
    print(data.decode(),end="")
    data=conn.recv(1024)


