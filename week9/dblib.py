import sqlite3

class GradeBookDatabase:

    def __init__(self, db_name="gradebook.db"):
        self.db_name = db_name 
        #veritabani ismini alir  ve sinifi baslatir

    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("""
            create table if not exists GradeBook (
                gid   integer primary key autoincrement,
                fname text,
                lname text,
                grade integer
            );
            """)
        conn.commit()
        conn.close()

    def fill_data(self):
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

        for item in data:
            cur.execute("insert into GradeBook(fname, lname, grade) values(?, ?, ?)", item)
            #values(?,?,?) means that we are going to insert 3 values (parametre yer tutucuları olarak kullanılır. Bu yer tutucular, gerçek kullanıcı verisinin sorguya yerleştirilmeden önce düzgün bir şekilde işlenmesini sağlar) 

        conn.commit()
        conn.close()

    def save_grade(self, fname, lname, grade):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("insert into GradeBook(fname, lname, grade) values(?, ?, ?)", (fname, lname, grade))
        conn.commit()
        conn.close()

    def get_grades(self):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("select * from GradeBook")
        grade_list = cur.fetchall() #fetchall() methodu, sorgudan dönen tüm satırları alır ve bir liste olarak döndürür.
        conn.close()

        return grade_list

    def get_count_and_average(self):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("select count(*), avg(grade) from GradeBook")
        result = cur.fetchone() #fetchone() methodu, sorgudan yalnızca bir satır alır ve bu satırı bir demet olarak döndürür.
        conn.close()

        return result

    def delete_grade(self, gid):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("delete from GradeBook where gid=?", (gid, ))
        # cur.execute("delete from GradeBook where gid=:gid", {"gid": gid})
        conn.commit()
        conn.close()

    def update_grade(self, gid, fname, lname, grade):
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("update GradeBook set fname=?, lname=?, grade=? where gid=?",
                    (fname, lname, grade, gid))
        conn.commit()
        conn.close()