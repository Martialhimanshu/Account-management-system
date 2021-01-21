#04
import sqlite3
def create():#테이블 생성
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS account(account_num TEXT PRIMARY KEY, name TEXT, password TEXT, money INTEGER)")
    #account테이블 생성, account_num이 기본키
    con.commit()
    con.close()
  
def viewall():#DB에 있는 모든 데이터보기
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM account") #account테이블 안에 있는 모든 데이터 선택
    rows = cur.fetchall()#모든 데이터 보여주기
    con.close()
    return rows

def search(account_num="",name="",password=""):#매개변수로 들어온 값을 통해 원하는 데이터 찾기
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM account WHERE account_num=? AND name=? AND password=?",(account_num,name,password))
    #모든 데이터 중에서 매개변수로 받는 것과 모두 동일한 데이터 찾기
    rows = cur.fetchall()#모든 데이터 보여주기
    con.close()
    return rows

def add(account_num, name, password, money):#데이터 추가
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("INSERT INTO account VALUES(?,?,?,?)",(account_num, name, password, money))
    #매개변수로 들어온 값을 DB에 저장
    con.commit()
    con.close()

def update(name,account_num, money):#입금, 출금시 데이터 업데이트
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("UPDATE account SET money = '%d' WHERE name = '%s' AND account_num = '%s'" % (money, name, account_num))
    #매개변수로 들어온 값을 새롭게 DB에 저장
    con.commit()
    con.close()

def update2(account_num, money):#계좌이체시 데이터 업데이트
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("UPDATE account SET money = '%d' WHERE account_num = '%s'" % (money, account_num))
    #매개변수로 들어온 값을 새롭게 DB에 저장
    con.commit()
    con.close()  

def delete(account_num):#데이터 삭제
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("DELETE FROM account WHERE account_num=?",(account_num,))
    #매개변수로 들어온 값을 가진 데이터 삭제
    con.commit()
    con.close()
create()
#print(search(category="social"))