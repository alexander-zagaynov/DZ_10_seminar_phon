from logger import input_data, print_data, put_data, delete_data


def interface():
    command = -1
    while command != 5:
        print('Доброго времени суток! Вы попали на специальную программу от нашей группы! Что же мы можем делать?\n'
              '1. Записать данные(в 2-ух форматах)\n'
              '2. Удалить данные\n'
              '3. Изменить данные\n'
              '4. Вывести данные\n'
              '5. Выход')
        command = int(input("Введите номер операции: "))

        while command < 1 or command > 5:
            print('Ты дурак?! Даю тебе последний шанс')
            command = int(input("Введите номер операции: "))

        if command == 1:
            input_data()
        elif command == 2:
            delete_data()
        elif command == 3:
            put_data()
        elif command == 4:
            print_data()
        elif command == 5:
            print("Спасибо, что воспользовались нашими услугами. Всего доброго!")





