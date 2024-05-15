import sqlite3


def sql_connect():
    try:
        connection = sqlite3.connect("sqlite3.db")  # SQLite3 bazasiga bog'lanish
        connection.commit()
        return True
    except sqlite3.Error as e:
        print(e)
        return False


def sql_connection():
    connection = sqlite3.connect("sqlite3.db")  # SQLite3 bazasiga bog'lanish
    connection.commit()
    return connection

def user_(ab, ba, id):
    if sql_connect() == True:

        conn = sql_connection()
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {ab} WHERE {ba} = ?", (id,))

        res = cursor.fetchall()
        conn.commit()

        if not res:
            return False
        else:
            return True
    else:
        return False


# def user_info(message):
#     if sql_connect() == True:
#         if (user_(message) == False):

#             try:
#                 conn = sql_connection()
#                 cursor = conn.cursor()
#                 insert_query = """ INSERT INTO users (uid, full_name, username) VALUES (?, ?, ?) """

#                 cursor.execute(insert_query, (message.from_user.id, message.from_user.full_name, message.from_user.user_name))
#                 conn.commit()
#                 return True
#             except sqlite3.Error as e:
#                 print(e)
#                 return False
#         else:
#             return False
#     else:
#         return False


# def create_table():
#     if sql_connect() == True:
#         conn = sql_connection()
#         cursor = conn.cursor()
#         create_table = """ CREATE TABLE users (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 uid BIGINT NOT NULL,
#                 full_name TEXT NOT NULL,
#                 username TEXT
#             ); """
#         cursor.execute(create_table)
#         conn.commit()
#     else:
#         print("Bazaga ulanishda xatolik yuz berdi")

# def create_tablee():
#     if sql_connect() == True:
#         conn = sql_connection()
#         cursor = conn.cursor()
#         create_table = """ CREATE TABLE maxsulotlar (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 key BIGINT NOT NULL,
#                 kategoriya TEXT NOT NULL,
#                 nomi TEXT NOT NULL,
#                 info TEXT NOT NULL,
#                 soni BIGINT NOT NULL,
#                 narxi BIGINT NOT NULL,
#                 rasm TEXT NOT NULL
#             ); """
#         cursor.execute(create_table)
#         conn.commit()
#     else:
#         print("Bazaga ulanishda xatolik yuz berdi")
        
# create_tablee()


# def create_table():
#     if sql_connect() == True:
#         conn = sql_connection()
#         cursor = conn.cursor()
#         create_table = """ CREATE TABLE buyurtma (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 uid BIGINT NOT NULL,
#                 key BIGINT NOT NULL,
#                 kategoriya TEXT NOT NULL,
#                 nomi TEXT NOT NULL,
#                 info TEXT NOT NULL,
#                 soni BIGINT NOT NULL,
#                 narxi BIGINT NOT NULL,
#                 rasm TEXT NOT NULL,
#                 code INTEGER NOT NULL,
#                 viloyat TEXT NOT NULL,
#                 holat TEST NOT NULL
#             ); """
#         cursor.execute(create_table)
#         conn.commit()
#     else:
#         print("Bazaga ulanishda xatolik yuz berdi")
        

def create_table():
    if sql_connect() == True:
        conn = sql_connection()
        cursor = conn.cursor()
        create_table = """ CREATE TABLE savat (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                uid BIGINT NOT NULL,
                key BIGINT NOT NULL,
                kategoriya TEXT NOT NULL,
                nomi TEXT NOT NULL,
                info TEXT NOT NULL,
                soni BIGINT NOT NULL,
                narxi BIGINT NOT NULL,
                rasm TEXT NOT NULL
            ); """
        cursor.execute(create_table)
        conn.commit()
    else:
        print("Bazaga ulanishda xatolik yuz berdi")


# def create_table():
#     if sql_connect() == True:
#         conn = sql_connection()
#         cursor = conn.cursor()
#         create_table = """ CREATE TABLE phone (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 uid INTEGER NOT NULL,
#                 number INTEGER NOT NULL
#             ); """
#         cursor.execute(create_table)
#         conn.commit()
#     else:
#         print("Bazaga ulanishda xatolik yuz berdi")

def add_information(uid, full_name, username):
    if sql_connect() == True:
        try:
            conn = sql_connection()
            cursor = conn.cursor()

            cursor.execute(
                """INSERT INTO users (uid, full_name, username) VALUES (?, ?, ?)""",
                (uid, full_name, username),
            )
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
    else:
        return False


def info(id, v):
    if sql_connect() == True:
        conn = sql_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM users WHERE {v} = ?", (id,))

        res = cursor.fetchall()
        conn.commit()
        if not res:
            return False
        else:
            for i in res:
                return list(i)
    else:
        return False


def select_info(id):
    if sql_connect() == True:
        conn = sql_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {id}")

        res = cursor.fetchall()
        conn.commit()
        l = list()
        if not res:
            return False
        else:
            for i in res:
                l.append(i)
            return l
    else:
        return False


def delete_table(da, ta, keys):
    if sql_connect() == True:
        try:
            conn = sql_connection()
            cursor = conn.cursor()
            cursor.execute(f"delete from {da} where {ta} = ?", (keys,))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
    else:
        return False


def drop_table(keys):
    if sql_connect() == True:
        try:
            conn = sql_connection()
            cursor = conn.cursor()
            cursor.execute(f"drop table {keys}")
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
    else:
        return False


def add_categ(nom):
    if sql_connect() == True:
        try:
            conn = sql_connection()
            cursor = conn.cursor()

            cursor.execute(f"""INSERT INTO kategoriya (nomi) VALUES ('{nom}')""")
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
    else:
        return False


def add_maxsulots(key, kategoriya, nomi, info, soni, narxi, rasm):
    if sql_connect() == True:
        try:
            conn = sql_connection()
            cursor = conn.cursor()

            cursor.execute(
                """INSERT INTO maxsulotlar (key, kategoriya, nomi, info, soni, narxi, rasm) VALUES (?, ?, ?, ?, ?, ?, ?)""",
                ((key, kategoriya, nomi, info, soni, narxi, rasm)),
            )
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
    else:
        return False


def add_savat(uid, key, kategoriya, nomi, info, soni, narxi, rasm):
    if sql_connect() == True:
        try:
            conn = sql_connection()
            cursor = conn.cursor()

            cursor.execute(
                """INSERT INTO savat (uid, key, kategoriya, nomi, info, soni, narxi, rasm) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                ((uid, key, kategoriya, nomi, info, soni, narxi, rasm)),
            )
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
    else:
        return False


def add_buyurtma(uid, key, kategoriya, nomi, info, soni, narxi, rasm, code, viloyat, holat):
    if sql_connect() == True:
        try:
            conn = sql_connection()
            cursor = conn.cursor()

            cursor.execute(
                """INSERT INTO buyurtma (uid, key, kategoriya, nomi, info, soni, narxi, rasm, code, viloyat, holat) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                ((uid, key, kategoriya, nomi, info, soni, narxi, rasm, code, viloyat, holat)),
            )
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
    else:
        return False


def update_data(d1, d2, d3, key1, key2):

    if sql_connect() == True:
        try:
            conn = sql_connection()
            cursor = conn.cursor()

            cursor.execute(f"""UPDATE {d1} SET {d2} = "{key1}" WHERE {d3} = {key2};""")

            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
    else:
        return False


def table_info(ab, ba, id):
    if sql_connect() == True:

        conn = sql_connection()
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {ab} WHERE {ba} = ?", (id,))

        res = cursor.fetchall()
        conn.commit()

        if not res:
            return False
        else:
            return res
    else:
        return False