"""
Transforms and Loads data into the local SQLite3 database
"""
import sqlite3
import csv
import os


# load the csv file and insert into a new sqlite3 database
def load(dataset="/workspaces/MySQL-CRUD-Operations/data/Titanic.csv"):
    """ "Transforms and Loads data into the local SQLite3 database"""

    # prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    print(payload)
    conn = sqlite3.connect("TitanicDB.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS TitanicDB")
    c.execute(
        """CREATE TABLE TitanicDB (
                    PassengerId,
                    Survived,
                    Pclass, 
                    Name, 
                    Sex, 
                    Age, 
                    SibSp, 
                    Parch, 
                    Ticket,
                    Fare,
                    Cabin,
                    Embarked
              )"""
    )

    # insert
    c.executemany(
        """INSERT INTO TitanicDB 
                                (PassengerId,
                                 Survived,
                                 Pclass,
                                 Name,
                                 Sex,
                                 Age,
                                 SibSp,
                                 Parch,
                                 Ticket,
                                 Fare,
                                 Cabin,
                                 Embarked)
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        payload,
    )
    conn.commit()
    conn.close()
    return "TitanicDB.db"
