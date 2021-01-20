#Simple account management system suitable for windows operationg system
# Copyright 2017 by Martial Himanshu.  All rights reserved.
# Distributed under the MPL license.  See LICENSE.txt for details.

from tkinter import *
import ledger_bk
window = Tk()
window.title("Account Ledger") # 프로그램 제목

#----------------------------------------------------------------------------------------------------------
# View All 버튼을 누르면 실행되는 view_command 함수 정의

def view_command():
    lb.delete(0,END)    # lb 리스트박스의 내용들을 화면에서 지운다
    for row in ledger_bk.viewall():
        lb.insert(END,row)

#----------------------------------------------------------------------------------------------------------
# Search 버튼을 누르면 실행되는 search_command 함수 정의

def search_command():
    lb.delete(0,END)
    for row in ledger_bk.search(name=name.get(),user=user.get(),password=password.get(),category=category.get()):
        lb.insert(END,row)

#----------------------------------------------------------------------------------------------------------
# Add 버튼을 누르면 실행되는 add_command 함수 정의

def add_command():
    ledger_bk.add(name.get(),user.get(),password.get(),category.get(),cdate.get())
    lb.delete(0,END)
    lb.insert(END,name.get(),user.get(),password.get(),category.get(),cdate.get())

#----------------------------------------------------------------------------------------------------------
# 

def get_selected_row(event):
    try:
        global selected_tuple
        index=lb.curselection()[0]
        selected_tuple = lb.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
        e5.delete(0,END)
        e5.insert(END,selected_tuple[5])
    except IndexError:
        pass

#----------------------------------------------------------------------------------------------------------
# Update 버튼을 누르면 실행되는 update_command 함수 정의

def update_command():
    ledger_bk.update(selected_tuple[0],name.get(),user.get(),password.get(),category.get(),cdate.get())
    view_command()

#----------------------------------------------------------------------------------------------------------
# Delete 버튼을 누르면 실행되는 delete_command 함수 정의

def delete_command():
    ledger_bk.delete(selected_tuple[0])
    view_command()
    #lb.delete(END,get_selected_row.selected_tuple)

#----------------------------------------------------------------------------------------------------------
# Clear All 버튼을 누르면 실행되는 clear_command 함수 정의

def clear_command():
    lb.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)

#----------------------------------------------------------------------------------------------------------
# 정보 입력창에서 각각 무슨 정보를 입력하는 창인지 알려주는 레이블을 그리드 이용해 화면에 놓기

l1 = Label(window,text="Name")
l1.grid(row=0,column=0,columnspan=2)

l2 = Label(window,text="Username/Email")
l2.grid(row=1,column=0,columnspan=2)

l3 = Label(window,text="Password")
l3.grid(row=2,column=0,columnspan=2)

l4 = Label(window,text="Category")
l4.grid(row=3,column=0,columnspan=2)

l5 = Label(window,text="Date")
l5.grid(row=4,column=0,columnspan=2)

#----------------------------------------------------------------------------------------------------------
# 정보 입력창에서 정보를 입력하는 엔트리(한줄만을 입력받는 입력창)를 그리드 이용해 화면에 놓기 

name=StringVar()
e1 = Entry(window,textvariable=name,width=50)
e1.grid(row=0,column=0,columnspan=10)

user=StringVar()
e2 = Entry(window,textvariable=user,width=50)
e2.grid(row=1,column=0,columnspan=10)

password=StringVar()
e3 = Entry(window,textvariable=password,width=50)
e3.grid(row=2,column=0,columnspan=10)

category=StringVar()
e4 = Entry(window,textvariable=category,width=50)
e4.grid(row=3,column=0,columnspan=10)

cdate=StringVar()
e5 = Entry(window,textvariable=cdate,width=50)
e5.grid(row=4,column=0,columnspan=10)

#----------------------------------------------------------------------------------------------------------
# 각각의 기능에 해당하는 버튼 만들고 그리드 이용해 화면에 놓기 

b1 = Button(window,text="Add",width=12,command=add_command)  # 크기 12, 버튼 누르면 add_command 함수 호출
b1.grid(row=5,column=0)

b2 = Button(window,text="Update",width=12,command=update_command) # 크기 12, 버튼 누르면 update_command 함수 호출
b2.grid(row=5,column=1)

b3 = Button(window,text="Search",width=12,command=search_command) # 크기 12, 버튼 누르면 search_command 함수 호출
b3.grid(row=5,column=2)

b4 = Button(window,text="View All",width=12,command=view_command) # 크기 12, 버튼 누르면 view_command 함수 호출
b4.grid(row=5,column=3)

b5 = Button(window,text="Delete",width=12,command=delete_command) # 크기 12, 버튼 누르면 delete_command 함수 호출
b5.grid(row=5,column=4)

b6 = Button(window,text="Cancel",width=12,command=window.destroy) # 크기 12, 버튼 누르면 destroy 함수(프로그램 종료하는 내장함수) 호출
b6.grid(row=5,column=5)

b7 = Button(window,text="Clear All",width=12,command=clear_command) # 크기 12, 버튼 누르면 clear_command 함수 호출
b7.grid(row=0,column=5)

#----------------------------------------------------------------------------------------------------------

lb=Listbox(window,height=20,width=94)  # lb라는 이름의 리스트박스를 세로 20줄, 가로 94글자가 보이게 생성
lb.grid(row=6,column=0,columnspan=6)   # lb 리스트박스를 그리드를 이용해 7번째 행 (첫번째 행이 0이므로 row = 6은 7번째 행)의 0번째 열에 배치 -> 6개의 열에 걸치도록 생성 (화면에 버튼이 6개가 나열되므로)

sb=Scrollbar(window)                   # sb라는 이름의 스크롤바를 생성
sb.grid(row=6,column=6,rowspan=6)      # sb 스크롤바를 그리드를 이용해 7번째 행의 7번째 열에 배치 (즉, lb 리스트박스의 바로 다음 열)

lb.configure(yscrollcommand=sb.set)    # lb 리스트박스 내에서 위아래로 이동하면 sb 스크롤바가 같이 움직이도록 연동
sb.configure(command=lb.yview)         # sb 스크롤바를 움직이면 lb 리스트박스가 같이 움직이도록 연동

lb.bind('<<ListboxSelect>>',get_selected_row)
window.mainloop()                      # 프로그램 열기
