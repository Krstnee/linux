import socket

sock = socket.socket()
#узнаём куда подключаться
server = input('IP: ')
port = int(input('Port: '))

#устанавливаем соединение
sock.connect((server, port))

#отправка
while True:
	#что отправлять
	sms = input("Message ")

	result = sock.send(sms.encode())

	#полученное обратно
	data = sock.recv(1024).decode("utf8")
	print("got_back", data)

	if data.lower() == 'stop;' or data.lower() == 'exit;':
		sock.close()

sock.close()
