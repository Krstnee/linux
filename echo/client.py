import socket
import logging # Модуль для ведения лог-файла


Log_Format = "%(levelname)s %(asctime)s - %(message)s" 

logging.basicConfig(filename = "clientlog.log",   
                    filemode = "w", 
                    format = Log_Format, 
                    level = logging.DEBUG)

logger = logging.getLogger()

sock = socket.socket()
sock.setblocking(1)

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname) 



print("Your Computer IP Address is :" + IPAddr)



while True:
	addrIP = str(input('Input IP address of echo-server\nor press enter to connect to default IP: '))
	if len(addrIP) == 0:
		try: sock.connect((IPAddr, 9000))
		except ConnectionRefusedError: print("Default address doesn't respond")
		else: break
	correct_check = addrIP.replace('.', '')
	correct_check = correct_check.replace(' ', '')
	for i in range(10): correct_check = correct_check.replace(str(i), '')
	if len(correct_check) != 0: print('There are excess symbols in your address, IP can contain only dots and digits')
	else:
		format = addrIP.split('.')
		if len(format) != 4: print('There are not 3 dots in your ip address')
		else:
			for i in range(4):
				if int(format[i]) > 255 or int(format[i]) < 0: 
					print('Incorrect IP address, nubers must be in between 0 and 255')
					break
			else:
				try:
					portNum = int(input('Input the port Number: '))
				except:
					print('Incorrect symbols, port number can contain only 4 digits')
				else:
					if portNum < 9999 and portNum > 1024:
						try: sock.connect((addrIP, portNum))
						except ConnectionRefusedError:	print('There in no server with that address and port')
						else: break
					else: print('incorrect diapozone')
                    



logger.info('connected to server')


print('Succsessfully connected! Press Enter to continue')
msg = ''
a = 0

#Обмен сообщениями с сервероm

while msg!= 'exit':

	msg = input()
# 	print()
	sock.send(msg.encode())
    
	if a != 0:logger.info('Message succsessfully sended')
	else: a = 1 
    
    
	data = sock.recv(1024)
    
	logger.info('You recieved a message!')
    
	print(data.decode()) 
# 	print()


logger.info('connection closed')
sock.close() 
