from socket import *
from sys import argv
import xml.etree.ElementTree as ET
import pickle

PLACE = ('localhost', 14900)

def client(data):
    with socket(AF_INET, SOCK_STREAM) as sock:  #Создаем сокет TCP
        sock.connect(PLACE) #Коненктимся с сервером
        sock.send(data) #Отправляем, кодировав в байты
        while True:
            data_sock = sock.recv(524288)
            data_pick = pickle.loads(data_sock) #десериализуем данные
            #Выводим на экран данные 19 клиентов:
            print('All attributes: ')
            i = 0
            while i != 72:
                print('Timer start time: ', data_pick[i].text, '\tSurname: ', data_pick[i + 1].text, '\tID: ', data_pick[i + 2].text, '\tClient connection time: ', data_pick[i + 3].text, '\n')
                i += 4

#Формируем XML-документы для отправки серверу:
fl_py, sur_user, id_user = argv
data = ET.Element('data')
surname = ET.SubElement(data, 'Surname')
id_data = ET.SubElement(surname, 'ID')
surname.text = sur_user
id_data.text = id_user
pick = pickle.dumps(data)   #сериализируем данные для отправки на сервер

if __name__ == '__main__':
    client(pick)