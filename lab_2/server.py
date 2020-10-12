import select
from socket import socket, AF_INET, SOCK_STREAM
import xml.etree.ElementTree as ET
import pickle
from datetime import datetime
import time

#Функция чтения клиентских запросов
def clients_read(r_clients, clientlist):
    #Создаем XML-элементы для приема данных
    root = ET.Element('Root')
    surname = ET.SubElement(root,'Surname')
    id = ET.SubElement(root, 'ID')
    for sock in r_clients:
        try:
            #Получаем данные, десериализуем и заполняем XML-элементы:
            data = sock.recv(524288)
            data_pick = pickle.loads(data)
            surname.text = data_pick[0].text
            id.text = data_pick[0][0].text
        except:
            print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            clientlist.remove(sock)
    return root

#Функция ответов клиентам на их запросы
def clients_write(requests, w_clients, all_clients):
    for sock in w_clients:
            try:
                #Подготовить и отправить отчет сервера:
                data_pick = pickle.dumps(requests)
                sock.send(data_pick)
            except:
                #Сокет недоступен, клиент отключился:
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                sock.close()
                all_clients.remove(sock)

def mainserver():
    adress = ('localhost', 14900)
    clients = []
    client_adress = []
    sock = socket(AF_INET, SOCK_STREAM) #Создаем сокет (AF_INET - домен (протокол TCP/IP))
    sock.bind(adress)  #связываем сокет и наш хост
    sock.listen(5)  #запускаем режим прослушивания для сокета и выбираем максимальное количество подключение в очереди
    sock.settimeout(0.2)
    timer = 0
    start_timer_for_write = ''

    data = ET.Element('data')   #Создаем XML-элемент

    r = []; w = []
    while True:
        mark = 0    #Метка успешности
        try:
            conn,addr = sock.accept()  #Проверяем подключения
            if addr not in client_adress:   #Проверяем не было ли такого клиента
                client_adress.append(addr)  #Заполняем массив клиентов
                mark = 1    #Метка успешности (получили адресс от клиента)
                if len(client_adress) == 1: #При первом подключении
                    timer = datetime.now()  #запускаем таймер
                    start_timer_for_write = datetime.now().isoformat(" ", "seconds")    #Фиксируем время запуска таймера (для ответа клиентам)
            else:
                mark = 0    #Метка успешности (не получили адресс от клиента)
        except OSError as e:
            pass    #Таймаут вышел
        else:
            print("Получен запрос на соединение от %s" % str(addr))
            clients.append(conn)
        finally:
            #Проверяем наличие событий ввода-вывода:
            wait = 10
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass    #Ничего не делаем, если какой-то клиент отключился
            else:
                requests = clients_read(r, clients) #Принимаем запросы клиентов
                #Заполняем XML-элементы (вложенные) только в случае, если ранее такого клиента не было:
                if mark == 1:
                    start_timer = ET.SubElement(data, 'Start')
                    start_timer.text = start_timer_for_write
                    surname = ET.SubElement(data, 'Surname')
                    surname.text = requests[0].text
                    id_data = ET.SubElement(data, 'ID')
                    id_data.text = requests[1].text
                    time_conn = ET.SubElement(data, 'Time connection')
                    time_conn.text = datetime.now().isoformat(" ", "seconds")

                #Если уже подключилось 19 клиентов,
                if len(client_adress) == 19:
                    time.sleep(29 - (datetime.now() - timer).total_seconds())   #Запускаем таймер на 29 секунд
                    #то отправляем ответ клиентам:
                    clients_write(data, w, clients)
                    input('Press enter to end the process: ')
                    break

print('Server is RUN')
mainserver()