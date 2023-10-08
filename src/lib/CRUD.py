import sqlite3


def create_table():
    """Create the TitanicDB table"""
    conn = sqlite3.connect("TitanicDB.db")
    cursor = conn.cursor()
    cursor.execute(
        """
                   CREATE TABLE IF NOT EXISTS TitanicDB 
                   (PassengerId INTEGER PRIMARY KEY AUTOINCREMENT,
                   Survived INTEGER NOT NULL, 
                   Pclass INTEGER NOT NULL, 
                   Name TEXT NOT NULL, 
                   Sex TEXT NOT NULL, 
                   Age REAL,
                   SibSp INTEGER NOT NULL, 
                   Parch INTEGER NOT NULL, 
                   Ticket TEXT,
                   Fare REAL,
                   Cabin TEXT,
                   Embarked TEXT)
                   """
    )

    cursor.execute("PRAGMA table_info(TitanicDB);")
    results = cursor.fetchall()
    column_names = [result[1] for result in results]
    print(column_names)
    conn.commit()
    conn.close()


def create(
    survived, pclass, name, sex, age, sibsp, parch, ticket, fare, cabin, embarked
):
    """Insert a new item into the TitanicDB table"""
    conn = sqlite3.connect("TitanicDB.db")
    cursor = conn.cursor()
    # cursor.execute("SELECT COUNT(*) FROM TitanicDB")
    # id = cursor.fetchone()[0] + 1
    cursor.execute(
        """INSERT INTO TitanicDB 
                   (Survived,
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
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (survived, pclass, name, sex, age, sibsp, parch, ticket, fare, cabin, embarked),
    )
    conn.commit()
    conn.close()


def read():
    """Query the database for all rows of the TitanicDB table"""
    conn = sqlite3.connect("TitanicDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TitanicDB")
    rows = cursor.fetchall()
    conn.close()

    for row in rows:
        print(row)


def update(
    survived,
    pclass,
    name,
    sex,
    age,
    sibsp,
    parch,
    ticket,
    fare,
    cabin,
    embarked,
    passenger_id,
):
    """Update an item in the TitanicDB table"""
    conn = sqlite3.connect("TitanicDB.db")
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE TitanicDB 
                         SET Survived=?,
                             Pclass=?, 
                             Name=?,
                             Sex=?, 
                             Age=?,
                             SibSp=?, 
                             Parch=?,
                             Ticket=?,
                             Fare=?,
                             Cabin=?,
                             Embarked=? 
                       WHERE PassengerId=?""",
        (
            survived,
            pclass,
            name,
            sex,
            age,
            sibsp,
            parch,
            ticket,
            fare,
            cabin,
            embarked,
            passenger_id,
        ),
    )
    conn.commit()
    conn.close()


def delete(passenger_id):
    """Delete an item from the TitanicDB table"""
    conn = sqlite3.connect("TitanicDB.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM TitanicDB WHERE PassengerId=?", (passenger_id,))
    deleted_rows = cursor.rowcount
    conn.commit()
    conn.close()
    return deleted_rows


def get_database_dimensions():
    """Get the number of rows and columns in the TitanicDB table"""
    conn = sqlite3.connect("TitanicDB.db")
    cursor = conn.cursor()
    cursor.execute(
        """SELECT COUNT(*) AS num_rows, 
                             COUNT(*) * (SELECT COUNT(*)
                        FROM pragma_table_info('TitanicDB')) AS num_cols FROM TitanicDB"""
    )
    result = cursor.fetchone()
    conn.close()
    if result:
        return result
    else:
        return None


if __name__ == "__main__":
    create_table()
    create_table()
    create(
        survived=0,
        pclass=3,
        name="Bruce Wayne",
        sex="male",
        age=23,
        sibsp=1,
        parch=0,
        ticket="PC 1996",
        fare=8.8,
        cabin="C8",
        embarked="S",
    )
    read()
