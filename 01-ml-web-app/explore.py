"""A quick look at the iris dataset before we build anything."""
import pandas as pd
from sklearn.datasets import load_iris

# Load the dataset that ships inside scikit-learn.
iris = load_iris(as_frame=True)

# The measurements (our inputs) live in a table called "data".
X = iris.data
# The flower species (the answer we want to predict) lives in "target".
y = iris.target

# Put it all together into one friendly table so we can read it.
df = X.copy()
df["species"] = y.map(dict(enumerate(iris.target_names)))

print("Shape (rows, columns):", df.shape)
print("\nColumn names:")
print(list(df.columns))

print("\nFirst 5 flowers:")
print(df.head())

print("\nHow many of each species?")
print(df["species"].value_counts())

print("\nQuick summary of the measurements:")
print(df.describe().round(2))
