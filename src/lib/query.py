"""Query the database"""

import sqlite3
from prettytable import PrettyTable


def query(dbpath, n):
    """Query the database for the top n rows of the GroceryDB table"""
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TitanicDB LIMIT " + str(int(n)+1))
    rows = cursor.fetchall()[1:]
    conn.close()

    # Create a table to display the results
    table = PrettyTable()
    table.field_names = [description[0] for description in cursor.description]
    for row in rows:
        table.add_row(row)

    print("Top " + str(n) + " rows of the TitanicDB table:")
    print(table)
    return "Success"
