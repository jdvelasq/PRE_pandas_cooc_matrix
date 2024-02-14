"""GitHub Classroom autograding script."""

import os

import pandas as pd

from cooc_matrix import run

run()

#
# Test 1
if not os.path.exists("cooc_table.csv"):
    raise FileNotFoundError("File 'cooc_table.csv' not found")

cooc_table = pd.read_csv("cooc_table.csv", index_col=False)
cooc_table = cooc_table.sort_values(
    by=["value", "row", "col"], ascending=[False, True, True]
).reset_index(drop=True)

assert cooc_table.loc[0, "row"] == "Data mining"
assert cooc_table.loc[0, "col"] == "Data mining"
assert cooc_table.loc[0, "value"] == 200


#
# Test 2
if not os.path.exists("cooc_matrix.csv"):
    raise FileNotFoundError("File 'cooc_matrix.csv' not found")

cooc_matrix = pd.read_csv("cooc_matrix.csv", index_col="row")

assert cooc_matrix.loc["Data mining", "Data mining"] == 200
