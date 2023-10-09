# CRUD Operations with SQLite3

[![CI](https://github.com/dhavalpotdar/MySQL-CRUD-Operations/actions/workflows/main.yml/badge.svg)](https://github.com/dhavalpotdar/MySQL-CRUD-Operations/actions/workflows/main.yml)

## About

This project aims to perform the Extract-Tranform-Load steps on a database using SQLite. The data comes from the toy dataset hosted on github - [Titanic](https://github.com/quantumsnowball/toy-datasets-collections/blob/master/titanic/titanic.csv). This repositroy contains files to perform CRUD (Create-Write-Update-Delete) operations in a SQLite Database using Python and CLI.

## Run project

1. The first step is to install the necessary dependencies. This can be done by running this command:
```bash
make install
```
2. The second step is to perform ETL operations on the dataset. 
```bash
python3 main.py --step=extract
python3 main.py --step=load
python3 main.py --step=query
```
3. CRUD Operations
`lib/CRUD.py` has the functions to perform CRUD operations on the database. The below is the sample usage:
```python
# creating table
create_table()

# create entry
last_id = get_database_dimensions()[0]
create(
    passenger_id=last_id,
    survived=?,
    pclass=?,
    name=?,
    sex=?,
    age=?,
    sibsp=?,
    parch=?,
    ticket=?,
    fare=?,
    cabin=?,
    embarked=?
)

# update an existing entry using passenger_id
update(
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
)

# delete entry using passenger_id
delete(passenger_id)
```


