import sqlite3
from tkinter import *
import pandas as pd
from tkinter import messagebox


options = ['Male', 'Female']
Name = []
Age = []
Phone_number = []
Gender = []

root = Tk()
root.title('COVID database')
root.minsize(width=500, height=500)

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS people (name TEXT, age INTEGER)")
conn.commit()
conn.close()


def tab1():
    choices = options  # Added this line

    def tab2():
        L1.destroy()
        BP1.destroy()
        BP2.destroy()
        L2 = Label(root, text='Add People', font=("Times_New_Roman", 20))
        L2.pack()
        LP2 = Label(root, text='Name', font=("Times_New_Roman", 20))
        LP2.pack(padx=15, ipadx=10, ipady=10, anchor="center")
        I2 = Entry(root, text='Name', font=("Times_New_Roman", 20))
        I2.pack(pady=20, padx=10, ipadx=10, ipady=5)
        LPD2 = Label(root, text='Age', font=("Times_New_Roman", 20))
        LPD2.pack(padx=10, ipadx=10, ipady=10, anchor="center")
        SB1 = Spinbox(root, from_=0, to=100, font=("Times_New_Roman", 20))
        SB1.pack(pady=20, padx=10, ipadx=10, ipady=9)
        LPD3 = Label(root, text='Gender', font=("Times_New_Roman", 20))
        LPD3.pack(padx=10, ipadx=10, ipady=10, anchor="center")
        CB = StringVar(root)
        CB.set(choices[0])
        CB1 = OptionMenu(root, CB, *options,)
        CB1.config(font=("Times_New_Roman", 20), width=15)
        CB1.pack(pady=20, padx=10, ipadx=10, ipady=5)
        LPD4 = Label(root, text='Phone Number', font=("Times_New_Roman", 20))
        LPD4.pack(padx=10, ipadx=10, ipady=10, anchor="center")
        PHNUM = Entry(root, text='Phone Number', font=("Times_New_Roman", 20))
        PHNUM.pack(pady=20, padx=10, ipadx=10, ipady=5)

        def OK1():
            name = str(I2.get())
            age = str(SB1.get())
            gender = str(CB.get())
            phone_number = str(PHNUM.get())
            if name == "":
                messagebox.showerror('Error', 'Please enter a name.')
            elif age == "0" or not age.isdigit():
                messagebox.showerror('Error', 'Please enter an age.')
            elif phone_number == "" or not phone_number.isdigit():
                messagebox.showerror('Error', 'Please enter your phone number.')
            else:
                age = int(age) 
                conn = sqlite3.connect('database.db')
                cursor = conn.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS people (name TEXT, age INTEGER, gender TEXT, phone_number TEXT)")
                conn.commit()
                conn.close()

                print("Name:", name)
                print("Age:", age)
                print("Gender:", gender)
                print("Phone_number:", phone_number)
                Name.append(name)
                Age.append(age)
                Gender.append(gender)
                Phone_number.append(phone_number)
                I2.delete(0, 'end')
                SB1.delete(0, 'end')
                PHNUM.delete(0, 'end')
                L2.destroy()
                B2.destroy()
                I2.destroy()
                BOK2.destroy()
                SB1.destroy()
                LP2.destroy()
                LPD2.destroy()
                CB1.destroy()
                LPD3.destroy()
                LPD4.destroy()
                PHNUM.destroy()
                tab1()

        BOK2 = Button(root, text="OK", font=("Times_New_Roman", 25), command=OK1)
        BOK2.pack(side=RIGHT, padx=10, ipadx=10, ipady=5, anchor="se")

        def back1():
                I2.delete(0, 'end')
                SB1.delete(0, 'end')
                PHNUM.delete(0, 'end')
                L2.destroy()
                B2.destroy()
                I2.destroy()
                BOK2.destroy()
                SB1.destroy()
                LP2.destroy()
                LPD2.destroy()
                CB1.destroy()
                LPD3.destroy()
                LPD4.destroy()
                PHNUM.destroy()
                tab1()
                
        B2 = Button(root, text="back", font=("Times_New_Roman", 25), command=back1)
        B2.pack(side=BOTTOM, padx=10, ipadx=10, ipady=5, anchor="se")

    def tab3():
        L1.destroy()
        BP1.destroy()
        BP2.destroy()
        L3 = Label(root, text='DATA', font=("Times_New_Roman", 25))
        L3.pack()
        conn = sqlite3.connect('database.db')
        df = pd.read_sql_query("SELECT * FROM people", conn)
        conn.close()

        TF = LabelFrame(root, text='Data Table')
        TF.pack(fill='both', expand=True, padx=10, pady=10)
        from tkinter.ttk import Treeview
        tree = Treeview(TF)
        columns = tuple(df.columns) 
        tree['columns'] = columns

        for column in columns:
            tree.heading(column, text=column)

        for index, row in df.iterrows():
            values = tuple(row) 
            tree.insert('', 'end', text=index, values=values)

        tree.pack(fill='both', expand=True)

        def back2():
            L3.destroy()
            B3.destroy()
            TF.destroy()
            tab1()

        B3 = Button(root, text="Back", font=("Times_New_Roman", 25), command=back2)
        B3.pack(side=BOTTOM)


    L1 = Label(root, text='What do you need to do', font=("Times_New_Roman", 25))
    L1.pack()
    BP1 = Button(root, text="Add People", font=("Times_New_Roman", 25), command=tab2)
    BP2 = Button(root, text="Data", font=("Times_New_Roman", 25), command=tab3)
    BP1.pack(side=LEFT, padx=10, ipadx=20, ipady=5, anchor="center")
    BP2.pack(side=LEFT, padx=10, ipadx=20, ipady=5, anchor="center")


tab1()

root.mainloop()
