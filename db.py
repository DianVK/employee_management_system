import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS employees(
            id Integer Primary Key,
            name text,
            age text,
            doj text,
            email text,
            gender text,
            contact text,
            address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name, age, doj, email,gender,contact,address):
        sql = "insert into employees values(NULL,?,?,?,?,?,?,?)"
        self.cur.execute(sql,(name, age, doj, email,gender,contact,address))
        self.con.commit()


o = Database("Employee.db")
o.insert("Peter","25","05-10-2022","peter_grigorov@gmail.com","Male","+359892407444","Oborishte 8, Plovdiv")
o.insert("John","27","08-4-2023","this_is_test_email@gmail.com","Male","+359883457841","Mariya Luiza 103, Sofia")
