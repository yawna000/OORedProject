import sqlite3


class Database:
    conn = sqlite3.connect("../Restaurant.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS Appetizers(
                    allergen string,
                    name string,
                    cost integer,
                    UNIQUE(name)
                );""")
    c.execute("""CREATE TABLE IF NOT EXISTS Main_Dish(
                    allergen string,
                    name string,
                    cost integer,
                    UNIQUE(name)
                    );""")
    c.execute("""CREATE TABLE IF NOT EXISTS Desserts(
                    allergen string,
                    name string,
                    cost integer,
                    UNIQUE(name)
                    );""")
    c.execute("""CREATE TABLE IF NOT EXISTS Beverages(
                    allergen string,
                    name string,
                    cost integer,
                    UNIQUE(name)
                    );""")
    try:
        c.executemany("INSERT INTO Appetizers VALUES(?,?,?)",
                      {
                        ("Nuts", "Marinated Manchego", 350,), (None, "Patatas Bravas", 500), (None, "Gazpacho", 1000)
                      })
        c.executemany("INSERT INTO Main_Dish VALUES(?,?,?)",
                      {
                          (None, "Rabo de Toro", 1350,), ("Seafood", "Gambas al ajillo", 2500),
                          (None, "Paella Valenciana ", 1000)
                      })
        c.executemany("INSERT INTO Desserts VALUES(?,?,?)",
                      {
                          ("Dairy", "Chocolate Churros", 350,), ("Nuts", "Turron", 500), ("Dairy", "Flan", 1000)
                      })
        c.executemany("INSERT INTO Beverages VALUES(?,?,?)",
                      {
                          ("Nuts and Dairy", "Horchata", 350), (None, "Vermouth", 500), (None, "Tinto de Verano", 1000)
                      })
    except sqlite3.IntegrityError:
        pass
    finally:
        conn.commit()
        conn.close()
