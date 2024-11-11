import sqlite3 # sqlite3 modülünü, SQLite veritabanı ile çalışmak için import eder.

class GradeBookDatabase:

    def __init__(self, db_name="gradebook.db"):
        self.db_name = db_name

    def create_table(self): # Veritabanında "GradeBook" adlı bir tablo oluşturur.
        conn = sqlite3.connect(self.db_name) #veritabanina baglanti kurar
        cur = conn.cursor()# Veritabanı üzerinde işlem yapmak için bir cursor (işlem yöneticisi) oluşturur.
        cur.execute("""
            create table if not exists GradeBook (
                gid   integer primary key autoincrement, #otomatik artan id
                fname text,
                lname text,
                grade integer
            );
            """)
        conn.commit() # Yapılan değişiklikleri veritabanına kaydeder.
        conn.close()# Veritabanı bağlantısını kapatır.

    def fill_data(self): # Veritabanına bazı başlangıç verilerini ekler.
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        data = [('Melissa', 'Bishop', 70),
                ('Linda', 'Scanlon', 55),
                ('Russel', 'Gruver', 60),
                ('Maria', 'Mayes', 100),
                ('Dennis', 'Hill', 95),
                ('Nathan', 'Martin', 40),
                ('William', 'Biggs', 85),
                ('Lois', 'Ballard', 60),
                ('Larry', 'Manning', 50),
                ('Dustin', 'Smalls', 30),
                ('Alice', 'Lucas', 70),
                ('John', 'Howell', 90)]

        for item in data: # Veritabanına her bir veriyi ekler.
            cur.execute("insert into GradeBook(fname, lname, grade) values(?, ?, ?)", item)

        conn.commit()
        conn.close()

    def save_grade(self, fname, lname, grade): # Yeni bir öğrenci notu veritabanına kaydeder
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("insert into GradeBook(fname, lname, grade) values(?, ?, ?)", (fname, lname, grade)) # Veritabanına verilen isim, soyisim ve notu ekler.
        conn.commit()
        conn.close()

    def get_grades(self): # Veritabanındaki tüm öğrenci notlarını getirir.
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor() # Veritabanı üzerinde işlem yapmak için bir cursor (işlem yöneticisi) oluşturur.
        cur.execute("select * from GradeBook")# "GradeBook" tablosundaki tüm verileri çeker.
        grade_list = cur.fetchall()# Çekilen tüm verileri bir liste olarak alır.
        conn.close()

        return grade_list #tum ogrenci notlarini dondurur

    def get_count_and_average(self): # Veritabanındaki notların sayısını ve ortalamasını getirir.
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("select count(*), avg(grade) from GradeBook")
        result = cur.fetchone()
        conn.close()

        return result

    def delete_grade(self, gid): # Veritabanındaki belirli bir öğrencinin notunu siler.
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("delete from GradeBook where gid=?", (gid, )) # "gid" (öğrenci ID) ile eşleşen satırı siler.
        # cur.execute("delete from GradeBook where gid=:gid", {"gid": gid})
        conn.commit()
        conn.close()
