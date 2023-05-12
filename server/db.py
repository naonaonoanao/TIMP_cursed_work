import sqlite3
import random


def add_new_member(name, email, number, photo, roles, interests, departament):
    _sqlite_connection = sqlite3.connect('sqlite_python.db')
    print("Соединение с базой данных установлено!")
    sqlite_create_table_query = f'''INSERT INTO MEMBERS (id,name,email,number,photo,interests,roles,departament)
                                   VALUES ({random.randint(0, 10000000)},'{name}','{email}','{number}','{photo}','{interests}','{roles}','{departament}');'''

    cursor = _sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    cursor.execute(sqlite_create_table_query)
    _sqlite_connection.commit()
    print("Запись создана!")
    cursor.close()
    _sqlite_connection.close()
    print("Соединение с SQLite закрыто")


def create_db(_sqlite_connection):
    sqlite_create_table_query = '''CREATE TABLE MEMBERS (
                                    id int NOT NULL,
                                    name TEXT NOT NULL,
                                    email text NOT NULL,
                                    number text NOT NULL,
                                    photo text NOT NULL,
                                    interests text NOT NULL,
                                    roles text NOT NULL,
                                    departament text NOT NULL);'''

    cursor = _sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    print("Таблица SQLite создана")
    cursor.close()


def string_to_map(data):
    new_data = []
    for user in data:
        new_data.append({
            "name": user[1],
            "email": user[2],
            "number": user[3],
            "photo": user[4],
            "interests": user[5],
            "roles": user[6],
            "departament": user[7]
        })

    return new_data


def get_all():
    _sqlite_connection = sqlite3.connect('sqlite_python.db')
    print("Соединение с базой данных установлено!")
    sqlite_create_table_query = '''SELECT * FROM MEMBERS;'''
    cursor = _sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    cursor.execute(sqlite_create_table_query)
    data = cursor.fetchall()
    print(data)
    print("Таблица SQLite создана")
    cursor.close()
    _sqlite_connection.close()
    print("Соединение с SQLite закрыто")
    return data


def find_same_users(key):
    data = get_all()
    same_users = []

    for user in data:
        for field in user:
            if key in str(field):
                same_users.append(user)
                break

    return same_users


def delete_all():
    _sqlite_connection = sqlite3.connect('sqlite_python.db')
    print("Соединение с базой данных установлено!")
    sqlite_create_table_query = '''DELETE FROM MEMBERS;'''
    cursor = _sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    cursor.execute(sqlite_create_table_query)
    print("Удаление успешно!")
    _sqlite_connection.commit()
    cursor.close()
    _sqlite_connection.close()
    print("Соединение с SQLite закрыто")


if __name__ == "__main__":
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        create_db(sqlite_connection)
        # add_new_member(sqlite_connection, "Hagrid Amoralov", "222@d.c", "8-800-555-35-35", "url to photo", "Dev","Dota 2, Poland")
        # get_all()
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
