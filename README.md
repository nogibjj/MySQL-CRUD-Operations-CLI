# Interating with DB using SQLite3 and CLI

## About

This project aims to perform the Extract-Tranform-Load steps on a database using SQLite. The data comes from the toy dataset hosted on github - [Titanic](https://github.com/quantumsnowball/toy-datasets-collections/blob/master/titanic/titanic.csv). This repositroy contains files to perform CRUD (Create-Write-Update-Delete) operations in a SQLite Database using Python and CLI.

## User Guide

1. The first step is to install the necessary dependencies. This can be done by running this command:
```bash
make install
```
2. The second step is to perform Extract and Transform operations on the dataset. The `extract` command downloads the `Titanic.csv` data into `/data` folder from Kaggle. The `transform` command puts this data into a Database using SQLite. 
```bash
python3 src/main.py extract
python3 src/main.py transform
```
3. The third step is to query the dataset. This is shown below:
```bash
python3 src/main.py query
```
This will prompt the user to input the number of rows to query as shown below.

```bash
Enter number of rows to query.: 5
Querying...
Top 5 rows of the TitanicDB table:
+-------------+----------+--------+-----------------------------------------------------+--------+-----+-------+-------+------------------+---------+-------+----------+
| PassengerId | Survived | Pclass |                         Name                        |  Sex   | Age | SibSp | Parch |      Ticket      |   Fare  | Cabin | Embarked |
+-------------+----------+--------+-----------------------------------------------------+--------+-----+-------+-------+------------------+---------+-------+----------+
|      1      |    0     |   3    |               Braund, Mr. Owen Harris               |  male  |  22 |   1   |   0   |    A/5 21171     |   7.25  |       |    S     |
|      2      |    1     |   1    | Cumings, Mrs. John Bradley (Florence Briggs Thayer) | female |  38 |   1   |   0   |     PC 17599     | 71.2833 |  C85  |    C     |
|      3      |    1     |   3    |                Heikkinen, Miss. Laina               | female |  26 |   0   |   0   | STON/O2. 3101282 |  7.925  |       |    S     |
|      4      |    1     |   1    |     Futrelle, Mrs. Jacques Heath (Lily May Peel)    | female |  35 |   1   |   0   |      113803      |   53.1  |  C123 |    S     |
|      5      |    0     |   3    |               Allen, Mr. William Henry              |  male  |  35 |   0   |   0   |      373450      |   8.05  |       |    S     |
+-------------+----------+--------+-----------------------------------------------------+--------+-----+-------+-------+------------------+---------+-------+----------+
```


