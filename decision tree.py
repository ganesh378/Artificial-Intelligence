from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create an instance of the DecisionTreeClassifier
clf = DecisionTreeClassifier()

# Fit the classifier to the data
clf.fit(X, y)

# Make predictions on new data
predictions = clf.predict(X)

print(predictions)
