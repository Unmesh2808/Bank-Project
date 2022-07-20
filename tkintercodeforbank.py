from cgitb import text
import Bank
from tkinter import *
from tkinter import messagebox
import ast
from turtle import heading
from Bank import BankAccount

window = Tk()
window.title("Bank Login Page")
window.geometry("925x500+300+200")
window.configure(bg='#fff')
window.resizable(False, False)

img = PhotoImage(file="D:\\MY_PY_codes\\Coding_1\\bank1.png")

#ACCOUNT CREATION WINDOW
def func1():
    def call_inp1():
        names = name.get()
        PAN = pan.get()
        bankname = bank_name.get()
        Bank.Customer(names, PAN, bankname)
        #messagebox.showinfo("info",f"the PAN is {PAN}, preferred bank name is {bankname}")
    frame2=Frame(window, width=350, height=390, bg='#fff')
    frame2.place(x=480,y=50)
    text= Label(frame2, text="Enter your full name", fg="black", bg='white', font=("times", 16))
    text.place(x=25,y=77)
    name = Entry(frame2, width=25, fg="black", border=2, bg="white",font=("Helvetica",14))
    name.place(x=25,y=107)
    text= Label(frame2, text="Enter your PAN card details", fg="black", bg='white', font=("times", 16))
    text.place(x=25,y=137)
    pan = Entry(frame2, width=25, fg="black", border=2, bg="white",font=("Helvetica",14))
    pan.place(x=25,y=167)
    text= Label(frame2, text="Enter your preferred bank name", fg="black", bg='white', font=("times", 16))
    text.place(x=25,y=197)
    bank_name = Entry(frame2, width=25, fg="black", border=2, bg="white",font=("Helvetica",14))
    bank_name.place(x=25,y=227)
    Button(frame2, width=39, text="Submit", bg="#57a1f8", fg="white", border=2, command = call_inp1).place(x=25,y=270)
    Button(frame2, width=20, text="Back to Main Menu", bg="grey", fg="black", border=2, command=main_func007).place(x=27,y=300)

# AMOUNT DEPOSIT WINDOW 
def func2():   
    def call_inp2():
        acn = acnt_num.get()
        Pin = int(pin.get())
        ramt = int(amt.get())
        BankAccount.deposit(acn, Pin, ramt) 
    frame3= Frame(window, width=350, height=390, bg="#fff")
    frame3.place(x=480,y=50)
    text= Label(frame3, text="Enter your account number", fg="black", bg='white', font=("times", 16))
    text.place(x=25,y=77)
    acnt_num = Entry(frame3, width=25, fg="black", border=2, bg="white",font=("Helvetica",14))
    acnt_num.place(x=25,y=107)
    text= Label(frame3, text="Enter your PIN ", fg="black", bg='white', font=("times", 16))
    text.place(x=25,y=137)
    pin = Entry(frame3, width=25, fg="black", border=2, bg="white",font=("Helvetica",14), show="*")
    pin.place(x=25,y=167)
    text= Label(frame3, text="Amount to be Deposited", fg="black", bg='white', font=("times", 16))
    text.place(x=25,y=197)
    amt = Entry(frame3, width=25, fg="black", border=2, bg="white",font=("Helvetica",14))
    amt.place(x=25,y=227)
    Button(frame3, width=39, text="Submit", bg="#57a1f8", fg="white", border=2, command=call_inp2).place(x=25,y=270)
    Button(frame3, width=20, text="Back to Main Menu", bg="grey", fg="black", border=2, command=main_func007).place(x=27,y=300)

