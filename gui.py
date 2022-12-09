from tkinter import *
import csv

class GUI:
    def __init__(self, window):

        self.window = window
        self.frame_account = Frame(self.window)
        self.label_account = Label(self.frame_account, text='Account Name')
        self.entry_account = Entry(self.frame_account)
        self.label_account.pack(padx=5, side='left')
        self.entry_account.pack(padx=5, side='left')
        self.frame_account.pack(anchor='w', pady=10)

        self.frame_password = Frame(self.window)
        self.label_password = Label(self.frame_password, text='Password')
        self.entry_password = Entry(self.frame_password)
        self.label_password.pack(padx=20, side='left')
        self.entry_password.pack(padx=5, side='left')
        self.frame_password.pack(anchor='w', pady=10)

        self.frame_button = Frame(self.window)
        self.button_log = Button(self.frame_button, text='Submit', command=self.clicked)
        self.button_log.pack()
        self.frame_button.pack()

        self.label_message = Label(self.window)
        self.label_message.pack()



    def clicked(self):
        x = 0
        with open('records.csv', 'r') as checking:
            reading = csv.reader(checking)
            for row in reading:
                if self.entry_account.get() in row and self.entry_password.get() in row:
                    global account_name
                    account_name = self.entry_account.get()
                    x = 1
        if x == 1:
            self.frame_account.destroy()
            self.frame_password.destroy()
            self.frame_button.destroy()
            new.new_add(self)
        else:
            self.label_message.config(text=f'Account information or password is incorrect.\nPlease re-enter information.')
            self.entry_password.delete(0, END)
            self.entry_account.delete(0, END)

    def clack(self):
        with open('records.csv', 'r') as checking:
            reading = csv.reader(checking)
            for row in reading:
                if account_name in row:
                    balance = float(row[2])
        amount = float(self.entry_amount.get())
        status = self.check_1.get()
        if status == 0:
            if amount <=0:
                self.label_message.config(text=f'Please deposit positive amount.')
            else:
                total = balance + amount
                self.label_message.config(text=f'{account_name} has ${total:.2f}')
        elif status == 1:
            if amount > balance:
                self.label_message.config(text=f'Cannot withdraw more than account balance ${balance}.')
            elif amount <= 0:
                self.label_message.config(text=f'Cannot withdraw negative amount.\nBalance ${balance}')
            else:
                total = balance - amount
                self.label_message.config(text=f'{account_name} has ${total}')

class new:
    def new_add(self):
        with open('records.csv', 'r') as checking:
            reading = csv.reader(checking)
            for row in reading:
                if account_name in row:
                    self.label_message.config(text=f'You have ${row[2]} in your account.')
        self.frame_check = Frame(self.window)
        self.check_1 = IntVar()
        self.check_1.set(0)
        self.check_deposit = Radiobutton(self.frame_check, text='Deposit', variable=self.check_1, value=0)
        self.check_with = Radiobutton(self.frame_check, text='Withdraw', variable=self.check_1, value=1)
        self.check_deposit.pack()
        self.check_with.pack()
        self.frame_check.pack()

        self.frame_amount = Frame(self.window)
        self.label_amount = Label(self.frame_amount, text='Amount')
        self.entry_amount = Entry(self.frame_amount)
        self.label_amount.pack(padx=10, side='left')
        self.entry_amount.pack(padx=30, side='left')
        self.frame_amount.pack(anchor='w', pady=10)

        self.frame_butt = Frame(self.window)
        self.butt_log = Button(self.frame_butt, text='Submit', command=self.clack)
        self.butt_log.pack()
        self.frame_butt.pack()
