import os
import base64
import sqlite3
import hashlib

from rsa import PublicKey, encrypt


class KeeSafe():
    def __init__(self):
        self.__connection = None
        self.passwords_file = None
        

    def create_master_key(self, master_key):
        conn = self.connect_db()
        c = conn.cursor()

        salt = os.urandom(32)
        hashed_mp = hashlib.pbkdf2_hmac('sha256', master_key.encode(), salt, 100000)
        storage = salt + hashed_mp

        c.execute("INSERT INTO pm (mp) VALUES (?)", (storage,))
        conn.commit()


    def get_master_key(self):
        conn = self.connect_db()
        c = conn.cursor()

        c.execute("SELECT mp FROM pm")
        return c.fetchone()


    def connect_db(self):
        if self.__connection is None:
            self.__connection = sqlite3.connect(
                "database.db",
                check_same_thread=False
            )
        return self.__connection


    def create_tables(self):
        conn = self.connect_db()
        c = conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS pm(
                id     INTEGER PRIMARY KEY AUTOINCREMENT,
                mp  TEXT
            )
        ''')

        c.execute('''CREATE TABLE IF NOT EXISTS data(
                id     INTEGER PRIMARY KEY AUTOINCREMENT,
                name    VARCHAR(255),
                login   VARCHAR(255),
                password    BLOB,
                url     VARCHAR(255)
            )
        ''')

        conn.commit()

    
    def add_new_data(self, name, login, password, url):
        conn = self.connect_db()
        c = conn.cursor()

        with open("public.pem", 'r') as f:
            publicKey = PublicKey.load_pkcs1(f.read().encode())

        password = encrypt(password.encode(), publicKey)
        password = base64.b64encode(password)

        c.execute("INSERT INTO data (name, login, password, url) VALUES (?, ?, ?, ?)", (name, login, password, url,))
        conn.commit()


    def show_all_data(self):
        conn = self.connect_db()
        c = conn.cursor()

        c.execute("SELECT * FROM data")
        data = c.fetchall()
        return data


    def edit_data(self, name, login, password, url, row_id):
        conn = self.connect_db()
        c = conn.cursor()

        with open("public.pem", 'r') as f:
            publicKey = PublicKey.load_pkcs1(f.read().encode())

        password = encrypt(password.encode("utf-8"), publicKey)
        password = base64.b64encode(password).decode()

        c.execute("UPDATE data SET name = ?, login = ?, password = ?, url = ? WHERE id = ?", (name, login, password, url, row_id,))
        conn.commit()

    
    def delete_data(self, name):
        conn = self.connect_db()
        c = conn.cursor()

        c.execute("DELETE FROM data WHERE name = ?", (name,))
        conn.commit()

    
    def check_data(self, name):
        conn = self.connect_db()
        c = conn.cursor()

        c.execute("SELECT login, password, url FROM data WHERE name = ?", (name,))
        data = c.fetchall()
        return data


    def get_row_id(self, name):
        conn = self.connect_db()
        c = conn.cursor()

        c.execute("SELECT id FROM data WHERE name = ?", (name,))
        data = c.fetchone()
        return data