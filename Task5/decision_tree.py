import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

# Step 1: Load the Iris dataset from CSV
file_path = 'iris.csv'
data = pd.read_csv(file_path)
print(data.head())

X = data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values
Y = data['species'].values

#Split the dataset into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Step 2: Train the decision tree classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, Y_train)

# Step 3: Print the classification report and confusion matrix
Y_pred = clf.predict(X_test)
print("Classification Report:")
print(classification_report(Y_test, Y_pred))
print("Confusion Matrix:")
print(confusion_matrix(Y_test, Y_pred))

# Step 4: Visualize the decision tree
plt.figure(figsize=(12, 8))
plot_tree(clf, filled=True, feature_names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'], class_names=data['species'].unique())
plt.title("Decision Tree Classifier - Iris Dataset")
plt.show()
