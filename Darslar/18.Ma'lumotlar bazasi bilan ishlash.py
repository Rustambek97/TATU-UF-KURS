import mysql.connector

class Database:
    def __init__(self):
        self.db = self.ulanish()
        self.cursor = self.db.cursor()

    def ulanish(self):
        return mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Rustam123456b",
            database = "uquv_markaz"
        )

    def ishlatish(self, sql, fetchall=False, fetchone=False, commit=False):
        data = None
        if fetchall:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
        elif fetchone:
            self.cursor.execute(sql)
            data = self.cursor.fetchone()
        elif commit:
            self.db.commit()
        if data:
            return data


    def kurs_nomi(self, id):
        sql = f"SELECT kurs_nomi FROM kurslar WHERE id={id}"
        return self.ishlatish(sql, fetchone=True)

    def kurs_nomlari(self):
        sql = f"SELECT kurs_nomi FROM kurslar"
        return self.ishlatish(sql, fetchone=True)


mybase = Database()
kurs_nomi = mybase.kurs_nomi(3)
print(kurs_nomi)
kurs_nomlari = mybase.kurs_nomlari()
for i in kurs_nomlari:
    print(i)



