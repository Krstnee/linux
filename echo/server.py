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
conn.close()import socket
import logging # Модуль для ведения лог-файла

# =============================================================================
""" Заготовки для лог файла"""
# =============================================================================
Log_Format = "%(levelname)s %(asctime)s - %(message)s" # Формат лог-файла Уровень предупреджения -> Время предупреждения -> Предупреждение

logging.basicConfig(filename = "Serverlog.log",    # Название лог файла
                    filemode = "w", # Ставим файл на запись
                    format = Log_Format, # Подставляем формат лога сюда
                    level = logging.DEBUG) # Ставим уровень отображаемых сообщений на минимальный

logger = logging.getLogger() # Инициируем логгер. Все упоминания logger дальше - внесение записей в log файл

sock = socket.socket()
sock.setblocking(1)

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname) # Получаем свой айпишник - для дефолтного адреса IP

# =============================================================================


# =============================================================================
""" Сбор информации об IP адресе и порте. Открытие сервера """
# =============================================================================

print("Your Computer IP Address is :" + IPAddr)

a = "Your Computer Name is :" + hostname
logger.info(a)

a = "Your Computer IP Address is :" + IPAddr
logger.info(a)
logger.info('server started')
greet = 'Hello '
sock = socket.socket()
portNum = 9000 # Я взял за родной порт - 9000


while True: # Если порт 9000 занят - пробуем открыть на следующем порту, пока не получится

	try: sock.bind(('', portNum))
	except:	portNum += 1
	else: break

print(a)
a = 'Server is opened on port: ' + str(portNum) 
print(a)
logger.info(a) # Итоговое значение порта выводится в лог и в консоль

# =============================================================================

users = {'key':'info'} # Словарь известных нам пользователей(Пара IP и никнейм) для авторизации
c = 0

# =============================================================================
""" Обмен сообщениями """
# =============================================================================
while c < 5: # Выставил цикл обмена продолжительностью 5 отдельных соединений
# =============================================================================
	""" Ожидание пользователя """
# =============================================================================
	logger.info('Looking for connection...')
	sock.listen()
	conn, addr = sock.accept()
	print('connected ',addr[0])
	curr = list(users.keys()) 
	uzvers = str("Connected by " + str(addr[0]))
	logger.info(uzvers)
# =============================================================================

# =============================================================================
	""" Проверяем пользователя - знаком или нет """
# =============================================================================
	for i in range(len(curr)): # Если находим пользователя в списке - приветствуем его
		if str(curr[i]) == str(addr[0]):
			greet1 = greet + users[addr[0]] + '!'
			conn.send(bytes(greet1, encoding = 'utf-8'))
			break 
	else: # Иначе запрашиваем никнейм
		logger.info('nickname requested')
		conn.send(b'Hello, stranger! Input your username')
		sock.listen(0)
		Username = ''
		while Username == '':
			data = conn.recv(1024)
			if not data:
				None
			else:
				Username = str(data)
				Username = Username.replace("'", "")
				Username = Username.replace('b', '', 1)
				print(Username)
				users[addr[0]] = Username # Добавляем нового пользователя в список известных
				uzname = 'User entered nickname' + str(Username)
				logger.info(uzname)
				conn.send(b'Nice to meet you and welcome to server!')
				print(users)
				break
# =============================================================================

# =============================================================================
	""" Обмен сообщениями с пользователем """
# =============================================================================            
	sock.listen(0)
	msg = ''
	while msg != 'exit':
		msg = ''
		msg = users[addr[0]] + ': ' # Начало ответного сообщения - Никнейм пользователя + ":"
		data = conn.recv(1024)
		uzver = 'Recieved message: "' + str(data.decode()) + '" by ' + str(users[addr[0]]) 
		logger.info(uzver)
		if not data:
			break
		msg += data.decode()
		data2 = bytes(msg, encoding = 'utf-8')
		print(msg)
		conn.send(data2)
		logger.info('Message sent to this user!')

	conn.close()
	c += 1
	logger.info('Connection closed')
# =============================================================================
logger.info('Server closed')

