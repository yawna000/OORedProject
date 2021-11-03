import tkinter as tk
from tkinter import *
from tkinter import ttk
from database import *


class Start:
    def __init__(self):
        root = tk.Tk()
        root.title("Welcome to Casa De Allana")
        root.geometry("300x200")
        oldwindow = ttk.Notebook(root)
        tab1 = ttk.Frame(oldwindow)
        oldwindow.add(tab1, text='Welcome')
        oldwindow.pack(expand=1, fill="both")
        ttk.Label(tab1, text="Please specify your allergen").place(x=0, y=0)
        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        ttk.Checkbutton(tab1, variable=var1, text="Nuts", onvalue="Nuts", offvalue=None).place(x=0, y=20)
        ttk.Checkbutton(tab1, variable=var2, text="Seafood", onvalue="Seafood", offvalue=None).place(x=0, y=40)
        ttk.Checkbutton(tab1, variable=var3, text="Dairy", onvalue="Dairy", offvalue=None).place(x=0, y=60)
        ttk.Button(tab1, text="Proceed to Menu", command=lambda: [root.destroy(), self.open_new_window(var1),
                                                                  Database()]).place(x=100, y=100)
        root.mainloop()

    def open_new_window(self, var1):
        global tree
        new = tk.Tk()
        new.title("Welcome to Casa De Allana")
        new.geometry("300x200")
        newwindow = ttk.Notebook(new)
        tab2 = ttk.Frame(newwindow)
        tab3 = ttk.Frame(newwindow)
        tab4 = ttk.Frame(newwindow)
        tab5 = ttk.Frame(newwindow)
        tab6 = ttk.Frame(newwindow)
        newwindow.add(tab2, text="Appetizers")
        newwindow.pack(expand=1, fill="both")
        newwindow.add(tab3, text="Main Dish")
        newwindow.pack(expand=1, fill="both")
        newwindow.add(tab4, text="Desserts")
        newwindow.pack(expand=1, fill="both")
        newwindow.add(tab5, text="Beverages")
        newwindow.pack(expand=1, fill="both")
        newwindow.add(tab6, text="Checkout")
        newwindow.pack(expand=1, fill="both")
        # creating frame
        top_view_form = Frame(tab2, width=600, bd=1, relief=SOLID)
        top_view_form.pack(side=TOP, fill=X)
        left_view_form = Frame(tab2, width=600)
        left_view_form.pack(side=LEFT, fill=Y)
        mid_view_form = Frame(tab2, width=600)
        mid_view_form.pack(side=RIGHT)
        lbl_text = Label(top_view_form, text="Appetizers", font=('verdana', 18), width=600,
                         bg="#1C2833", fg="white")
        lbl_text.pack(fill=X)
        lbl_txtsearch = Label(left_view_form, text="WELCOME", font=('verdana', 15))
        lbl_txtsearch.pack(side=TOP, anchor=W)
        # setting scrollbar
        scrollbarx = Scrollbar(mid_view_form, orient=HORIZONTAL)
        scrollbary = Scrollbar(mid_view_form, orient=VERTICAL)
        tree = ttk.Treeview(mid_view_form, columns=("Name", "Cost"),
                            selectmode="extended", height=100, yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        # setting headings for the columns
        tree.heading('Name', text="Name", anchor=W)
        tree.heading('Cost', text="Cost", anchor=W)
        # setting width of the columns
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=150)
        tree.pack()
        self.display_data()
        ttk.Button(tab2, text="Back", command=lambda: [new.destroy(), self.__init__()]).place(x=100, y=100)
        ttk.Button(tab2, text="Remove", command=self.remove_record(var1)).place(x=100, y=150)
        new.mainloop()

    def display_data(self):
        tree.delete(*tree.get_children())
        conn = sqlite3.connect('../Restaurant.db')
        # select query
        cursor = conn.execute("SELECT name, cost FROM Appetizers")
        # fetch all data from database
        fetch = cursor.fetchall()
        # loop for displaying all data in GUI
        for data in fetch:
            tree.insert('', 'end', values=data)
        cursor.close()
        conn.close()

    def remove_record(self, var1):
        if var1.get() != "":
            # clearing current display data
            tree.delete(*tree.get_children())
            # open database
            conn = sqlite3.connect('../Restaurant.db')
            # select query with where clause
            cursor = conn.execute("SELECT name, cost FROM Appetizers WHERE allergen NOT LIKE ?")

            # fetch all matching records
            fetch = cursor.fetchall()
            # loop for displaying all records into GUI
            for data in fetch:
                tree.insert('', 'end', values=data)
            cursor.close()
            conn.close()
        else:
            pass


Start()
