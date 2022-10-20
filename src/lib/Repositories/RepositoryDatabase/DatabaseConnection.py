import os
import sqlite3
from sqlite3 import Error

class DatabaseConnection:

    DB_PATH = r"/db/tech_challenge.db"

    def __init__(self):
        """ Create a database connection to a SQLite database """
        self.__conn = None
        try:
            self.__conn = sqlite3.connect(os.getcwd() + self.DB_PATH)
        except Error as e:
            print(e)
            self.__conn.close()

    def updateMultipleRows(self, query, rowData):
        self.__conn.row_factory = sqlite3.Row
        cur = self.__conn.cursor()
        for row in rowData:
            cur.execute(query, row)

        self.__conn.commit()
