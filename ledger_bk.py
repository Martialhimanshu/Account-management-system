#04
import sqlite3
def create():
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS account(account_num TEXT PRIMARY KEY, name TEXT, password TEXT, money INTEGER)")
    con.commit()
    con.close()
  
def viewall():
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM account")
    rows = cur.fetchall()
    con.close()
    return rows

#def search(name="",user="",password="",category=""):
#    con = sqlite3.connect("aledger.db")
#    cur = con.cursor()
#    cur.execute("SELECT * FROM account WHERE name=? OR user=? OR password=? OR category=?",(name,user,password,category))
#    rows = cur.fetchall()
#    con.close()
#    return rows

def search(account_num="",name="",password=""):
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM account WHERE account_num=? AND name=? AND password=?",(account_num,name,password))
    rows = cur.fetchall()
    con.close()
    return rows

def add(account_num, name, password, money):
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("INSERT INTO account VALUES(?,?,?,?)",(account_num, name, password, money))
    con.commit()
    con.close()
    
#def update(account,name,password,money):
    #con = sqlite3.connect("aledger.db")
    #cur = con.cursor()
    #cur.execute("UPDATE account SET account_num=?, name=?,password=?,money=?",(account_num, name, password, money))
    #con.commit()
    #con.close()

def update(name,account_num, money):
   con = sqlite3.connect("aledger.db")
   cur = con.cursor()
   cur.execute("UPDATE account SET money = '%d' WHERE name = '%s' AND account_num = '%s'" % (money, name, account_num))
   con.commit()
   con.close()

def delete(account_num):
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("DELETE FROM account WHERE account_num=?",(account_num,))
    con.commit()
    con.close()
create()
#print(search(category="social"))