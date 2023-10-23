"""
ETL-Query script using CLI.
"""

import click

from lib.extract import extract as lib_extract
from lib.transform_load import load as lib_load
from lib.query import query as lib_query


@click.group()
def commands():
    pass


@click.command()
@click.argument("filepath", type=click.Path(exists=False), required=0)
def extract(filepath):
    click.echo("Extracting data...")
    filename = filepath if filepath is not None else "/workspaces/MySQL-CRUD-Operations-CLI/data/Titanic.csv"
    lib_extract(filename)


@click.command()
@click.argument("filepath", type=click.Path(exists=False), required=0)
@click.argument("dbpath", type=click.Path(exists=False), required=0)
def load(filepath, dbpath):
    click.echo("Loading data...")
    filename = filepath if filepath is not None else "/workspaces/MySQL-CRUD-Operations-CLI/data/Titanic.csv"
    dbpath = dbpath if dbpath is not None else "/workspaces/MySQL-CRUD-Operations-CLI/data"
    lib_load(filename, dbpath)


@click.command()
@click.argument("dbpath", type=click.Path(exists=False), required=0)
@click.option("-n", prompt="Enter number of rows to query.", help="The number of rows to query.")
def query(dbpath, n):
    n = 5 if n is None else n
    dbpath = dbpath if dbpath is not None else "/workspaces/MySQL-CRUD-Operations-CLI/data/TitanicDB"
    click.echo("Querying...")
    lib_query(dbpath, n)

commands.add_command(extract)
commands.add_command(load)
commands.add_command(query)

if __name__ == "__main__":
    commands()