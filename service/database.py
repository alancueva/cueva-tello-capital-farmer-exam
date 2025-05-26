import sqlite3

# clase Database que maneja la conexión y operaciones con la base de datos SQLite
class Database:
    def __init__(self, db_name='database.db'):
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS cotizaciones (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    numero TEXT,
                    nombre TEXT,
                    email TEXT,
                    servicio TEXT,
                    precio INTEGER,
                    fecha TEXT
                )
            ''')
            conn.commit()

    def insertar_cotizacion(self, numero, nombre, email, servicio, precio, fecha):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO cotizaciones (numero, nombre, email, servicio, precio, fecha)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (numero, nombre, email, servicio, precio, fecha))
            conn.commit()
