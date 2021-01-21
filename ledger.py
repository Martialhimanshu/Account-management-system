#Simple account management system suitable for windows operationg system
# Copyright 2017 by Martial Himanshu.  All rights reserved.
# Distributed under the MPL license.  See LICENSE.txt for details.

import tkinter.messagebox as msgbox # 메세지박스를 msgbox라는 이름으로 가져옴
from tkinter import * #tkinter밑에있는 모든 정보 가져옴
import ledger_bk #ledger_bk 정보 가져옴
import datetime # datetime 정보 가져옴
import random # random 정보 가져옴
window = Tk() #윈도우 창 생성
window.title("계좌 관리 프로그램") #윈도우 창 타이틀

def rand_accnum() : # 랜덤한 계좌번호를 문자열로 생성해서 리턴 하는 함수
    accnum_list = []
    acc_num = ""

    for i in range(16) :
        accnum_list.append(random.randint(0, 9))#0부터 9사이로 된 숫자가 랜덤으로 입력 
    accnum_list[6] = '-'#7번째 자리에 '-'입력
    accnum_list[9] = '-'#10번째 자리에 '-'입력

    for j in range(16):
        acc_num += str(accnum_list[j])#acc_num에 str로 하나씩 저장
    return acc_num

def view_command(): # 이름을 입력해 해당 이름으로 등록된 계좌들을 검색하는 함수
    #lb=Listbox(window,height=20,width=94) (111번 줄에 정의)
    lb.delete(0,END) #0항목부터 END까지 삭제
    for row in ledger_bk.viewall(): #ledger_bk파일에 있는 viewall()함수 이용
        if name.get() in row : # 입력한 이름으로 등록된 계좌 찾기
            lb.insert(END,row) #lb(리스트박스) 끝에서부터 하나씩 DB에 있는 정보 하나씩 기입

def add_command():
    # 정보 입력 시 빈칸이 있으면 에러 발생하고 저장 x
    if name.get() == "" or password.get() == "" or money.get() == "" :
        msgbox.showerror("에러", "정보 칸을 모두 입력해주세요!")#에러 발생
        return -1

    acc_number = rand_accnum()
    ledger_bk.add(acc_number, name.get(), password.get(), money.get())#ledger_bk파일에 있는 add()함수 이용
    lb.delete(0,END) #0항목부터 END까지 삭제
    lb.insert(END,"이름 : " + name.get(),"계좌번호 : " + acc_number, "패스워드 : " + "*" * len(password.get()),"계좌잔고 : " + money.get(), "계좌 개설 시간 : " + datetime.datetime.now().strftime('%Y년 %m월 %d일 %H시 %M분 %S초'))
    #lb에 ledger_bk파일에 있는 add()함수에서 받아온 정보와 계좌번호, 그리고 계좌를 생성한 시간을 화면에 출력

def get_selected_row(event):
    try:
        global selected_tuple #전역 변수
        index=lb.curselection()[0] #curselection() 선택된 항목들을 반환
        selected_tuple = lb.get(index) #selected_tuple에 lb에 있는 index 항목 반환
        
        e1.delete(0,END)#성명
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)#계좌번호
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)#비밀번호
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)#금액
        e4.insert(END,selected_tuple[4])
        e5.delete(0,END)#start_account 
        e5.insert(END,selected_tuple[5])
        e6.delete(0,END)#target_account
        e6.insert(END,selected_tuple[5])
        
    except IndexError:
        pass

def deposit_command():#입금
    a = ledger_bk.search(account_num.get(), name.get(), password.get())#Entry에서 받아옴
    b = int(a[0][3]) + int(money.get())#DB에 있는 계좌 잔액과 Entry에서 받아온 금액 합산
    ledger_bk.update(name.get(),account_num.get(),b)#합산된 금액 업데이트
    lb.delete(0,END)
    lb.insert(END,"입금이 완료되었습니다.")
    #view_command()

