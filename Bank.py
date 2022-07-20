import mymongo
import random
from tkinter import messagebox

class BankAccount:
    def __init__(self, name, PAN, bankname):
        self.name = name
        self.pan = PAN
        self.bank_name = bankname
        self.pin = int(random.random()*10000)
        n = int(random.random()*100000)
        self.acn = f"{self.bank_name}{n}"
        self.bal = 0
        messagebox.askokcancel("info",f"Please note Your account number {self.acn} and pin no. {self.pin}")
            
    def authenticate(args, pin):
        g = 0
        print(pin)
        print(list(args.values()))
        comp = list(args.values())
        #print(type(comp)) 
        if pin == comp[5]:   
            g = 1
            return g
        
    def balance(Acnum, pin):
        #path = "D:\\MY PY codes\\Coding_1\\bankdatabase.xlsx"
        #wb_obj = openpyxl.load_workbook(path)
        #sh_obj = wb_obj.active
        verify = {}
        for all in mymongo.acquire({"AcnNum":Acnum}):
            verify.update(all)
        go = BankAccount.authenticate(verify, pin)
        if go == 1:
            Bal = list(verify.values())[6]     
            print(f"the current balance is {Bal}")
            messagebox.askokcancel("info",f"Your current balance is {Bal}")
            

    def deposit(Acnum, pin, topup):
        verify = {}
        for i in mymongo.acquire({"AcnNum":Acnum}):
            verify.update(i)
        go = BankAccount.authenticate(verify, pin)
        #print(f"go == {go}")
        if go == 1:
            #print("ok2")
            BankAccount.depo(verify, pin, topup)


    def depo(args, pin, topup):
        for k, v in list(args.items()):
            if k == "Balance":
                v += topup
                bal=v
        #print("ok3")
        mymongo.edit(bal, pin)
        print("Amount deposited successfully")
        messagebox.showinfo("info","Amount deposited successfully")

    def withdraw(Acnum, pin, rem):
        for all in mymongo.acquire({"AcnNum":Acnum}):
            verify=all
        go = BankAccount.authenticate(verify, pin)
        #print(f"go == {go}")
        if go == 1:
            #print("ok2")
            BankAccount.nikaal(verify, pin, rem)

    def nikaal(args, pin, rem):
        for k, v in list(args.items()):
            if k == "Balance":
                v -= rem
                bal=v
        #print("ok3")
        mymongo.edit(bal, pin)
        print("Amount withdrawn successfully")
        messagebox.showinfo("info","Amount withdrawn successfully")

class Customer(BankAccount):
    def __init__(self, clname, clPAN, clbankname):
        super().__init__(clname, clPAN, clbankname)
        client1 = {"name":self.name,"PAN":self.pan,"bank":self.bank_name,"AcnNum":self.acn,"Pin":self.pin,"Balance":self.bal}
        mymongo.initialize(client1)