# AMOUNT WITHDRAW WINDOW
def func3():    
    def call_inp3():
        acn = acnt_num.get()
        Pin = int(pin.get())
        ramt = int(amt.get())
        BankAccount.withdraw(acn, Pin, ramt)
    frame4= Frame(window, width=350, height=390, bg="#fff")
    frame4.place(x=480,y=50)
    text= Label(frame4, text="Enter your account number", fg="black", bg='white', font=("times", 16))
    text.place(x=25,y=77)
    acnt_num = Entry(frame4, width=25, fg="black", border=2, bg="white",font=("Helvetica",14))
    acnt_num.place(x=25,y=107)
    text= Label(frame4, text="Enter your PIN ", fg="black", bg='white', font=("times", 16))
    text.place(x=25,y=137)
    pin = Entry(frame4, width=25, fg="black", border=2, bg="white",font=("Helvetica",14), show="*")
    pin.place(x=25,y=167)
    text= Label(frame4, text="Amount to be Withdrawn", fg="black", bg='white', font=("times", 16))
    text.place(x=25,y=197)
    amt = Entry(frame4, width=25, fg="black", border=2, bg="white",font=("Helvetica",14))
    amt.place(x=25,y=227)
    Button(frame4, width=39, text="Submit", bg="#57a1f8", fg="white", border=2, command=call_inp3).place(x=25,y=270)
    Button(frame4, width=20, text="Back to Main Menu", bg="grey", fg="black", border=2, command=main_func007).place(x=27,y=300)

# BALANCE CHECK WINDOW
def func4(): 
    def call_inp4():
        acn = acnt_num.get()
        Pin = int(pin.get())
        BankAccount.balance(acn, Pin)
    frame5= Frame(window, width=350, height=390, bg="#fff")
    frame5.place(x=480,y=50)
    text= Label(frame5, text="Enter your account number", fg="black", bg='white', font=("times", 16))
    text.place(x=25,y=77)
    acnt_num = Entry(frame5, width=25, fg="black", border=2, bg="white",font=("Helvetica",14))
    acnt_num.place(x=25,y=107)
    text= Label(frame5, text="Enter your PIN ", fg="black", bg='white', font=("times", 16))
    text.place(x=25,y=137)
    pin = Entry(frame5, width=25, fg="black", border=2, bg="white",font=("Helvetica",14), show="*")
    pin.place(x=25,y=167)
    Button(frame5, width=39, text="Submit", bg="#57a1f8", fg="white", border=2, command=call_inp4).place(x=25,y=270)
    Button(frame5, width=20, text="Back to Main Menu", bg="grey", fg="black", border=2, command=main_func007).place(x=27,y=300)

def main_func007():    
    def get_choice():
        choice=user.get().lower()
        if choice=='a':
            func1()
        elif choice=="b":
            func2()
        elif choice=="c":
            func3()
        elif choice=="d":
            func4()
            
    Label(window, image=img, border=0, bg="white").place(x=50,y=90)
    frame1=Frame(window, width=350, height=390, bg='#fff')
    frame1.place(x=480,y=50)

    #messagebox.showinfo("info","This u=is an info message")

    heading= Label(frame1, text='Bank Login Page', fg="grey", bg="white", font=('Roman',23,'bold'))
    heading.place(x=100,y=5)

    text= Label(frame1, text="Choose from the following options: ", fg="black", bg="white", font=("times",16, 'bold'))
    text.place(x=25,y=107)
    text= Label(frame1, text="(a) To create new Account", fg="black", bg="white", font=("times",16))
    text.place(x=25,y=137)
    text= Label(frame1, text="(b) To deposit in the account", fg="black", bg="white", font=("times",16))
    text.place(x=25,y=167)
    text= Label(frame1, text="(c) To withdraw from the account", fg="black", bg="white", font=("times",16))
    text.place(x=25,y=197)
    text= Label(frame1, text="(d) To check your balance amount", fg="black", bg="white", font=("times",16))
    text.place(x=25,y=227)

    def on_enter(e):
        user.delete(0,"end")
    def on_leave(e):
        if user.get()=="":
            user.insert(0,"Choice")

    user = Entry(frame1, width=25, fg="black", border=2, bg="white",font=("Helvetica",11))
    user.place(x=30,y=80)
    user.insert(0, "Choice")
    user.bind("<FocusIn>",on_enter)
    user.bind("<FocusOut>",on_leave)

    Button(frame1, width=10, text="Submit", bg="#57a1f8", fg="white", border=2, command=get_choice).place(x=240,y=80)

main_func007()    
#####-----------------------------------------------------------------------
window.mainloop()

#text= Label(frame, text="(a) To create new Account\n(b) To deposit in the account\n(c) To withdraw from the account\n(d) To check your balance amount", fg="black", bg="white", font=("times",16))
#text.place(x=25,y=107)