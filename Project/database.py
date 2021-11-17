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
    try:
        # inserts value at specified table with corresponding columns
        c.executemany("INSERT INTO Appetizers VALUES(?,?,?,?)",
                      {
                        ("Nuts", "None", "Marinated Manchego", 350,), ("None", "None", "Patatas Bravas", 500),
                        ("None", "None", "Gazpacho", 1000)
                      })
        c.executemany("INSERT INTO Main_Dish VALUES(?,?,?,?)",
                      {
                          ("None", "None", "Rabo de Toro", 1350,), ("Seafood", "None", "Gambas al ajillo", 2500),
                          ("None", "None", "Paella Valenciana ", 1000)
                      })
        c.executemany("INSERT INTO Desserts VALUES(?,?,?,?)",
                      {
                          ("Dairy", "None", "Chocolate Churros", 350,), ("Nuts", "None", "Turron", 500),
                          ("Dairy", "None", "Flan", 1000)
                      })
        c.executemany("INSERT INTO Beverages VALUES(?,?,?,?)",
                      {
                          ("Dairy", "Nuts", "Horchata", 350), ("None", "None", "Vermouth", 500),
                          ("None", "None", "Tinto de Verano", 1000)
                      })
    # raises an exception
    except sqlite3.IntegrityError:
        pass
    finally:
        # sends the command into the sql server
        conn.commit()
        conn.close()
