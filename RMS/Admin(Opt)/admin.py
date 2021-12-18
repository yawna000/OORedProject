from tkinter import *
from tkinter import ttk
from database import *


class Admin(Database):
    def __init__(self):
        self.open_window()

    def create_button(self, frame, text, a, side, anchor, allergy1, allergy2, name, cost, type, oid, menu, tree1,
                      tree2, tree3, tree4):
        if name != "":
            if a == 0:
                ttk.Button(frame, text=text, command=lambda: [self.add(allergy1, allergy2, name, cost, type),
                                                              self.reset_tree(tree1, tree2, tree3, tree4),
                                                              self.display_data(tree1, tree2, tree3, tree4)])\
                    .pack(side=side, anchor=anchor)
            elif a == 1:
                ttk.Button(frame, text=text, command=lambda: [self.delete(oid, menu),
                                                              self.reset_tree(tree1, tree2, tree3, tree4),
                                                              self.display_data(tree1, tree2, tree3, tree4)])\
                    .pack(side=side, anchor=anchor)
        else:
            messagebox.showerror("Error", "Cannot Accept Empty Value")

    def create_label(self, tab, text, width, bg, fg, size, x, y):
        Label(tab, text=text, font=('verdana', size), width=width, bg=bg, fg=fg).pack(side=x, anchor=y)

    def create_checkbutton(self, frame, variable, text, on, off, x, y):
        checkbutton = ttk.Checkbutton(frame, variable=variable, text=text, onvalue=on, offvalue=off)
        checkbutton.place(x=x, y=y)

    def create_window(self, window, frame, text):
        window.add(frame, text=text)
        window.pack(expand=1, fill="both")

    def reset_tree(self, tree1, tree2, tree3, tree4):
        # clearing current display data
        tree1.delete(*tree1.get_children())
        tree2.delete(*tree2.get_children())
        tree3.delete(*tree3.get_children())
        tree4.delete(*tree4.get_children())

    def retrieve_data(self, cursor, tree):
        # fetch all matching records and loop for displaying all records into GUI
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=data)
        cursor.close()

    def bind(self, tree, clicker):
        tree.bind("<Double-1>", clicker)
        tree.bind("<ButtonRelease-1>", clicker)

    def open_window(self):
        def txt_config(textbox1, values, index1):
            # inserts value and configure text boxes
            textbox1.config(state="normal")
            textbox1.insert(0, values[index1])

        def txt_config_delete(textbox1):
            textbox1.config(state="normal")
            textbox1.delete(0, END)

        def select1():
            selected1 = tree1.focus()
            # Grab record values
            values1 = tree1.item(selected1, 'values')
            txt_config(oid1, values1, 0)
            txt_config(allergy1_box1, values1, 1)
            txt_config(allergy1_box2, values1, 2)
            txt_config(name_box1, values1, 3)
            txt_config(cost_box1, values1, 4)

        def clicker1(e):
            txt_config_delete(oid1)
            txt_config_delete(allergy1_box1)
            txt_config_delete(allergy1_box2)
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
            txt_config(oid2, values2, 0)
            txt_config(allergy2_box1, values2, 1)
            txt_config(allergy2_box2, values2, 2)
            txt_config(name_box1, values2, 3)
            txt_config(cost_box1, values2, 4)

        def clicker2(e):
            txt_config_delete(oid2)
            txt_config_delete(allergy2_box1)
            txt_config_delete(allergy2_box2)
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
            txt_config(oid3, values3, 0)
            txt_config(allergy3_box1, values3, 1)
            txt_config(allergy3_box2, values3, 2)
            txt_config(name_box1, values3, 3)
            txt_config(cost_box1, values3, 4)

        def clicker3(e):
            txt_config_delete(oid3)
            txt_config_delete(allergy3_box1)
            txt_config_delete(allergy3_box2)
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
            txt_config(oid4, values4, 0)
            txt_config(allergy3_box1, values4, 1)
            txt_config(allergy3_box2, values4, 2)
            txt_config(name_box1, values4, 3)
            txt_config(cost_box1, values4, 4)

        def clicker4(e):
            txt_config_delete(oid4)
            txt_config_delete(name_box4)
            txt_config_delete(cost_box4)
            txt_config_delete(allergy4_box1)
            txt_config_delete(allergy4_box2)
            try:
                select4()
            except IndexError:
                pass

        def scrollbar_properties(scrollbar_x, scrollbar_y, tree):
            scrollbar_y.config(command=tree.yview)
            scrollbar_y.pack(side=RIGHT, fill=Y)
            scrollbar_x.config(command=tree.xview)
            scrollbar_x.pack(side=BOTTOM, fill=X)

        def tree_properties(tree, text1, text2, text3, text4, text5, text6):
            if text6 == "":
                tree.heading(text1, text=text1, anchor=W)
                tree.heading(text2, text=text2, anchor=W)
                tree.heading(text3, text=text3, anchor=W)
                tree.heading(text4, text=text4, anchor=W)
                tree.heading(text5, text=text5, anchor=W)
                tree.column('#0', stretch=NO, minwidth=0, width=0)
                tree.column('#1', stretch=NO, minwidth=0, width=100)
                tree.column('#2', stretch=NO, minwidth=0, width=200)
                tree.column('#3', stretch=NO, minwidth=0, width=300)
                tree.column('#4', stretch=NO, minwidth=0, width=400)
                tree.pack()
            else:
                tree.heading(text1, text=text1, anchor=W)
                tree.heading(text2, text=text2, anchor=W)
                tree.heading(text3, text=text3, anchor=W)
                tree.heading(text4, text=text4, anchor=W)
                tree.heading(text5, text=text5, anchor=W)
                tree.column('#0', stretch=NO, minwidth=0, width=0)
                tree.column('#1', stretch=NO, minwidth=0, width=100)
                tree.column('#2', stretch=NO, minwidth=0, width=200)
                tree.column('#3', stretch=NO, minwidth=0, width=300)
                tree.column('#4', stretch=NO, minwidth=0, width=400)
                tree.pack()

        # initialize Tkinter
        new = Tk()

        # initialize title of Window
        new.title("Restaurant Management System(Admin)")
        w = 500
        h = 500
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

        # add tabs to whichever frame
        self.create_window(new_window, tab2, "Appetizers")
        self.create_window(new_window, tab3, "Main Dish")
        self.create_window(new_window, tab4, "Desserts")
        self.create_window(new_window, tab5, "Beverages")

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

        # creating label
        self.create_label(top_view_form1, "Appetizers", 600, "#1C2833", "white", 15, TOP, N)
        self.create_label(left_view_form1, "What will you Order?", None, None, None, 15, TOP, W)
        self.create_label(top_view_form2, "Main Dish", 600, "#1C2833", "white", 15, TOP, N)
        self.create_label(left_view_form2, "What will you Order?", None, None, None, 15, TOP, W)
        self.create_label(top_view_form3, "Desserts", 600, "#1C2833", "white", 15, TOP, N)
        self.create_label(left_view_form3, "What will you Order?", None, None, None, 15, TOP, W)
        self.create_label(top_view_form4, "Beverages", 600, "#1C2833", "white", 15, TOP, N)
        self.create_label(left_view_form4, "What will you Order?", None, None, None, 15, TOP, W)

        # ID - Appetizers
        self.create_label(left_view_form1, "ID", None, None, None, 8, None, W)
        oid1 = Entry(left_view_form1)
        oid1.pack(anchor=W)

        # Allergy 1 - Appetizers
        self.create_label(left_view_form1, "Allergy 1", None, None, None, 8, None, W)
        allergy1_box1 = Entry(left_view_form1)
        allergy1_box1.pack(anchor=W)

        # Allergy 2 - Appetizers
        self.create_label(left_view_form1, "Allergy 2", None, None, None, 8, None, W)
        allergy1_box2 = Entry(left_view_form1)
        allergy1_box2.pack(anchor=W)

        # Name - Appetizers
        self.create_label(left_view_form1, "Name", None, None, None, 8, None, W)
        name_box1 = Entry(left_view_form1)
        name_box1.pack(anchor=W)

        # Cost - Appetizers
        self.create_label(left_view_form1, "Cost", None, None, None, 8, None, W)
        cost_box1 = Entry(left_view_form1)
        cost_box1.pack(anchor=W)

        # ID - Main Dish
        self.create_label(left_view_form2, "ID", None, None, None, 8, None, W)
        oid2 = Entry(left_view_form2)
        oid2.pack(anchor=W)

        # Allergy 1 - Main Dish
        self.create_label(left_view_form2, "Allergy 1", None, None, None, 8, None, W)
        allergy2_box1 = Entry(left_view_form2)
        allergy2_box1.pack(anchor=W)

        # Allergy 2 - Main Dish
        self.create_label(left_view_form2, "Allergy 2", None, None, None, 8, None, W)
        allergy2_box2 = Entry(left_view_form2)
        allergy2_box2.pack(anchor=W)

        # Name - Main Dish
        self.create_label(left_view_form2, "Name", None, None, None, 8, None, W)
        name_box2 = Entry(left_view_form2)
        name_box2.pack(anchor=W)

        # Cost - Main Dish
        self.create_label(left_view_form2, "Cost", None, None, None, 8, None, W)
        cost_box2 = Entry(left_view_form2)
        cost_box2.pack(anchor=W)

        # ID - Desserts
        self.create_label(left_view_form3, "ID", None, None, None, 8, None, W)
        oid3 = Entry(left_view_form3)
        oid3.pack(anchor=W)

        # Allergy 1 - Desserts
        self.create_label(left_view_form3, "Allergy 1", None, None, None, 8, None, W)
        allergy3_box1 = Entry(left_view_form3)
        allergy3_box1.pack(anchor=W)

        # Allergy 2 - Desserts
        self.create_label(left_view_form3, "Allergy 2", None, None, None, 8, None, W)
        allergy3_box2 = Entry(left_view_form3)
        allergy3_box2.pack(anchor=W)

        # Name - Desserts
        self.create_label(left_view_form3, "Name", None, None, None, 8, None, W)
        name_box3 = Entry(left_view_form3)
        name_box3.pack(anchor=W)

        # Cost - Desserts
        self.create_label(left_view_form3, "Cost", None, None, None, 8, None, W)
        cost_box3 = Entry(left_view_form3)
        cost_box3.pack(anchor=W)

        # ID - Beverages
        self.create_label(left_view_form4, "ID", None, None, None, 8, None, W)
        oid4 = Entry(left_view_form4)
        oid4.pack(anchor=W)

        # Allergy 1 - Beverages
        self.create_label(left_view_form4, "Allergy 1", None, None, None, 8, None, W)
        allergy4_box1 = Entry(left_view_form4)
        allergy4_box1.pack(anchor=W)

        # Allergy 2 - Beverages
        self.create_label(left_view_form4, "Allergy 2", None, None, None, 8, None, W)
        allergy4_box2 = Entry(left_view_form4)
        allergy4_box2.pack(anchor=W)

        # Name - Beverages
        self.create_label(left_view_form4, "Name", None, None, None, 8, None, W)
        name_box4 = Entry(left_view_form4)
        name_box4.pack(anchor=W)

        # Cost - Beverages
        self.create_label(left_view_form4, "Cost", None, None, None, 8, None, W)
        cost_box4 = Entry(left_view_form4)
        cost_box4.pack(anchor=W)

        # setting scrollbar
        scroll_bar_x1 = Scrollbar(mid_view_form1, orient=HORIZONTAL)
        scroll_bar_y1 = Scrollbar(mid_view_form1, orient=VERTICAL)
        scroll_bar_x2 = Scrollbar(mid_view_form2, orient=HORIZONTAL)
        scroll_bar_y2 = Scrollbar(mid_view_form2, orient=VERTICAL)
        scroll_bar_x3 = Scrollbar(mid_view_form3, orient=HORIZONTAL)
        scroll_bar_y3 = Scrollbar(mid_view_form3, orient=VERTICAL)
        scroll_bar_x4 = Scrollbar(mid_view_form4, orient=HORIZONTAL)
        scroll_bar_y4 = Scrollbar(mid_view_form4, orient=VERTICAL)

        # setting tree
        tree1 = ttk.Treeview(mid_view_form1, columns=("ID", "Allergy 1", "Allergy 2", "Name", "Cost"),
                             selectmode="extended", height=100, yscrollcommand=scroll_bar_y1.set,
                             xscrollcommand=scroll_bar_x1.set)
        tree2 = ttk.Treeview(mid_view_form2, columns=("ID", "Allergy 1", "Allergy 2", "Name", "Cost"),
                             selectmode="extended", height=100, yscrollcommand=scroll_bar_y2.set,
                             xscrollcommand=scroll_bar_x2.set)
        tree3 = ttk.Treeview(mid_view_form3, columns=("ID", "Allergy 1", "Allergy 2", "Name", "Cost"),
                             selectmode="extended", height=100, yscrollcommand=scroll_bar_y3.set,
                             xscrollcommand=scroll_bar_x3.set)
        tree4 = ttk.Treeview(mid_view_form4, columns=("ID", "Allergy 1", "Allergy 2", "Name", "Cost"),
                             selectmode="extended", height=100, yscrollcommand=scroll_bar_y4.set,
                             xscrollcommand=scroll_bar_x4.set)

        # edit properties of the scrollbars
        scrollbar_properties(scroll_bar_x1, scroll_bar_y1, tree1)
        scrollbar_properties(scroll_bar_x2, scroll_bar_y2, tree2)
        scrollbar_properties(scroll_bar_x3, scroll_bar_y3, tree3)
        scrollbar_properties(scroll_bar_x4, scroll_bar_y4, tree4)

        # setting width, headings for the columns
        tree_properties(tree1, "ID", "Allergy 1", "Allergy 2", "Name", "Cost", "")
        tree_properties(tree2, "ID", "Allergy 1", "Allergy 2", "Name", "Cost", "")
        tree_properties(tree3, "ID", "Allergy 1", "Allergy 2", "Name", "Cost", "")
        tree_properties(tree4, "ID", "Allergy 1", "Allergy 2", "Name", "Cost", "")

        # creating buttons
        self.create_button(left_view_form1, "Delete", 1, LEFT, W, None, None, None, None, None, oid1, 1, tree1, tree2,
                           tree3, tree4)
        self.create_button(left_view_form1, "Add", 0, LEFT, W, allergy1_box1, allergy1_box2, name_box1,
                           cost_box1, 1, None, None, tree1, tree2, tree3, tree4)
        self.create_button(left_view_form2, "Delete", 1, LEFT, W, None, None, None, None, None, oid2, 2, tree1, tree2,
                           tree3, tree4)
        self.create_button(left_view_form2, "Add", 0, LEFT, W, allergy2_box1, allergy2_box2, name_box2,
                           cost_box2, 2, None, None, tree1, tree2, tree3, tree4)
        self.create_button(left_view_form3, "Delete", 1, LEFT, W, None, None, None, None, None, oid3, 3, tree1, tree2,
                           tree3, tree4)
        self.create_button(left_view_form3, "Add", 0, LEFT, W, allergy3_box1, allergy3_box2, name_box3,
                           cost_box3, 3, None, None, tree1, tree2, tree3, tree4)
        self.create_button(left_view_form4, "Delete", 1, LEFT, W, None, None, None, None, None, oid4, 4, tree1, tree2,
                           tree3, tree4)
        self.create_button(left_view_form4, "Add", 0, LEFT, W, allergy4_box1, allergy4_box2, name_box4,
                           cost_box4, 4, None, None, tree1, tree2, tree3, tree4)

        # binding on click effect
        self.bind(tree1, clicker1)
        self.bind(tree2, clicker2)
        self.bind(tree3, clicker3)
        self.bind(tree4, clicker4)

        self.display_data(tree1, tree2, tree3, tree4)

        new.resizable(False, False)
        new.mainloop()

    def display_data(self, tree1, tree2, tree3, tree4):
        self.reset_tree(tree1, tree2, tree3, tree4)

        # connect to database
        conn = sqlite3.connect('Restaurant.db')

        # select query
        cursor1 = conn.execute("SELECT oid, * FROM Appetizers")
        cursor2 = conn.execute("SELECT oid, * FROM Main_Dish")
        cursor3 = conn.execute("SELECT oid, * FROM Desserts")
        cursor4 = conn.execute("SELECT oid, * FROM Beverages")

        # fetch all data from database and loop for displaying all data in GUI
        self.retrieve_data(cursor1, tree1)
        self.retrieve_data(cursor2, tree2)
        self.retrieve_data(cursor3, tree3)
        self.retrieve_data(cursor4, tree4)

        conn.close()
