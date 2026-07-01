"""Train a simple model on the iris dataset and check how good it is."""
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1. Load the data: X is the measurements, y is the species.
iris = load_iris(as_frame=True)
X = iris.data
y = iris.target

# 2. Split into a training set and a testing set.
#    The model learns from the training set, then we quiz it on the
#    testing set it has never seen. That is the only honest way to
#    know if it actually learned anything.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print("Flowers to learn from :", len(X_train))
print("Flowers to quiz with  :", len(X_test))

# 3. Create the model and train it. "fit" is the word for "learn".
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. Grade it on the flowers it has never seen.
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"\nAccuracy on unseen flowers: {accuracy:.0%}")

# 5. Try one prediction by hand to see it work.
sample = [[5.1, 3.5, 1.4, 0.2]]  # looks like a setosa
guess = model.predict(sample)[0]
print("Prediction for", sample[0], "->", iris.target_names[guess])
