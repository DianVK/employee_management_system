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

    # Fetch all Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from employees")
        rows = self.cur.fetchall()
        #print(rows)
        return rows

    # Delete a Record in DB
    def remove(self,id):
        self.cur.execute("delete from employees where id=?",(id,))
        self.con.commit()

    # Update a Record in DB
    def update(self,id,name, age, doj, email,gender,contact,address):
        self.cur.execute("update employees set name=?,age=?,doj=?,email=?,gender=?,contact=?,address=? where id=?",
                         (name, age, doj, email,gender,contact,address,id))
        self.con.commit()


o = Database("Employee.db")
o.update("2","Ivan Asenov","35","12-12-2025","ivanasenov@abv.bg","Male","0897720760","Test Address")
