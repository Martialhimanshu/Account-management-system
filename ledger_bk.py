#04
import sqlite3
def create():
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS account(account_num TEXT PRIMARY KEY, name TEXT, password TEXT, money INTEGER)")
    con.commit()
    con.close()
  
def viewall(name):
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM account WHERE name={}".format(name))
    rows = cur.fetchall()
    con.close()
    return rows

# def search(name="",user="",password="",category=""):
#     con = sqlite3.connect("aledger.db")
#     cur = con.cursor()
#     cur.execute("SELECT * FROM account WHERE name=? OR user=? OR password=? OR category=?",(name,user,password,category))
#     rows = cur.fetchall()
#     con.close()
#     return rows

def add(account_num, name, password, money):
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("INSERT INTO account VALUES(?,?,?,?)",(account_num, name, password, money))
    con.commit()
    con.close()
    
#  def update(account_num,name,password):
#      con = sqlite3.connect("aledger.db")
#      cur = con.cursor()
#      cur.execute("UPDATE account SET account_num=?, name=?,password=?,money=?",(account_num,name,password,money))
#      con.commit()
#      con.close()

def delete(account_num):
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("DELETE FROM account WHERE account_num=?",(account_num,))
    con.commit()
    con.close()
    
def remittance(self,start_number, target_number, amount, password):
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("REMETTANCE from account=?, to account=?, money=?, password=?",(start_number, target_number, amount, password))
    con.commit()
    con.close()
create()
#print(search(category="social"))