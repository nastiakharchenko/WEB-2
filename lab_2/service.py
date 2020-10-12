from subprocess import Popen, CREATE_NEW_CONSOLE

process_list = [] #Сюда будут попадать все клиентские процессы
Popen('python server.py ', creationflags=CREATE_NEW_CONSOLE)    #Запускаем сервер

while True:
    user = input("Запускать 19 клиентов (start) / Закрыть клиентов (close) / Выйти (quit)")
    if user == 'quit':  #Если пользователь ввел quit, то останавливаем цикл
        break
    elif user == 'start':   #Если пользователь ввел start, то запускаем цикл
        for i in range(19):
            name = 'python client.py ' + 'Sur_' + str(i) + ' ' + str(i)
            process_list.append(Popen(name, creationflags=CREATE_NEW_CONSOLE))  #Открываем каждый процесс в новой консоли
        print('Запущено 19 клиентов')
    elif user == 'close':   #Если пользователь ввел close, то завершаем все процессы
        for process in process_list:
            process.kill()
        process_list.clear()    #Очищаем список