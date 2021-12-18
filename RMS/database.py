from tkinter import messagebox
import sqlite3


class Database:
    # connects the database
    conn = sqlite3.connect("Restaurant.db")

    # instance which invokes methods that executes SQL Statements
    c = conn.cursor()

    # creates a table
    c.execute("""CREATE TABLE IF NOT EXISTS Appetizers(
                    allergen1 string,
                    allergen2 string,
                    name string,
                    cost integer,
                    UNIQUE(name)
                );""")

    c.execute("""CREATE TABLE IF NOT EXISTS Main_Dish(
                    allergen1 string,
                    allergen2 string,
                    name string,
                    cost integer,
                    UNIQUE(name)
                    );""")

    c.execute("""CREATE TABLE IF NOT EXISTS Desserts(
                    allergen1 string,
                    allergen2 string,
                    name string,
                    cost integer,
                    UNIQUE(name)
                    );""")

    c.execute("""CREATE TABLE IF NOT EXISTS Beverages(
                    allergen1 string,
                    allergen2 string,
                    name string,
                    cost integer,
                    UNIQUE(name)
                    );""")

    c.execute("""CREATE TABLE IF NOT EXISTS Bill(
                    name string,
                    cost integer
                    );""")

    try:
        # inserts value at specified table with corresponding columns
        c.executemany("INSERT INTO Appetizers VALUES(?,?,?,?)",
                      {
                          ("Nuts", "None", "Marinated Manchego", 350,), ("None", "None", "Patatas Bravas", 500),
                          ("None", "None", "Gazpacho", 1000), ("Seafood", "None", "Crab Cakes", 850),
                          ("Dairy", "None", "Cheese Sticks", 400), ("Dairy", "None", "Dinner Rolls", 300)
                      })
        c.executemany("INSERT INTO Main_Dish VALUES(?,?,?,?)",
                      {
                          ("None", "None", "Rabo de Toro", 1350,), ("Seafood", "None", "Gambas al ajillo", 2500),
                          ("None", "None", "Paella Valenciana ", 1000), ("Seafood", "None", "Baked Salmon", 2300),
                          ("Dairy", "None", "Cheese Ravioli", 1200), ("None", "None", "Steak", 2500)
                      })
        c.executemany("INSERT INTO Desserts VALUES(?,?,?,?)",
                      {
                          ("Dairy", "None", "Chocolate Churros", 350,), ("Nuts", "None", "Turron", 500),
                          ("Dairy", "None", "Flan", 1000), ("Dairy", "None", "Tiramisu", 400),
                          ("None", "None", "Berry Tart", 800), ("None", "None", "Sorbet", 600)
                      })
        c.executemany("INSERT INTO Beverages VALUES(?,?,?,?)",
                      {
                          ("Dairy", "Nuts", "Horchata", 350), ("None", "None", "Vermouth", 500),
                          ("None", "None", "Tinto de Verano", 1000), ("None", "None", "Soda", 150),
                          ("None", "None", "Juice", 200), ("None", "None", "Sparkling Water", 100)
                      })
        # raises an exception
    except sqlite3.IntegrityError:
        pass
    finally:
        # sends the command into the sql server
        conn.commit()
        conn.close()

    def order(self, entry_box, cost_box):
        try:
            if str(entry_box.get()) != "" or int(cost_box.get()) != 0:
                # connects the database
                conn = sqlite3.connect("Restaurant.db")

                # instance which invokes methods that execute SQL Statements
                c = conn.cursor()

                c.execute("INSERT INTO Bill VALUES(:name, :cost)",
                          {
                              "name": entry_box.get(),
                              "cost": cost_box.get()})
                conn.commit()
                conn.close()
            else:
                messagebox.showerror("Error", "Cannot Accept Empty Values")
        except ValueError:
            messagebox.showerror("Error", "Cannot Accept Empty Value")

    def print_bill(self, root):
        # connects the database
        conn = sqlite3.connect("Restaurant.db")

        # instance which invokes methods that executes SQL Statements
        c = conn.cursor()
        prompt = messagebox.askquestion("Checkout?", "Are you sure?")
        if prompt == "yes":
            c.execute("DELETE from Bill")
            root.destroy()
        else:
            messagebox.showinfo('Return', 'You will now return to the application screen')
        conn.commit()
        conn.close()

    def remove(self, oid):
        try:
            # connects the database
            conn = sqlite3.connect("Restaurant.db")
            # instance which invokes methods that executes SQL Statements
            c = conn.cursor()
            c.execute("DELETE from Bill WHERE oid= " + oid.get())
            conn.commit()
            conn.close()

        except sqlite3.OperationalError:
            messagebox.showerror("Error", "Cannot Accept Empty Value")

    def add(self, allergy1, allergy2, name, cost, type):
        try:
            # connects the database
            conn = sqlite3.connect("Restaurant.db")
            # instance which invokes methods that executes SQL Statements
            c = conn.cursor()
            if int(type) == 1:
                c.execute("INSERT INTO Appetizers VALUES(:allergen1, :allergen2, :name, :cost)",
                          {
                              "allergen1": allergy1.get(),
                              "allergen2": allergy2.get(),
                              "name": name.get(),
                              "cost": cost.get()
                          })
            elif int(type) == 2:
                c.execute("INSERT INTO Main_Dish VALUES(:allergen1, :allergen2, :name, :cost)",
                          {
                              "allergen1": allergy1.get(),
                              "allergen2": allergy2.get(),
                              "name": name.get(),
                              "cost": cost.get()
                          })
            elif int(type) == 3:
                c.execute("INSERT INTO Desserts VALUES(:allergen1, :allergen2, :name, :cost)",
                          {
                              "allergen1": allergy1.get(),
                              "allergen2": allergy2.get(),
                              "name": name.get(),
                              "cost": cost.get()
                          })
            elif int(type) == 4:
                c.execute("INSERT INTO Beverages VALUES(:allergen1, :allergen2, :name, :cost)",
                          {
                              "allergen1": allergy1.get(),
                              "allergen2": allergy2.get(),
                              "name": name.get(),
                              "cost": cost.get()
                          })
            else:
                pass

        except sqlite3.OperationalError:
            messagebox.showerror("Error", "Cannot Accept Empty Value")
        finally:
            conn.commit()
            conn.close()

    def delete(self, oid, menu):
        # connects the database
        conn = sqlite3.connect("Restaurant.db")
        # instance which invokes methods that executes SQL Statements
        c = conn.cursor()
        if menu == 1:
            c.execute("DELETE from Appetizers WHERE oid= " + oid.get())
        elif menu == 2:
            c.execute("DELETE from Main_Dish WHERE oid= " + oid.get())
        elif menu == 3:
            c.execute("DELETE from Desserts WHERE oid= " + oid.get())
        elif menu == 4:
            c.execute("DELETE from beverages WHERE oid= " + oid.get())
        conn.commit()
        conn.close()
