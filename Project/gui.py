from tkinter import *
from tkinter import ttk
from database import *


class GUI:
    def __init__(self):
        # initialize Tkinter
        root = Tk()
        # initialize title of Window
        root.title("Restaurant Management System")
        # specifies the window's dimensions
        root.geometry("300x200")
        old_window = ttk.Notebook(root)
        # initializes the Frames(Rectangular Windows) for other widgets
        tab1 = ttk.Frame(old_window)
        # adds a tab
        old_window.add(tab1, text='Welcome')
        # edits the attribute/s of the tab
        old_window.pack(expand=1, fill="both")
        # creates a Label
        ttk.Label(tab1, text="Please specify your allergen").place(x=0, y=0)
        # initializes var1-3 as a String Variable of Tkinter
        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        # creates a checkbutton
        ttk.Checkbutton(tab1, variable=var1, text="Nuts", onvalue="Nuts", offvalue=None).place(x=0, y=20)
        ttk.Checkbutton(tab1, variable=var2, text="Seafood", onvalue="Seafood", offvalue=None).place(x=0, y=40)
        ttk.Checkbutton(tab1, variable=var3, text="Dairy", onvalue="Dairy", offvalue=None).place(x=0, y=60)
        ttk.Button(tab1, text="Proceed to Menu", command=lambda: [root.destroy(),
                                                                  self.open_new_window(var1, var2, var3),
                                                                  Database()]).place(x=100, y=100)
        # disables the window to be resizable
        root.resizable(False, False)
        # runs the code
        root.mainloop()

    def open_new_window(self, var1, var2, var3):
        # initialize Tkinter
        new = Tk()
        # initialize title of Window
        new.title("Restaurant Management System")
        # specifies the window's dimensions
        new.geometry("500x200")
        # initializes Notebook widget for the collection of windows and displays it one at a time.
        new_window = ttk.Notebook(new)
        # initializes the Frames(Rectangular Windows) for other widgets
        tab2 = ttk.Frame(new_window)
        tab3 = ttk.Frame(new_window)
        tab4 = ttk.Frame(new_window)
        tab5 = ttk.Frame(new_window)
        tab6 = ttk.Frame(new_window)
        # add tabs to whichever frame
        new_window.add(tab2, text="Appetizers")
        new_window.pack(expand=1, fill="both")
        new_window.add(tab3, text="Main Dish")
        new_window.pack(expand=1, fill="both")
        new_window.add(tab4, text="Desserts")
        new_window.pack(expand=1, fill="both")
        new_window.add(tab5, text="Beverages")
        new_window.pack(expand=1, fill="both")
        # creating frame
        top_view_form1 = Frame(tab2, width=600, bd=1, relief=SOLID)
        top_view_form1.pack(side=TOP, fill=X)
        left_view_form1 = Frame(tab2, width=600)
        left_view_form1.pack(side=LEFT, fill=Y)
        mid_view_form1 = Frame(tab2, width=600)
        mid_view_form1.pack(side=RIGHT)
        lbl_text = Label(top_view_form1, text="Appetizers", font=('verdana', 18), width=600, bg="#1C2833", fg="white")
        lbl_text.pack(fill=X)
        ttk.Label(left_view_form1, text="What will you Order?", font=('verdana', 15)).pack(side=TOP, anchor=W)
        top_view_form2 = Frame(tab3, width=600, bd=1, relief=SOLID)
        top_view_form2.pack(side=TOP, fill=X)
        left_view_form2 = Frame(tab3, width=600)
        left_view_form2.pack(side=LEFT, fill=Y)
        mid_view_form2 = Frame(tab3, width=600)
        mid_view_form2.pack(side=RIGHT)
        lbl_text = Label(top_view_form2, text="Appetizers", font=('verdana', 18), width=600, bg="#1C2833", fg="white")
        lbl_text.pack(fill=X)
        ttk.Label(left_view_form2, text="What will you Order?", font=('verdana', 15)).pack(side=TOP, anchor=W)
        top_view_form3 = Frame(tab4, width=600, bd=1, relief=SOLID)
        top_view_form3.pack(side=TOP, fill=X)
        left_view_form3 = Frame(tab4, width=600)
        left_view_form3.pack(side=LEFT, fill=Y)
        mid_view_form3 = Frame(tab4, width=600)
        mid_view_form3.pack(side=RIGHT)
        lbl_text = Label(top_view_form3, text="Appetizers", font=('verdana', 18), width=600, bg="#1C2833", fg="white")
        lbl_text.pack(fill=X)
        ttk.Label(left_view_form3, text="What will you Order?", font=('verdana', 15)).pack(side=TOP, anchor=W)
        top_view_form4 = Frame(tab5, width=600, bd=1, relief=SOLID)
        top_view_form4.pack(side=TOP, fill=X)
        left_view_form4 = Frame(tab5, width=600)
        left_view_form4.pack(side=LEFT, fill=Y)
        mid_view_form4 = Frame(tab5, width=600)
        mid_view_form4.pack(side=RIGHT)
        lbl_text = Label(top_view_form4, text="Appetizers", font=('verdana', 18), width=600, bg="#1C2833", fg="white")
        lbl_text.pack(fill=X)
        ttk.Label(left_view_form4, text="What will you Order?", font=('verdana', 15)).pack(side=TOP, anchor=W)
        top_view_form5 = Frame(tab6, width=600, bd=1, relief=SOLID)
        top_view_form5.pack(side=TOP, fill=X)
        left_view_form5 = Frame(tab6, width=600)
        left_view_form5.pack(side=LEFT, fill=Y)
        mid_view_form5 = Frame(tab6, width=600)
        mid_view_form5.pack(side=RIGHT)
        lbl_text = Label(top_view_form5, text="Appetizers", font=('verdana', 18), width=600,
                         bg="#1C2833", fg="white")
        lbl_text.pack(fill=X)
        ttk.Label(left_view_form5, text="What will you Order?", font=('verdana', 15)).pack(side=TOP, anchor=W)
        # setting scrollbar
        scroll_bar_x1 = Scrollbar(mid_view_form1, orient=HORIZONTAL)
        scroll_bar_y1 = Scrollbar(mid_view_form1, orient=VERTICAL)
        tree1 = ttk.Treeview(mid_view_form1, columns=("Name", "Cost"),
                             selectmode="extended", height=100, yscrollcommand=scroll_bar_y1.set,
                             xscrollcommand=scroll_bar_x1.set)
        scroll_bar_x2 = Scrollbar(mid_view_form2, orient=HORIZONTAL)
        scroll_bar_y2 = Scrollbar(mid_view_form2, orient=VERTICAL)
        tree2 = ttk.Treeview(mid_view_form2, columns=("Name", "Cost"),
                             selectmode="extended", height=100, yscrollcommand=scroll_bar_y2.set,
                             xscrollcommand=scroll_bar_x2.set)
        scroll_bar_x3 = Scrollbar(mid_view_form3, orient=HORIZONTAL)
        scroll_bar_y3 = Scrollbar(mid_view_form3, orient=VERTICAL)
        tree3 = ttk.Treeview(mid_view_form3, columns=("Name", "Cost"),
                             selectmode="extended", height=100, yscrollcommand=scroll_bar_y3.set,
                             xscrollcommand=scroll_bar_x3.set)
        scroll_bar_x4 = Scrollbar(mid_view_form4, orient=HORIZONTAL)
        scroll_bar_y4 = Scrollbar(mid_view_form4, orient=VERTICAL)
        tree4 = ttk.Treeview(mid_view_form4, columns=("Name", "Cost"),
                             selectmode="extended", height=100, yscrollcommand=scroll_bar_y4.set,
                             xscrollcommand=scroll_bar_x4.set)
        scroll_bar_x5 = Scrollbar(mid_view_form5, orient=HORIZONTAL)
        scroll_bar_y5 = Scrollbar(mid_view_form5, orient=VERTICAL)
        tree5 = ttk.Treeview(mid_view_form4, columns=("Name", "Cost"),
                             selectmode="extended", height=100, yscrollcommand=scroll_bar_y5.set,
                             xscrollcommand=scroll_bar_x5.set)
        scroll_bar_x5 = Scrollbar(mid_view_form5, orient=HORIZONTAL)
        scroll_bar_y5 = Scrollbar(mid_view_form5, orient=VERTICAL)
        # edit properties of the scrollbars
        scroll_bar_y1.config(command=tree1.yview)
        scroll_bar_y1.pack(side=RIGHT, fill=Y)
        scroll_bar_x1.config(command=tree1.xview)
        scroll_bar_x1.pack(side=BOTTOM, fill=X)
        scroll_bar_y2.config(command=tree2.yview)
        scroll_bar_y2.pack(side=RIGHT, fill=Y)
        scroll_bar_x2.config(command=tree2.xview)
        scroll_bar_x2.pack(side=BOTTOM, fill=X)
        scroll_bar_y3.config(command=tree3.yview)
        scroll_bar_y3.pack(side=RIGHT, fill=Y)
        scroll_bar_x3.config(command=tree3.xview)
        scroll_bar_x3.pack(side=BOTTOM, fill=X)
        scroll_bar_y4.config(command=tree4.yview)
        scroll_bar_y4.pack(side=RIGHT, fill=Y)
        scroll_bar_x4.config(command=tree4.xview)
        scroll_bar_x4.pack(side=BOTTOM, fill=X)
        scroll_bar_y5.config(command=tree5.yview)
        scroll_bar_y5.pack(side=RIGHT, fill=Y)
        scroll_bar_x5.config(command=tree5.xview)
        scroll_bar_x5.pack(side=BOTTOM, fill=X)
        # setting headings for the columns
        tree1.heading('Name', text="Name", anchor=W)
        tree1.heading('Cost', text="Cost", anchor=W)
        tree2.heading('Name', text="Name", anchor=W)
        tree2.heading('Cost', text="Cost", anchor=W)
        tree3.heading('Name', text="Name", anchor=W)
        tree3.heading('Cost', text="Cost", anchor=W)
        tree4.heading('Name', text="Name", anchor=W)
        tree4.heading('Cost', text="Cost", anchor=W)
        tree5.heading('Name', text="Name", anchor=W)
        tree5.heading('Cost', text="Cost", anchor=W)
        # setting width of the columns
        tree1.column('#0', stretch=NO, minwidth=0, width=0)
        tree1.column('#1', stretch=NO, minwidth=0, width=150)
        tree1.column('#2', stretch=NO, minwidth=0, width=150)
        tree1.pack()
        tree2.column('#0', stretch=NO, minwidth=0, width=0)
        tree2.column('#1', stretch=NO, minwidth=0, width=150)
        tree2.column('#2', stretch=NO, minwidth=0, width=150)
        tree2.pack()
        tree3.column('#0', stretch=NO, minwidth=0, width=0)
        tree3.column('#1', stretch=NO, minwidth=0, width=150)
        tree3.column('#2', stretch=NO, minwidth=0, width=150)
        tree3.pack()
        tree4.column('#0', stretch=NO, minwidth=0, width=0)
        tree4.column('#1', stretch=NO, minwidth=0, width=150)
        tree4.column('#2', stretch=NO, minwidth=0, width=150)
        tree4.pack()
        tree5.column('#0', stretch=NO, minwidth=0, width=0)
        tree5.column('#1', stretch=NO, minwidth=0, width=150)
        tree5.column('#2', stretch=NO, minwidth=0, width=150)
        tree5.pack()
        # creating buttons
        ttk.Button(left_view_form1, text="Back", command=lambda: [new.destroy(),
                                                                  self.__init__()]).pack(side=TOP, anchor=W)
        ttk.Button(left_view_form2, text="Back", command=lambda: [new.destroy(),
                                                                  self.__init__()]).pack(side=TOP, anchor=W)
        ttk.Button(left_view_form3, text="Back", command=lambda: [new.destroy(),
                                                                  self.__init__()]).pack(side=TOP, anchor=W)
        ttk.Button(left_view_form4, text="Back", command=lambda: [new.destroy(),
                                                                  self.__init__()]).pack(side=TOP, anchor=W)
        ttk.Button(left_view_form5, text="Back", command=lambda: [new.destroy(),
                                                                  self.__init__()]).pack(side=TOP, anchor=W)
        self.remove_record(tree1, tree2, tree3, tree4, tree5, var1, var2, var3)
        new.resizable(False, False)
        new.mainloop()

    def display_data(self, tree1, tree2, tree3, tree4, tree5):
        # clearing current display data
        tree1.delete(*tree1.get_children())
        tree2.delete(*tree2.get_children())
        tree3.delete(*tree3.get_children())
        tree4.delete(*tree4.get_children())
        tree5.delete(*tree5.get_children())
        conn = sqlite3.connect('Restaurant.db')
        # select query
        cursor1 = conn.execute("SELECT name, cost FROM Appetizers")
        cursor2 = conn.execute("SELECT name, cost FROM Main_Dish")
        cursor3 = conn.execute("SELECT name, cost FROM Desserts")
        cursor4 = conn.execute("SELECT name, cost FROM Beverages")
        # fetch all data from database
        fetch1 = cursor1.fetchall()
        fetch2 = cursor2.fetchall()
        fetch3 = cursor3.fetchall()
        fetch4 = cursor4.fetchall()
        # loop for displaying all data in GUI
        for data1 in fetch1:
            tree1.insert('', 'end', values=data1)
        for data2 in fetch2:
            tree2.insert('', 'end', values=data2)
        for data3 in fetch3:
            tree3.insert('', 'end', values=data3)
        for data4 in fetch4:
            tree4.insert('', 'end', values=data4)
        cursor1.close()
        cursor2.close()
        cursor3.close()
        cursor4.close()
        conn.close()

    def remove_record(self, tree1, tree2, tree3, tree4, tree5, var1, var2, var3):
        a = var1.get()
        b = var2.get()
        c = var3.get()
        if a != "" and b == "" and c == "":
            # clearing current display data
            tree1.delete(*tree1.get_children())
            tree2.delete(*tree2.get_children())
            tree3.delete(*tree3.get_children())
            tree4.delete(*tree4.get_children())
            tree5.delete(*tree5.get_children())
            # open database
            allergen1 = [a]
            conn = sqlite3.connect('Restaurant.db')
            # select query with where clause
            a = """SELECT name, cost FROM Appetizers WHERE allergen1 NOT LIKE :a
                AND allergen2 NOT LIKE :a;"""
            cursor1 = conn.execute(a, allergen1)
            # fetch all matching records
            fetch1 = cursor1.fetchall()
            # loop for displaying all records into GUI
            for data1 in fetch1:
                tree1.insert('', 'end', values=data1)
            cursor1.close()
            b = """SELECT name, cost FROM Main_Dish WHERE allergen1 NOT LIKE :a
                            AND allergen2 NOT LIKE :a;"""
            cursor2 = conn.execute(b, allergen1)
            fetch2 = cursor2.fetchall()
            # loop for displaying all records into GUI
            for data2 in fetch2:
                tree2.insert('', 'end', values=data2)
            cursor2.close()
            c = """SELECT name, cost FROM Desserts WHERE allergen1 NOT LIKE :a
                                        AND allergen2 NOT LIKE :a;"""
            cursor3 = conn.execute(c, allergen1)
            fetch3 = cursor3.fetchall()
            # loop for displaying all records into GUI
            for data3 in fetch3:
                tree3.insert('', 'end', values=data3)
            cursor3.close()
            d = """SELECT name, cost FROM Beverages WHERE allergen1 NOT LIKE :a
                                                    AND allergen2 NOT LIKE :a;"""
            cursor4 = conn.execute(d, allergen1)
            fetch4 = cursor4.fetchall()
            # loop for displaying all records into GUI
            for data4 in fetch4:
                tree4.insert('', 'end', values=data4)
            cursor4.close()
            conn.close()
        elif a == "" and b != "" and c == "":
            # clearing current display data
            tree1.delete(*tree1.get_children())
            tree2.delete(*tree2.get_children())
            tree3.delete(*tree3.get_children())
            tree4.delete(*tree4.get_children())
            tree5.delete(*tree5.get_children())
            # open database
            conn = sqlite3.connect('Restaurant.db')
            # select query with where clause
            cursor1 = conn.execute("""SELECT name, cost FROM Appetizers WHERE allergen1 NOT LIKE :a
                AND allergen2 NOT LIKE :a;""", {"a": b})
            # fetch all matching records
            fetch1 = cursor1.fetchall()
            # loop for displaying all records into GUI
            for data1 in fetch1:
                tree1.insert('', 'end', values=data1)
            cursor1.close()
            cursor2 = conn.execute("""SELECT name, cost FROM Main_Dish WHERE allergen1 NOT LIKE :a
                AND allergen2 NOT LIKE :a;""", {"a": b})
            fetch2 = cursor2.fetchall()
            # loop for displaying all records into GUI
            for data2 in fetch2:
                tree2.insert('', 'end', values=data2)
            cursor2.close()
            cursor3 = conn.execute("""SELECT name, cost FROM Desserts WHERE allergen1 NOT LIKE :a
                AND allergen2 NOT LIKE :a;""", {"a": b})
            fetch3 = cursor3.fetchall()
            # loop for displaying all records into GUI
            for data3 in fetch3:
                tree3.insert('', 'end', values=data3)
            cursor3.close()
            cursor4 = conn.execute("""SELECT name, cost FROM Beverages WHERE allergen1 NOT LIKE :a
                AND allergen2 NOT LIKE :a;""", {"a": b})
            fetch4 = cursor4.fetchall()
            # loop for displaying all records into GUI
            for data4 in fetch4:
                tree4.insert('', 'end', values=data4)
            cursor4.close()
            conn.close()
        elif a == "" and b == "" and c != "":
            # clearing current display data
            tree1.delete(*tree1.get_children())
            tree2.delete(*tree2.get_children())
            tree3.delete(*tree3.get_children())
            tree4.delete(*tree4.get_children())
            tree5.delete(*tree5.get_children())
            # open database
            conn = sqlite3.connect('Restaurant.db')
            # select query with where clause
            cursor1 = conn.execute("""SELECT name, cost FROM Appetizers WHERE allergen1 NOT LIKE :a
                AND allergen2 NOT LIKE :a;""", {"a": c})
            # fetch all matching records
            fetch1 = cursor1.fetchall()
            # loop for displaying all records into GUI
            for data1 in fetch1:
                tree1.insert('', 'end', values=data1)
            cursor1.close()
            cursor2 = conn.execute("""SELECT name, cost FROM Main_Dish WHERE allergen1 NOT LIKE :a
                AND allergen2 NOT LIKE :a;""", {"a": c})
            fetch2 = cursor2.fetchall()
            # loop for displaying all records into GUI
            for data2 in fetch2:
                tree2.insert('', 'end', values=data2)
            cursor2.close()
            cursor3 = conn.execute("""SELECT name, cost FROM Desserts WHERE allergen1 NOT LIKE :a
                AND allergen2 NOT LIKE :a;""", {"a": c})
            fetch3 = cursor3.fetchall()
            # loop for displaying all records into GUI
            for data3 in fetch3:
                tree3.insert('', 'end', values=data3)
            cursor3.close()
            cursor4 = conn.execute("""SELECT name, cost FROM Beverages WHERE allergen1 NOT LIKE :a
                AND allergen2 NOT LIKE :a;""", {"a": c})
            fetch4 = cursor4.fetchall()
            # loop for displaying all records into GUI
            for data4 in fetch4:
                tree4.insert('', 'end', values=data4)
            cursor4.close()
            conn.close()
        elif a != "" and b != "" and c == "":
            # clearing current display data
            tree1.delete(*tree1.get_children())
            tree2.delete(*tree2.get_children())
            tree3.delete(*tree3.get_children())
            tree4.delete(*tree4.get_children())
            tree5.delete(*tree5.get_children())
            # open database
            conn = sqlite3.connect('Restaurant.db')
            # select query with where clause
            cursor1 = conn.execute("""SELECT name, cost FROM Appetizers WHERE (allergen1 NOT LIKE :a 
                        AND allergen1 NOT LIKE :b)
                        AND (allergen2 NOT LIKE :a
                        AND allergen2 NOT LIKE :b)""",
                                   {"a": a, "b": b})
            # fetch all matching records
            fetch1 = cursor1.fetchall()
            # loop for displaying all records into GUI
            for data1 in fetch1:
                tree1.insert('', 'end', values=data1)
            cursor1.close()
            cursor2 = conn.execute("""SELECT name, cost FROM Main_Dish WHERE (allergen1 NOT LIKE :a 
                        AND allergen1 NOT LIKE :b)
                        AND (allergen2 NOT LIKE :a
                        AND allergen2 NOT LIKE :b)""",
                                   {"a": a, "b": b})
            fetch2 = cursor2.fetchall()
            # loop for displaying all records into GUI
            for data2 in fetch2:
                tree2.insert('', 'end', values=data2)
            cursor2.close()
            cursor3 = conn.execute("""SELECT name, cost FROM Desserts WHERE (allergen1 NOT LIKE :a 
                        AND allergen1 NOT LIKE :b)
                        AND (allergen2 NOT LIKE :a
                        AND allergen2 NOT LIKE :b)""",
                                   {"a": a, "b": b})
            fetch3 = cursor3.fetchall()
            # loop for displaying all records into GUI
            for data3 in fetch3:
                tree3.insert('', 'end', values=data3)
            cursor3.close()
            cursor4 = conn.execute("""SELECT name, cost FROM Beverages WHERE (allergen1 NOT LIKE :a 
                        AND allergen1 NOT LIKE :b)
                        AND (allergen2 NOT LIKE :a
                        AND allergen2 NOT LIKE :b)""",
                                   {"a": a, "b": b})
            fetch4 = cursor4.fetchall()
            # loop for displaying all records into GUI
            for data4 in fetch4:
                tree4.insert('', 'end', values=data4)
            cursor4.close()
            conn.close()
        elif a != "" and b == "" and c != "":
            # clearing current display data
            tree1.delete(*tree1.get_children())
            tree2.delete(*tree2.get_children())
            tree3.delete(*tree3.get_children())
            tree4.delete(*tree4.get_children())
            tree5.delete(*tree5.get_children())
            # open database
            conn = sqlite3.connect('Restaurant.db')
            # select query with where clause
            cursor1 = conn.execute("""SELECT name, cost FROM Appetizers WHERE (allergen1 NOT LIKE :a 
                        AND allergen1 NOT LIKE :b)
                        AND (allergen2 NOT LIKE :a
                        AND allergen2 NOT LIKE :b)""",
                                   {"a": a, "b": c})
            # fetch all matching records
            fetch1 = cursor1.fetchall()
            # loop for displaying all records into GUI
            for data1 in fetch1:
                tree1.insert('', 'end', values=data1)
            cursor1.close()
            cursor2 = conn.execute("""SELECT name, cost FROM Main_Dish WHERE (allergen1 NOT LIKE :a 
                        AND allergen1 NOT LIKE :b)
                        AND (allergen2 NOT LIKE :a
                        AND allergen2 NOT LIKE :b)""",
                                   {"a": a, "b": c})
            fetch2 = cursor2.fetchall()
            # loop for displaying all records into GUI
            for data2 in fetch2:
                tree2.insert('', 'end', values=data2)
            cursor2.close()
            cursor3 = conn.execute("""SELECT name, cost FROM Desserts WHERE (allergen1 NOT LIKE :a 
                        AND allergen1 NOT LIKE :b)
                        AND (allergen2 NOT LIKE :a
                        AND allergen2 NOT LIKE :b)""",
                                   {"a": a, "b": c})
            fetch3 = cursor3.fetchall()
            # loop for displaying all records into GUI
            for data3 in fetch3:
                tree3.insert('', 'end', values=data3)
            cursor3.close()
            cursor4 = conn.execute("""SELECT name, cost FROM Beverages WHERE (allergen1 NOT LIKE :a 
                        AND allergen1 NOT LIKE :b)
                        AND (allergen2 NOT LIKE :a
                        AND allergen2 NOT LIKE :b)""",
                                   {"a": a, "b": c})
            fetch4 = cursor4.fetchall()
            # loop for displaying all records into GUI
            for data4 in fetch4:
                tree4.insert('', 'end', values=data4)
            cursor4.close()
            conn.close()
        elif a == "" and b != "" and c != "":
            # clearing current display data
            tree1.delete(*tree1.get_children())
            tree2.delete(*tree2.get_children())
            tree3.delete(*tree3.get_children())
            tree4.delete(*tree4.get_children())
            tree5.delete(*tree5.get_children())
            # open database
            conn = sqlite3.connect('Restaurant.db')
            # select query with where clause
            cursor1 = conn.execute("""SELECTname, cost FROM Appetizers WHERE (allergen1 NOT LIKE :a 
                        AND allergen1 NOT LIKE :b)
                        AND (allergen2 NOT LIKE :a
                        AND allergen2 NOT LIKE :b)""",
                                   {"a": b, "b": c})
            # fetch all matching records
            fetch1 = cursor1.fetchall()
            # loop for displaying all records into GUI
            for data1 in fetch1:
                tree1.insert('', 'end', values=data1)
            cursor1.close()
            cursor2 = conn.execute("""SELECT name, cost FROM Main_Dish WHERE (allergen1 NOT LIKE :a 
                        AND allergen1 NOT LIKE :b)
                        AND (allergen2 NOT LIKE :a
                        AND allergen2 NOT LIKE :b)""",
                                   {"a": b, "b": c})
            fetch2 = cursor2.fetchall()
            # loop for displaying all records into GUI
            for data2 in fetch2:
                tree2.insert('', 'end', values=data2)
            cursor2.close()
            cursor3 = conn.execute("""SELECT name, cost FROM Desserts WHERE (allergen1 NOT LIKE :a 
                        AND allergen1 NOT LIKE :b)
                        AND (allergen2 NOT LIKE :a
                        AND allergen2 NOT LIKE :b)""",
                                   {"a": b, "b": c})
            fetch3 = cursor3.fetchall()
            # loop for displaying all records into GUI
            for data3 in fetch3:
                tree3.insert('', 'end', values=data3)
            cursor3.close()
            cursor4 = conn.execute("""SELECT name, cost FROM Beverages WHERE (allergen1 NOT LIKE :a 
                        AND allergen1 NOT LIKE :b)
                        AND (allergen2 NOT LIKE :a
                        AND allergen2 NOT LIKE :b)""",
                                   {"a": b, "b": c})
            fetch4 = cursor4.fetchall()
            # loop for displaying all records into GUI
            for data4 in fetch4:
                tree4.insert('', 'end', values=data4)
            cursor4.close()
            conn.close()
        elif a != "" and b != "" and c != "":
            # clearing current display data
            tree1.delete(*tree1.get_children())
            tree2.delete(*tree2.get_children())
            tree3.delete(*tree3.get_children())
            tree4.delete(*tree4.get_children())
            tree5.delete(*tree5.get_children())
            # open database
            conn = sqlite3.connect('Restaurant.db')
            # select query with where clause
            cursor1 = conn.execute("""SELECT name, cost FROM Appetizers WHERE (allergen1 NOT LIKE :a 
            AND allergen1 NOT LIKE :b 
            AND allergen1 NOT LIKE :c)
            AND (allergen2 NOT LIKE :a 
            AND allergen2 NOT LIKE :b 
            AND allergen2 NOT LIKE :c)""",
                                   {"a": a, "b": b, "c": c, })
            # fetch all matching records
            fetch1 = cursor1.fetchall()
            # loop for displaying all records into GUI
            for data1 in fetch1:
                tree1.insert('', 'end', values=data1)
            cursor1.close()
            cursor2 = conn.execute("""SELECT name, cost FROM Main_Dish WHERE (allergen1 NOT LIKE :a 
            AND allergen1 NOT LIKE :b 
            AND allergen1 NOT LIKE :c)
            AND (allergen2 NOT LIKE :a 
            AND allergen2 NOT LIKE :b 
            AND allergen2 NOT LIKE :c)""",
                                   {"a": a, "b": b, "c": c, })
            fetch2 = cursor2.fetchall()
            # loop for displaying all records into GUI
            for data2 in fetch2:
                tree2.insert('', 'end', values=data2)
            # closes cursor object
            cursor2.close()
            cursor3 = conn.execute("""SELECT name, cost FROM Desserts WHERE (allergen1 NOT LIKE :a 
            AND allergen1 NOT LIKE :b 
            AND allergen1 NOT LIKE :c)
            AND (allergen2 NOT LIKE :a 
            AND allergen2 NOT LIKE :b 
            AND allergen2 NOT LIKE :c)""", {"a": a, "b": b, "c": c})
            fetch3 = cursor3.fetchall()
            # loop for displaying all records into GUI
            for data3 in fetch3:
                tree3.insert('', 'end', values=data3)
            # closes cursor object
            cursor3.close()
            cursor4 = conn.execute("""SELECT name, cost FROM Beverages WHERE (allergen1 NOT LIKE :a 
            AND allergen1 NOT LIKE :b 
            AND allergen1 NOT LIKE :c)
            AND (allergen2 NOT LIKE :a 
            AND allergen2 NOT LIKE :b 
            AND allergen2 NOT LIKE :c)""",
                                   {"a": a, "b": b, "c": c, })
            fetch4 = cursor4.fetchall()
            # loop for displaying all records into GUI
            for data4 in fetch4:
                tree4.insert('', 'end', values=data4)
            # closes cursor object
            cursor4.close()
            conn.close()
        else:
            self.display_data(tree1, tree2, tree3, tree4, tree5)


