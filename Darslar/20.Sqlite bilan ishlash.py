import sqlite3

class Database_sqlite:
    def __init__(self, path="sqlite.db"):
        self.path = path

    def ulanish(self):
        return sqlite3.connect(self.path)

    def execute(self, sql:str, fetchone=False, fetchall=False, commit=False):
        db = self.ulanish()
        cursor = db.cursor()
        cursor.execute(sql)
        data = None

        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        if commit:
            db.commit()
        db.close()
        return data

    def uquvchi_id(self, ism, familiya):
        sql = f"select id from uquvchilar where ism='{ism}' and familiya='{familiya}'"
        return self.execute(sql, fetchone=True)

obj = Database_sqlite()
print(obj.uquvchi_id("Alisher", "Yangiboyev"))