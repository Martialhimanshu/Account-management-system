import sqlite3
def create():
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS account(id INTEGER PRIMARY KEY,name TEXT,user TEXT, password TEXT,category TEXT,cdate TEXT)")
    con.commit()
    con.close()
def viewall():
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM account")
    rows = cur.fetchall()
    con.close()
    return rows

def search(name="",user="",password="",category=""):
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM account WHERE name=? OR user=? OR password=? OR category=?",(name,user,password,category))
    rows = cur.fetchall()
    con.close()
    return rows
def add(name,user,password,category,cdate):
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("INSERT INTO account VALUES(NULL,?,?,?,?,?)",(name,user,password,category,cdate))
    con.commit()
    con.close()
def update(id,name,user,password,category,cdate):
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("UPDATE account SET name=?,user=?,password=?,category=?,cdate=? WHERE id=?",(name,user,password,category,cdate,id))
    con.commit()
    con.close()
def delete(id):
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("DELETE FROM account WHERE id=?",(id,))
    con.commit()
    con.close()
create()
#print(search(category="social"))
