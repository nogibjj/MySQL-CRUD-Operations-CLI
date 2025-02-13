"""
Extract a dataset from a URL like Kaggle
 or data.gov. JSON or CSV formats tend to work well

food dataset
"""
import requests


def extract(
    file_path,
    url="https://raw.githubusercontent.com/quantumsnowball/toy-datasets-collections/master/titanic/titanic.csv",
):
    """ "Extract a url to a file path"""
    with requests.get(url, timeout=1000) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path
