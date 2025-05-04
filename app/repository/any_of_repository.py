# repositories/abstract.py
import psycopg2
from abc import ABC, abstractmethod


class RepositoryABC(ABC):
    @abstractmethod
    def get_client(self):
        pass


class clientsRepository(RepositoryABC):
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="wg_forge_db",
            host="localhost",
            user="wg_forge",
            password="42a",
            port="5432"
        )
        self.cursor = self.conn.cursor()

    def get_client(self):
        try:
            self.cursor.execute("SELECT * FROM clients")
            return True if self.cursor.fetchone() else False
        except psycopg2.Error as e:
            print(f"Ошибка получения студента: {e}")
            return None

    def close(self):
        self.cursor.close()
        self.conn.close()