def withdraw_command():#출금
    c = ledger_bk.search(account_num.get(), name.get(), password.get())#Entry에서 받아옴
    d = int(c[0][3])
    if (d >= int(money.get())):#DB에 있는 계좌 잔액이 Entry에서 받아온 금액보다 큰 경우
        e = int(c[0][3]) - int(money.get())#DB에 있는 계좌 잔액에서 Entry에서 받아온 금액 차감
        ledger_bk.update(name.get(), account_num.get(),e)#차감된 금액 업데이트
        lb.delete(0,END)
        lb.insert(END,"출금이 완료되었습니다.")
    else :#DB에 있는 계좌 잔액이 Entry에서 받아온 금액보다 작을 경우
        lb.delete(0,END)
        msgbox.showerror("에러", "금액이 부족하여 출금할 수 없습니다.")#에러 발생
    #view_command()

def remittance_command():#계좌이체
    for aa in ledger_bk.viewall(): #ledger_bk파일에 있는 viewall()함수 이용
        if start_account.get() in aa : # 입력한 이름으로 등록된 계좌 찾기
            star = aa

    for bb in ledger_bk.viewall(): #ledger_bk파일에 있는 viewall()함수 이용
        if target_account.get() in bb : # 입력한 이름으로 등록된 계좌 찾기
            targe = bb
    
    start_acc = star[3] - int(money.get())
    ledger_bk.update2(start_account.get(), start_acc)#차감된 금액 업데이트
    target_acc = targe[3] + int(money.get())
    ledger_bk.update2(target_account.get(), target_acc)#추가된 금액 업데이트
    lb.delete(0,END)
    lb.insert(END,"계좌이체가 완료되었습니다.")

def delete_command():#데이터 삭제
    ledger_bk.delete(selected_tuple[0])
    view_command()
    #lb.delete(END,get_selected_row.selected_tuple)

def clear_command():
    lb.delete(0,END) #0항목부터 END까지 삭제
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)

#Label
l1 = Label(window,text="성명")
l1.grid(row=0,column=0,columnspan=2)
l2 = Label(window,text="계좌번호")
l2.grid(row=1,column=0,columnspan=2)
l3 = Label(window,text="비밀번호")
l3.grid(row=2,column=0,columnspan=2)
l4 = Label(window,text="금액")
l4.grid(row=3,column=0,columnspan=2)
l5 = Label(window,text="start_account")
l5.grid(row=4,column=0,columnspan=2)
l6 = Label(window,text="target_account")
l6.grid(row=5,column=0,columnspan=2)

#Entry
name=StringVar()
e1 = Entry(window,textvariable=name,width=50)
e1.grid(row=0,column=0,columnspan=10)

account_num=StringVar()
e2 = Entry(window,textvariable=account_num,width=50)
e2.grid(row=1,column=0,columnspan=10)

password=StringVar()
e3 = Entry(window,textvariable=password,width=50)
e3.grid(row=2,column=0,columnspan=10)

money=StringVar()
e4 = Entry(window,textvariable=money,width=50)
e4.grid(row=3,column=0,columnspan=10)

start_account=StringVar()
e5 = Entry(window,textvariable=start_account,width=50)
e5.grid(row=4,column=0,columnspan=10)

target_account=StringVar()
e6 = Entry(window, textvariable=target_account, width=50)
e6.grid(row=5, column=0, columnspan=10)

#Button
b1 = Button(window,text="계좌생성",width=12,command=add_command)
b1.grid(row=6,column=0)

b2 = Button(window,text="계좌폐기",width=12,command=delete_command)
b2.grid(row=6,column=1)

b3 = Button(window,text="계좌검색",width=12,command=view_command)
b3.grid(row=6,column=2)

b4 = Button(window,text="입금",width=12,command=deposit_command)
b4.grid(row=6,column=3)

b5 = Button(window,text="출금",width=12,command=withdraw_command)
b5.grid(row=6,column=4)

b6 = Button(window,text="계좌이체",width=12, command=remittance_command)
b6.grid(row=6,column=5)

b7 = Button(window,text="초기화",width=12,command=clear_command)
b7.grid(row=0,column=5)

b8 = Button(window,text="나가기",width=12,command=window.destroy)
b8.grid(row=6,column=6)

#Listbox
lb=Listbox(window,height=20,width=100)
lb.grid(row=7,column=0,columnspan=6)

#Scrollbar
sb=Scrollbar(window)
sb.grid(row=7,column=6,rowspan=6)

lb.configure(yscrollcommand=sb.set)
sb.configure(command=lb.yview)

lb.bind('<<ListboxSelect>>',get_selected_row)
window.mainloop() #윈도우 창 종료