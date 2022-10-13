import socket
import pickle

sock=socket.socket()

sock.bind(('', 4040))
sock.listen(1)
conn, addr=sock.accept()
#print(addr)
msg=b''
while True:
    data = conn.recv(10)
    if not data:
        break
    msg += data
#data=conn.recv(1024)
#print(data)

print(msg)
conn.send(msg)
conn.close()

