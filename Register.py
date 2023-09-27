def register():
    with open("C:/Users/HP/Desktop/students.txt", "a") as file:
        name = input("Введите ваше имя: ")
        surname = input("Введите вашу фамилию: ")
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        file.write(f"{login}:{password}\n")
        print("Регистрация прошла успешно!")


def login():
    login = input("Введите ваш логин: ")
    password = input("Введите ваш пароль: ")
    with open("C:/Users/HP/Desktop/students.txt", "r") as file:
        for line in file:
            saved_login, saved_password = line.strip().split(":")
            if saved_login == login and saved_password == password:
                print("Авторизация успешна!")
                return
    print("Неправильный логин или пароль. Попробуйте еще раз.")

while True:
    print("1. Регистрация")
    print("2. Авторизация")
    print("3. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Выход из программы.")
        break
    else:
        print("Неправильный выбор. Пожалуйста, выберите 1, 2 или 3.")
