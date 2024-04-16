import os


FILE_NAME = 'users.txt'


def initialization_file() -> None:
    """Проверяет, существует ли файл, если нет, то создает его"""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', encoding='utf-8'):
            pass


def create_account(login: str, password: str) -> bool:
    """
    Создаем новый аккаунт

    Функция регистрирует в файле новый логин и пароль
    Args:
    login: str (содержит логин под которым пользователь может
                зарегистрироваться в системе)
    password: str (содержит пароль от логина)
    Return:
    bool: True - если регистрация прошла успешно,
          False - в обратном случае
    """
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        users = file.read().splitlines()

    for user in users:
        args = user.split(':')
        if login == args[0]:
            return False

    with open(FILE_NAME, 'a', encoding='utf-8') as file:
        file.write(f'{login}:{password}\n')
    return True


def check_account(login: str, password: str) -> bool:
    """
    Проверяем логин и пароль пользователя

    Функция проверяет наличие регистрации пользователя
    (присутствует ли введенный логин в файле FILE_NAME)
    Args:
    login: str (содержит логин под которым пользователь может войти в систему)
    password: str (содержит пароль от логина)
    bool: True - если данный пользователь зарегистрирован и присутствует
          в базе данных, False - в случае отсутствия данных о пользователе
    """
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        users = file.read().splitlines()

    for user in users:
        args = user.split(':')
        if login == args[0] and password == args[1]:
            return True
    return False


def main() -> None:
    """
    Главный цикл программы, который отсылает к другим функциям

    Данная функция запрашивает команды у пользователя, при вводе которых,
    пользователь может авторизироваться(1), зарегистрироваться(2),
    либо выйти из программы(3)
    Return: None
    """

    initialization_file()
    while True:
        print('''Добро пожаловать! Выберите пункт меню:
        1. Вход
        2. Регистрация
        3. Выход''')

        user_input = input()
        if user_input == '1':
            print('(логин должен содержать не менее'
                  ' 3 и не более 20 символов)')
            login = input('Введите логин: ')
            print('(пароль должен содержать не менее'
                  ' 4 и не более 32 символов)')
            password = input('Введите пароль: ')

            if check_account(login, password):
                print('Авторизация прошла успешно')
                break
            print('Ошибка! Пользователь не найден!')

        elif user_input == '2':
            print('(логин должен содержать не менее'
                  ' 3 и не более 20 символов)')
            login = input('Введите логин: ')
            if 3 > len(login) or len(login) > 20:
                print('Ошибка при регистрации, повторите попытку!')
                continue

            print('(пароль должен содержать не менее'
                  ' 4 и не более 32 символов)')
            password = input('Введите пароль: ')
            if 4 > len(password) or len(password) > 32:
                print('Ошибка при регистрации, повторите попытку!')
                continue

            password_repeat = input('Повторите пароль: ')

            if password != password_repeat:
                print('Пароли не совпадают!')
                continue

            if create_account(login, password):
                print('Регистрация прошла успешно!')
            else:
                print('Ошибка! Пользователь с данным'
                      ' аккаунтом уже существует!')

        elif user_input == '3':
            print('Завершение работы')
            break


if __name__ == '__main__':
    main()