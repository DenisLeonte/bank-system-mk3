import tkinter as tk
from test import test
from file_manager import manager
from user import user

man = manager.user_file()
man.set_path("database//database.txt")

def login_input(tx,ty):
    us = user()
    us.set_name(tx.get())
    us.set_password(ty.get())
    us.encrypt_password()
    if man.search_user(us) :
        x = man.get_user(us.get_name())
        if x.get_encrypted_password() == us.get_encrypted_password():
            return True
        else:
            return False
    else:
        print("User not found")
        return False


Test = test()

if Test.begin_test():
    root = tk.Tk()
    root.title("Bank System")

    #Text
    tx1 = tk.Label(root, text="Login", font="Arial").grid(column=1,row=0)
    tx2 = tk.Label(root, text="Login", font="Arial").grid(column=0,row=1)
    tx3 = tk.Label(root, text="Password", font="Arial").grid(column=0,row=2)
    txb1 = tk.Entry(root)
    txb2 = tk.Entry(root)
    but1 = tk.Button(root,text="Login",command=lambda : login_input(txb1,txb2)).grid(column=1,row=3)
    txb1.grid(column=1,row=1)
    txb2.grid(column=1,row=2)
    root.mainloop()
