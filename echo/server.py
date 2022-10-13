import socket
import datetime

def zapis(text):
    log = open("logs.txt", "a")

    timee = datetime.datetime.now()
    log.write(str(timee) + ':' + text + "/n")
    log.close()

#запуск
sock = socket.socket()
zapis('Запустился')

#задаём порт
port = int(input('Port: '))

#проверяем порт и подключаемся
if not (port>=1025 and port<=65536):
    print("Out of diapozon")
    port = int(input('Port: '))
    print("Port:", port)
    sock.bind(('localhost', port))
else:
    print("Port:", port)
    sock.bind(('localhost', port))


while True:
    #прослушка
    sock.listen(1)
    zapis(f"Прослушивание порта № ({port})")

    #приняли сигнал и зафиксировали
    conn, addr = sock.accept()

    zapis(f"Соединение установлено {addr[0]}:{addr[1]}")

    #начинаем получать сообщения
    while True:
        #считываем 1024 байта
        data = conn.recv(1024).decode("utf8")
        print("got", data)

        #выход из соединения
        if  data == "exit":
            zapis(f"Соединение разорвано")
            break

        elif data == "stop":
            break#сначала выход из этого цикла а потом уже из глобального

        zapis(f"Передача выполнена: {data}")

        #отправляем клиенту
        data += ';'
        conn.send(data.encode())
        zapis(f"Обратная отправка: {data}")

    #совсем конец
    if data == "stop":
        break

zapis('Завершение соединения')
conn.close()
