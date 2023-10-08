"""Query the database"""

import sqlite3
from prettytable import PrettyTable


def query():
    """Query the database for the top 5 rows of the GroceryDB table"""
    conn = sqlite3.connect("TitanicDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TitanicDB LIMIT 5")
    rows = cursor.fetchall()
    conn.close()

    # Create a table to display the results
    table = PrettyTable()
    table.field_names = [description[0] for description in cursor.description]
    for row in rows:
        table.add_row(row)

    print("Top 5 rows of the GroceryDB table:")
    print(table)
    return "Success"
