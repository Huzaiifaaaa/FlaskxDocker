import sqlite3
import io
import os
from datetime import date


class Database():
    def __init__(self, DATABASE_PATH):
        self.DATABASE_PATH=DATABASE_PATH
        self.conn = sqlite3.connect(self.DATABASE_PATH,check_same_thread=False)
        self.cursor = self.conn.cursor()

        self.createUsersTable(self.conn)

    def createUsersTable(self,conn):
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                userid TEXT NOT NULL,
                question1 TEXT NOT NULL,
                question2 TEXT NOT NULL,
                question3 TEXT NOT NULL,
                response TEXT NOT NULL
            )
        ''')
        conn.commit()

    def insertUser(self,userid,question1,question2,question3,response):
        self.cursor.execute('''
            INSERT INTO Users (userid, question1, question2, question3, response)
            VALUES (?,?,?,?,?)
        ''', (userid, question1, question2, question3, response))
        self.conn.commit()

    def getUsers(self,id):
        self.cursor.execute('''
            SELECT * FROM Users WHERE id=?
        ''', (id,))
        row=self.cursor.fetchone()
        return row
    
    def getIDbyResponse(self,response):
        #select maximum id from Users where response is equal to response
        self.cursor.execute('''
            SELECT MAX(id) FROM Users WHERE response=?
        ''', (response,))
        row=self.cursor.fetchone()
        return row[0]
    

    

