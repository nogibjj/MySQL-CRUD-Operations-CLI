"""
ETL-Query script
"""

import argparse

from lib.extract import extract
from lib.transform_load import load
from lib.query import query

parser = argparse.ArgumentParser()
parser.add_argument("--step", choices=["extract", "load", "query"])
args = parser.parse_args()

if args.step == "extract":
    print("Extracting data...")
    extract()

elif args.step == "load":
    print("Transforming and loading data...")
    load()

elif args.step == "query":
    print("Querying data...")
    query()
