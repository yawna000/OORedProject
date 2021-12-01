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

    def order1(self, entry_box1, cost_box1):

        # connects the database
        conn = sqlite3.connect("Restaurant.db")

        # instance which invokes methods that executes SQL Statements
        c = conn.cursor()

        c.execute("INSERT INTO Bill VALUES(:name, :cost)",
                  {
                                   "name": entry_box1.get(),
                                   "cost": cost_box1.get()
                    })
        conn.commit()
        conn.close()

    def order2(self, entry_box2, cost_box2):

        # connects the database
        conn = sqlite3.connect("Restaurant.db")

        # instance which invokes methods that executes SQL Statements
        c = conn.cursor()

        c.execute("INSERT INTO Bill VALUES(:name, :cost)",
                  {
                      "name": entry_box2.get(),
                      "cost": cost_box2.get()
                  })
        conn.commit()
        conn.close()

    def order3(self, entry_box3, cost_box3):

        # connects the database
        conn = sqlite3.connect("Restaurant.db")

        # instance which invokes methods that executes SQL Statements
        c = conn.cursor()

        c.execute("INSERT INTO Bill VALUES(:name, :cost)",
                  {
                      "name": entry_box3.get(),
                      "cost": cost_box3.get()
                  })
        conn.commit()
        conn.close()

    def order4(self, entry_box4, cost_box4):

        # connects the database
        conn = sqlite3.connect("Restaurant.db")

        # instance which invokes methods that executes SQL Statements
        c = conn.cursor()

        c.execute("INSERT INTO Bill VALUES(:name, :cost)",
                  {
                      "name": entry_box4.get(),
                      "cost": cost_box4.get()
                  })
        conn.commit()
        conn.close()

    def order5(self, entry_box5, cost_box5):

        # connects the database
        conn = sqlite3.connect("Restaurant.db")

        # instance which invokes methods that executes SQL Statements
        c = conn.cursor()

        c.execute("INSERT INTO Bill VALUES(:name, :cost)",
                  {
                      "name": entry_box5.get(),
                      "cost": cost_box5.get()
                  })
        conn.commit()
        conn.close()

    def print_bill(self):
        # connects the database
        conn = sqlite3.connect("Restaurant.db")

        # instance which invokes methods that executes SQL Statements
        c = conn.cursor()

        c.execute("DELETE from Bill")
        conn.commit()
        conn.close()

    def remove(self, entry_box5):
        # connects the database
        conn = sqlite3.connect("Restaurant.db")

        # instance which invokes methods that executes SQL Statements
        c = conn.cursor()

        c.execute("DELETE from Bill WHERE oid= " + entry_box5.get())

        conn.commit()
        conn.close()
