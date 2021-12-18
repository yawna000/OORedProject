from tkinter import *
from tkinter import ttk
from database import *


class GUI(Database):
    def __init__(self):
        master = Tk()
        w = 300
        h = 200
        ws = master.winfo_screenwidth()
        hs = master.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        # initialize title of Window
        master.title("Restaurant Management System")

        # specifies the window's dimensions
        master.geometry('%dx%d+%d+%d' % (w, h, x, y))

        old_window = ttk.Notebook(master)

        # initializes the Frames(Rectangular Windows) for other widgets
        tab1 = ttk.Frame(old_window)

        # adds a tab
        self.create_window(old_window, tab1, "Welcome")
        self.create_label(tab1, "Please Specify Your Allergen", None, None, None, 15, TOP, W)

        # initializes var1-3 as a String Variable of Tkinter
        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        self.create_checkbutton(tab1, var1, "Nuts", "Nuts", None, 0, 25)
        self.create_checkbutton(tab1, var2, "Seafood", "Seafood", None, 0, 45)
        self.create_checkbutton(tab1, var3, "Dairy", "Dairy", None, 0, 65)
        self.create_button(tab1, master, "Proceed to Menu", 1, BOTTOM, S, var1, var2, var3, None, None, None, None,
                           None, None, None)
        # disables the window to be resizable
        master.resizable(False, False)
        master.mainloop()

    def create_button(self, frame, root, text, a, z, q, var1, var2, var3, name_box, cost_box, tree1, tree2, tree3,
                      tree4, tree5):
        if name_box != "":
            if a == 1:
                ttk.Button(frame, text=text, command=lambda: [root.destroy(),
                                                              self.open_new_window(var1, var2, var3),
                                                              Database()]).pack(side=z, anchor=q)
            elif a == 2:
                ttk.Button(frame, text=text, command=lambda: [root.destroy(),
                                                              GUI()]).pack(side=z, anchor=q)
            elif a == 3:
                ttk.Button(frame, text=text, command=lambda: [self.order(name_box, cost_box),
                                                              self.remove_record(tree1, tree2, tree3, tree4, tree5,
                                                                                 var1, var2, var3)])\
                    .pack(side=z, anchor=q)
            elif a == 4:
                ttk.Button(frame, text=text, command=lambda: [self.remove(name_box),
                                                              self.reset_tree(tree1, tree2, tree3, tree4, tree5),
                                                              self.remove_record(tree1, tree2, tree3, tree4, tree5,
                                                                                 var1, var2, var3)])\
                    .pack(side=z, anchor=q)
            elif a == 5:
                ttk.Button(frame, text=text, command=lambda: [self.print_bill(root)]).pack(side=z, anchor=q)

        else:
            messagebox.showerror("Error", "Cannot Accept Empty Values")

    def create_label(self, tab, text, width, bg, fg, size, x, y):
        Label(tab, text=text, font=('verdana', size), width=width, bg=bg, fg=fg).pack(side=x, anchor=y)

    def create_checkbutton(self, frame, variable, text, on, off, x, y):
        checkbutton = ttk.Checkbutton(frame, variable=variable, text=text, onvalue=on, offvalue=off)
        checkbutton.place(x=x, y=y)

    def create_window(self, window, frame, text):
        window.add(frame, text=text)
        window.pack(expand=1, fill="both")

    def reset_tree(self, tree1, tree2, tree3, tree4, tree5):
        # clearing current display data
        tree1.delete(*tree1.get_children())
        tree2.delete(*tree2.get_children())
        tree3.delete(*tree3.get_children())
        tree4.delete(*tree4.get_children())
        tree5.delete(*tree5.get_children())

    def retrieve_data(self, cursor, tree):
        # fetch all matching records and loop for displaying all records into GUI
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=data)
        cursor.close()

    def bind(self, tree, clicker):
        tree.bind("<Double-1>", clicker)
        tree.bind("<ButtonRelease-1>", clicker)

    def open_new_window(self, var1, var2, var3):
        total = 0

        def txt_config(textbox1, values, index1):
            # inserts value and configure text boxes
            textbox1.config(state="normal")
            textbox1.insert(0, values[index1])
            textbox1.config(state="disabled")

        def txt_config_delete(textbox1):
            textbox1.config(state="normal")
            textbox1.delete(0, END)
            textbox1.config(state="disabled")

        def select1():
            selected1 = tree1.focus()
            # Grab record values
            values1 = tree1.item(selected1, 'values')
            txt_config(name_box1, values1, 0)
            txt_config(cost_box1, values1, 1)

        def clicker1(e):
            txt_config_delete(name_box1)
            txt_config_delete(cost_box1)
            try:
                select1()
            except IndexError:
                pass

        def select2():
            selected2 = tree2.focus()
            # Grab record values
            values2 = tree2.item(selected2, 'values')
            txt_config(name_box2, values2, 0)
            txt_config(cost_box2, values2, 1)

        def clicker2(e):
            txt_config_delete(name_box2)
            txt_config_delete(cost_box2)
            try:
                select2()
            except IndexError:
                pass

        def select3():
            selected3 = tree3.focus()
            # Grab record values
            values3 = tree3.item(selected3, 'values')
            txt_config(name_box3, values3, 0)
            txt_config(cost_box3, values3, 1)

        def clicker3(e):
            txt_config_delete(name_box3)
            txt_config_delete(cost_box3)
            try:
                select3()
            except IndexError:
                pass

        def select4():
            selected4 = tree4.focus()
            # Grab record values
            values4 = tree4.item(selected4, 'values')
            txt_config(name_box4, values4, 0)
            txt_config(cost_box4, values4, 1)

        def clicker4(e):
            txt_config_delete(name_box4)
            txt_config_delete(cost_box4)
            try:
                select4()
            except IndexError:
                pass

        def select5():
            selected5 = tree5.focus()
            # Grab record values
            values5 = tree5.item(selected5, 'values')
            txt_config(id_box, values5, 2)

        def clicker5(e):
            txt_config_delete(id_box)
            try:
                select5()
            except IndexError:
                pass
            except AttributeError:
                pass

        def scrollbar_properties(scrollbar_x, scrollbar_y, tree):
            scrollbar_y.config(command=tree.yview)
            scrollbar_y.pack(side=RIGHT, fill=Y)
            scrollbar_x.config(command=tree.xview)
            scrollbar_x.pack(side=BOTTOM, fill=X)

        def tree_properties(tree, text1, text2, text3):
            if text3 == "":
                tree.heading(text1, text=text1, anchor=W)
                tree.heading(text2, text=text2, anchor=W)
                tree.column('#0', stretch=NO, minwidth=0, width=0)
                tree.column('#1', stretch=NO, minwidth=0, width=150)
                tree.pack()
            else:
                tree.heading(text1, text=text1, anchor=W)
                tree.heading(text2, text=text2, anchor=W)
                tree.heading(text3, text=text3, anchor=W)
                tree.column('#0', stretch=NO, minwidth=0, width=0)
                tree.column('#1', stretch=NO, minwidth=0, width=150)
                tree.column('#2', stretch=NO, minwidth=0, width=150)
                tree.pack()

        # initialize Tkinter
        new = Tk()

        # initialize title of Window
        new.title("Restaurant Management System")
        w = 500
        h = 200
        # specifies the window's dimensions
        # get screen width and height
        ws = new.winfo_screenwidth()  # width of the screen
        hs = new.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        new.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # initializes Notebook widget for the collection of windows and displays it one at a time.
        new_window = ttk.Notebook(new)

        # initializes the Frames(Rectangular Windows) for other widgets
        tab2 = ttk.Frame(new_window)
        tab3 = ttk.Frame(new_window)
        tab4 = ttk.Frame(new_window)
        tab5 = ttk.Frame(new_window)
        tab6 = ttk.Frame(new_window)

        # add tabs to whichever frame
        self.create_window(new_window, tab2, "Appetizers")
        self.create_window(new_window, tab3, "Main Dish")
        self.create_window(new_window, tab4, "Desserts")
        self.create_window(new_window, tab5, "Beverages")
        self.create_window(new_window, tab6, "Bill")

        # creating frame
        top_view_form1 = Frame(tab2, width=600, bd=1, relief=SOLID)
        top_view_form1.pack(side=TOP, fill=X)
        left_view_form1 = Frame(tab2, width=600)
        left_view_form1.pack(side=LEFT, fill=Y)
        mid_view_form1 = Frame(tab2, width=600)
        mid_view_form1.pack(side=RIGHT)
        top_view_form2 = Frame(tab3, width=600, bd=1, relief=SOLID)
        top_view_form2.pack(side=TOP, fill=X)
        left_view_form2 = Frame(tab3, width=600)
        left_view_form2.pack(side=LEFT, fill=Y)
        mid_view_form2 = Frame(tab3, width=600)
        mid_view_form2.pack(side=RIGHT)
        top_view_form3 = Frame(tab4, width=600, bd=1, relief=SOLID)
        top_view_form3.pack(side=TOP, fill=X)
        left_view_form3 = Frame(tab4, width=600)
        left_view_form3.pack(side=LEFT, fill=Y)
        mid_view_form3 = Frame(tab4, width=600)
        mid_view_form3.pack(side=RIGHT)
        top_view_form4 = Frame(tab5, width=600, bd=1, relief=SOLID)
        top_view_form4.pack(side=TOP, fill=X)
        left_view_form4 = Frame(tab5, width=600)
        left_view_form4.pack(side=LEFT, fill=Y)
        mid_view_form4 = Frame(tab5, width=600)
        mid_view_form4.pack(side=RIGHT)
        top_view_form5 = Frame(tab6, width=600, bd=1, relief=SOLID)
        top_view_form5.pack(side=TOP, fill=X)
        left_view_form5 = Frame(tab6, width=600)
        left_view_form5.pack(side=LEFT, fill=Y)
        mid_view_form5 = Frame(tab6, width=600)
        mid_view_form5.pack(side=RIGHT)

        self.create_label(top_view_form1, "Appetizers", 600, "#1C2833", "white", 15, TOP, N)
        self.create_label(left_view_form1, "What will you Order?", None, None, None, 15, TOP, W)
        self.create_label(top_view_form2, "Main Dish", 600, "#1C2833", "white", 15, TOP, N)
        self.create_label(left_view_form2, "What will you Order?", None, None, None, 15, TOP, W)
        self.create_label(top_view_form3, "Desserts", 600, "#1C2833", "white", 15, TOP, N)
        self.create_label(left_view_form3, "What will you Order?", None, None, None, 15, TOP, W)
        self.create_label(top_view_form4, "Beverages", 600, "#1C2833", "white", 15, TOP, N)
        self.create_label(left_view_form4, "What will you Order?", None, None, None, 15, TOP, W)
        self.create_label(left_view_form4, "Name", None, None, None, 8, None, W)
        self.create_label(top_view_form5, "Bill", 600, "#1C2833", "white", 15, TOP, N)
        self.create_label(left_view_form5, "What will you Order?", None, None, None, 15, TOP, W)
        self.create_label(left_view_form5, "Id Number", None, None, None, 8, None, W)

        # Name - Appetizers
        self.create_label(left_view_form1, "Name", None, None, None, 8, None, W)
        name_box1 = Entry(left_view_form1)
        name_box1.pack(anchor=W)
        name_box1.config(state="disabled")

        # Cost - Appetizers
        self.create_label(left_view_form1, "Cost", None, None, None, 8, None, W)
        cost_box1 = Entry(left_view_form1)
        cost_box1.pack(anchor=W)
        cost_box1.config(state="disabled")

        # Name - Main Dish
        self.create_label(left_view_form2, "Name", None, None, None, 8, None, W)
        name_box2 = Entry(left_view_form2)
        name_box2.pack(anchor=W)
        name_box2.config(state="disabled")

        # Cost - Main Dish
        self.create_label(left_view_form2, "Cost", None, None, None, 8, None, W)
        cost_box2 = Entry(left_view_form2)
        cost_box2.pack(anchor=W)
        cost_box2.config(state="disabled")

        # Name - Desserts
        self.create_label(left_view_form3, "Name", None, None, None, 8, None, W)
        name_box3 = Entry(left_view_form3)
        name_box3.pack(anchor=W)
        name_box3.config(state="disabled")

        # Cost - Desserts
        self.create_label(left_view_form3, "Cost", None, None, None, 8, None, W)
        cost_box3 = Entry(left_view_form3)
        cost_box3.pack(anchor=W)
        cost_box3.config(state="disabled")

        # Name - Beverages
        name_box4 = Entry(left_view_form4)
        name_box4.pack(anchor=W)
        name_box4.config(state="disabled")

        # Cost - Beverages
        self.create_label(left_view_form4, "Cost", None, None, None, 8, None, W)
        cost_box4 = Entry(left_view_form4)
        cost_box4.pack(anchor=W)
        cost_box4.config(state="disabled")

        # ID - Bill
        id_box = Entry(left_view_form5)
        id_box.pack(anchor=W)
        id_box.config(state="disabled")

        # Cost - Bill
        self.create_label(left_view_form5, "Cost", None, None, None, 8, None, W)
        conn = sqlite3.connect("Restaurant.db")
        c = conn.cursor()
        c.execute("SELECT cost, oid FROM Bill WHERE name or cost IS NOT NULL")
        data = c.fetchall()
        for row in data:
            total += row[0]
        # Entry boxes
        cost_box5 = Label(left_view_form5, text=total)
        cost_box5.pack(anchor=W)

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

        tree5 = ttk.Treeview(mid_view_form5, columns=("Name", "Cost", "Number"),
                             selectmode="extended", height=100, yscrollcommand=scroll_bar_y5.set,
                             xscrollcommand=scroll_bar_x5.set)

        # edit properties of the scrollbars
        scrollbar_properties(scroll_bar_x1, scroll_bar_y1, tree1)
        scrollbar_properties(scroll_bar_x2, scroll_bar_y2, tree2)
        scrollbar_properties(scroll_bar_x3, scroll_bar_y3, tree3)
        scrollbar_properties(scroll_bar_x4, scroll_bar_y4, tree4)
        scrollbar_properties(scroll_bar_x5, scroll_bar_y5, tree5)

        # setting width, headings for the columns
        tree_properties(tree1, "Name", "Cost", "")
        tree_properties(tree2, "Name", "Cost", "")
        tree_properties(tree3, "Name", "Cost", "")
        tree_properties(tree4, "Name", "Cost", "")
        tree_properties(tree5, "Number", "Name", "Cost")

        # creating buttons
        self.create_button(left_view_form1, new, "Back",  2, LEFT, W, var1, var2, var3, None, None, tree1, tree2, tree3,
                           tree4, tree5)
        self.create_button(left_view_form1, new, "Order", 3, LEFT, W, var1, var2, var3, name_box1, cost_box1, tree1,
                           tree2, tree3, tree4, tree5)

        self.create_button(left_view_form2, new, "Back", 2, LEFT, W, var1, var2, var3, None, None, tree1, tree2, tree3,
                           tree4, tree5)
        self.create_button(left_view_form2, new, "Order", 3, LEFT, W, var1, var2, var3, name_box2, cost_box2, tree1,
                           tree2, tree3, tree4, tree5)

        self.create_button(left_view_form3, new, "Back", 2, LEFT, W, var1, var2, var3, None, None, tree1, tree2, tree3,
                           tree4, tree5)
        self.create_button(left_view_form3, new, "Order", 3, LEFT, W, var1, var2, var3, name_box3, cost_box3, tree1,
                           tree2, tree3, tree4, tree5)

        self.create_button(left_view_form4, new, "Back", 2, LEFT, W, var1, var2, var3, None, None, tree1, tree2, tree3,
                           tree4, tree5)
        self.create_button(left_view_form4, new, "Order", 3, LEFT, W, var1, var2, var3, name_box4, cost_box4, tree1,
                           tree2, tree3, tree4, tree5)

        self.create_button(left_view_form5, new, "Delete", 4, LEFT, W, var1, var2, var3, id_box, None, tree1, tree2,
                           tree3, tree4, tree5)
        self.create_button(left_view_form5, new, "Check Out", 5, LEFT, W, var1, var2, var3, id_box, None, tree1,
                           tree2, tree3, tree4, tree5)

        self.remove_record(tree1, tree2, tree3, tree4, tree5, var1, var2, var3)
        self.bind(tree1, clicker1)
        self.bind(tree2, clicker2)
        self.bind(tree3, clicker3)
        self.bind(tree4, clicker4)
        self.bind(tree5, clicker5)

        new.resizable(False, False)
        new.mainloop()

    def display_data(self, tree1, tree2, tree3, tree4, tree5):
        self.reset_tree(tree1, tree2, tree3, tree4, tree5)

        # connect to database
        conn = sqlite3.connect('Restaurant.db')

        # select query
        cursor1 = conn.execute("SELECT name, cost FROM Appetizers")
        cursor2 = conn.execute("SELECT name, cost FROM Main_Dish")
        cursor3 = conn.execute("SELECT name, cost FROM Desserts")
        cursor4 = conn.execute("SELECT name, cost FROM Beverages")
        cursor5 = conn.execute("SELECT name, cost, oid FROM Bill")

        # fetch all data from database and loop for displaying all data in GUI
        self.retrieve_data(cursor1, tree1)
        self.retrieve_data(cursor2, tree2)
        self.retrieve_data(cursor3, tree3)
        self.retrieve_data(cursor4, tree4)
        self.retrieve_data(cursor5, tree5)

        conn.close()

    def remove_record(self, tree1, tree2, tree3, tree4, tree5, var1, var2, var3):
        # initializes a, b, and c
        a = var1.get()
        b = var2.get()
        c = var3.get()
        self.reset_tree(tree1, tree2, tree3, tree4, tree5)

        # open database
        conn = sqlite3.connect('Restaurant.db')
        if a != "" and b == "" and c == "":
            cursor1 = conn.execute("""SELECT name, cost FROM Appetizers WHERE allergen1 NOT LIKE :a
                            AND allergen2 NOT LIKE :a;""", {"a": a})

            self.retrieve_data(cursor1, tree1)
            # loop for displaying all records into GUI

            cursor2 = conn.execute("""SELECT name, cost FROM Main_Dish WHERE allergen1 NOT LIKE :a
                            AND allergen2 NOT LIKE :a;""", {"a": a})
            self.retrieve_data(cursor2, tree2)

            cursor3 = conn.execute("""SELECT name, cost FROM Desserts WHERE allergen1 NOT LIKE :a
                                        AND allergen2 NOT LIKE :a;""", {"a": a})
            self.retrieve_data(cursor3, tree3)

            cursor4 = conn.execute("""SELECT name, cost FROM Beverages WHERE allergen1 NOT LIKE :a
                                        AND allergen2 NOT LIKE :a;""", {"a": a})
            self.retrieve_data(cursor4, tree4)

            cursor5 = conn.execute("SELECT name, cost, oid FROM Bill WHERE name or cost IS NOT NULL")
            self.retrieve_data(cursor5, tree5)

        elif a == "" and b != "" and c == "":
            # select query with where clause
            cursor1 = conn.execute("""SELECT name, cost FROM Appetizers WHERE allergen1 NOT LIKE :a
                AND allergen2 NOT LIKE :a;""", {"a": b})
            self.retrieve_data(cursor1, tree1)

            cursor2 = conn.execute("""SELECT name, cost FROM Main_Dish WHERE allergen1 NOT LIKE :a
                AND allergen2 NOT LIKE :a;""", {"a": b})
            self.retrieve_data(cursor2, tree2)

            cursor3 = conn.execute("""SELECT name, cost FROM Desserts WHERE allergen1 NOT LIKE :a
                AND allergen2 NOT LIKE :a;""", {"a": b})
            self.retrieve_data(cursor3, tree3)

            cursor4 = conn.execute("""SELECT name, cost FROM Beverages WHERE allergen1 NOT LIKE :a
                AND allergen2 NOT LIKE :a;""", {"a": b})
            self.retrieve_data(cursor4, tree4)

            cursor5 = conn.execute("SELECT name, cost, oid FROM Bill WHERE name or cost IS NOT NULL")
            self.retrieve_data(cursor5, tree5)

        elif a == "" and b == "" and c != "":
            # select query with where clause
            cursor1 = conn.execute("""SELECT name, cost FROM Appetizers WHERE allergen1 NOT LIKE :a
                AND allergen2 NOT LIKE :a;""", {"a": c})
            self.retrieve_data(cursor1, tree1)

            cursor2 = conn.execute("""SELECT name, cost FROM Main_Dish WHERE allergen1 NOT LIKE :a
                AND allergen2 NOT LIKE :a;""", {"a": c})
            self.retrieve_data(cursor2, tree2)

            cursor3 = conn.execute("""SELECT name, cost FROM Desserts WHERE allergen1 NOT LIKE :a
                AND allergen2 NOT LIKE :a;""", {"a": c})
            self.retrieve_data(cursor3, tree3)

            cursor4 = conn.execute("""SELECT name, cost FROM Beverages WHERE allergen1 NOT LIKE :a
                AND allergen2 NOT LIKE :a;""", {"a": c})
            self.retrieve_data(cursor4, tree4)

            cursor5 = conn.execute("SELECT name, cost, oid FROM Bill WHERE name or cost IS NOT NULL")
            self.retrieve_data(cursor5, tree5)

        elif a != "" and b != "" and c == "":
            # select query with where clause
            cursor1 = conn.execute("""SELECT name, cost FROM Appetizers WHERE (allergen1 NOT LIKE :a 
                        AND allergen1 NOT LIKE :b)
                        AND (allergen2 NOT LIKE :a
                        AND allergen2 NOT LIKE :b)""",
                                   {"a": a, "b": b})
            self.retrieve_data(cursor1, tree1)

            cursor2 = conn.execute("""SELECT name, cost FROM Main_Dish WHERE (allergen1 NOT LIKE :a 
                        AND allergen1 NOT LIKE :b)
                        AND (allergen2 NOT LIKE :a
                        AND allergen2 NOT LIKE :b)""",
                                   {"a": a, "b": b})
            self.retrieve_data(cursor2, tree2)

            cursor3 = conn.execute("""SELECT name, cost FROM Desserts WHERE (allergen1 NOT LIKE :a 
                        AND allergen1 NOT LIKE :b)
                        AND (allergen2 NOT LIKE :a
                        AND allergen2 NOT LIKE :b)""",
                                   {"a": a, "b": b})
            self.retrieve_data(cursor3, tree3)

            cursor4 = conn.execute("""SELECT name, cost FROM Beverages WHERE (allergen1 NOT LIKE :a 
                        AND allergen1 NOT LIKE :b)
                        AND (allergen2 NOT LIKE :a
                        AND allergen2 NOT LIKE :b)""",
                                   {"a": a, "b": b})
            self.retrieve_data(cursor4, tree4)

            cursor5 = conn.execute("SELECT name, cost, oid FROM Bill WHERE name or cost IS NOT NULL")
            self.retrieve_data(cursor5, tree5)

        elif a != "" and b == "" and c != "":
            # select query with where clause
            cursor1 = conn.execute("""SELECT name, cost FROM Appetizers WHERE (allergen1 NOT LIKE :a 
                        AND allergen1 NOT LIKE :b)
                        AND (allergen2 NOT LIKE :a
                        AND allergen2 NOT LIKE :b)""",
                                   {"a": a, "b": c})
            self.retrieve_data(cursor1, tree1)

            cursor2 = conn.execute("""SELECT name, cost FROM Main_Dish WHERE (allergen1 NOT LIKE :a 
                        AND allergen1 NOT LIKE :b)
                        AND (allergen2 NOT LIKE :a
                        AND allergen2 NOT LIKE :b)""",
                                   {"a": a, "b": c})
            self.retrieve_data(cursor2, tree2)

            cursor3 = conn.execute("""SELECT name, cost FROM Desserts WHERE (allergen1 NOT LIKE :a 
                        AND allergen1 NOT LIKE :b)
                        AND (allergen2 NOT LIKE :a
                        AND allergen2 NOT LIKE :b)""",
                                   {"a": a, "b": c})
            self.retrieve_data(cursor3, tree3)

            cursor4 = conn.execute("""SELECT name, cost FROM Beverages WHERE (allergen1 NOT LIKE :a 
                        AND allergen1 NOT LIKE :b)
                        AND (allergen2 NOT LIKE :a
                        AND allergen2 NOT LIKE :b)""",
                                   {"a": a, "b": c})
            self.retrieve_data(cursor4, tree4)

            cursor5 = conn.execute("SELECT name, cost, oid FROM Bill WHERE name or cost IS NOT NULL")
            self.retrieve_data(cursor5, tree5)

        elif a == "" and b != "" and c != "":
            # select query with where clause
            cursor1 = conn.execute("""SELECT name, cost FROM Appetizers WHERE (allergen1 NOT LIKE :a 
                        AND allergen1 NOT LIKE :b)
                        AND (allergen2 NOT LIKE :a
                        AND allergen2 NOT LIKE :b)""",
                                   {"a": b, "b": c})
            self.retrieve_data(cursor1, tree1)

            cursor2 = conn.execute("""SELECT name, cost FROM Main_Dish WHERE (allergen1 NOT LIKE :a 
                        AND allergen1 NOT LIKE :b)
                        AND (allergen2 NOT LIKE :a
                        AND allergen2 NOT LIKE :b)""",
                                   {"a": b, "b": c})
            self.retrieve_data(cursor2, tree2)

            cursor3 = conn.execute("""SELECT name, cost FROM Desserts WHERE (allergen1 NOT LIKE :a 
                        AND allergen1 NOT LIKE :b)
                        AND (allergen2 NOT LIKE :a
                        AND allergen2 NOT LIKE :b)""",
                                   {"a": b, "b": c})
            self.retrieve_data(cursor3, tree3)

            cursor4 = conn.execute("""SELECT name, cost FROM Beverages WHERE (allergen1 NOT LIKE :a 
                        AND allergen1 NOT LIKE :b)
                        AND (allergen2 NOT LIKE :a
                        AND allergen2 NOT LIKE :b)""",
                                   {"a": b, "b": c})
            self.retrieve_data(cursor4, tree4)

            cursor5 = conn.execute("SELECT name, cost, oid FROM Bill WHERE name or cost IS NOT NULL")
            self.retrieve_data(cursor5, tree5)

        elif a != "" and b != "" and c != "":
            # select query with where clause
            cursor1 = conn.execute("""SELECT name, cost FROM Appetizers WHERE (allergen1 NOT LIKE :a 
            AND allergen1 NOT LIKE :b 
            AND allergen1 NOT LIKE :c)
            AND (allergen2 NOT LIKE :a 
            AND allergen2 NOT LIKE :b 
            AND allergen2 NOT LIKE :c)""", {"a": a, "b": b, "c": c, })
            self.retrieve_data(cursor1, tree1)

            cursor2 = conn.execute("""SELECT name, cost FROM Main_Dish WHERE (allergen1 NOT LIKE :a 
            AND allergen1 NOT LIKE :b 
            AND allergen1 NOT LIKE :c)
            AND (allergen2 NOT LIKE :a 
            AND allergen2 NOT LIKE :b 
            AND allergen2 NOT LIKE :c)""",
                                   {"a": a, "b": b, "c": c, })
            self.retrieve_data(cursor2, tree2)

            cursor3 = conn.execute("""SELECT name, cost FROM Desserts WHERE (allergen1 NOT LIKE :a 
            AND allergen1 NOT LIKE :b 
            AND allergen1 NOT LIKE :c)
            AND (allergen2 NOT LIKE :a 
            AND allergen2 NOT LIKE :b 
            AND allergen2 NOT LIKE :c)""", {"a": a, "b": b, "c": c})
            self.retrieve_data(cursor3, tree3)

            cursor4 = conn.execute("""SELECT name, cost FROM Beverages WHERE (allergen1 NOT LIKE :a 
            AND allergen1 NOT LIKE :b 
            AND allergen1 NOT LIKE :c)
            AND (allergen2 NOT LIKE :a 
            AND allergen2 NOT LIKE :b 
            AND allergen2 NOT LIKE :c)""",
                                   {"a": a, "b": b, "c": c, })
            self.retrieve_data(cursor4, tree4)

            cursor5 = conn.execute("SELECT name, cost, oid FROM Bill WHERE name or cost IS NOT NULL")
            self.retrieve_data(cursor5, tree5)

        else:
            self.display_data(tree1, tree2, tree3, tree4, tree5)
        conn.close()
