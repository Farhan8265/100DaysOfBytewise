import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Exercise 1: Load a simple dataset and print the first 5 rows
diabetes = datasets.load_diabetes()
diabetes_df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
print("First 5 rows of the Diabetes dataset:")
print(diabetes_df.head())

# Exercise 2: Function to return the number of features and samples
def dataset_info(data):
    samples = data.shape[0]
    features = data.shape[1]
    return samples, features

samples, features = dataset_info(diabetes_df)
print(f"\nNumber of samples: {samples}")
print(f"Number of features: {features}")

# Exercise 3: Split the dataset into training and testing sets with an 80/20 split
X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target, test_size=0.2, random_state=42)
print("\nData split into training and testing sets.")
print(f"Training set size: {X_train.shape[0]} samples")
print(f"Testing set size: {X_test.shape[0]} samples")

# Exercise 4: Explore basic statistics of the dataset
print("\nBasic statistics of the Diabetes dataset:")
print(diabetes_df.describe())

# Exercise 5: Visualize the distribution of one of the features using a histogram
plt.hist(diabetes_df['bmi'], bins=30, edgecolor='k')
plt.title('Distribution of BMI')
plt.xlabel('BMI')
plt.ylabel('Frequency')
plt.show()

# Exercise 6: Python script to create a list of 10 numbers and compute their mean
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mean_numbers = np.mean(numbers)
print(f"\nMean of the list of numbers: {mean_numbers}")

# Exercise 7: Function to return count, mean, median, and standard deviation of a list
def list_stats(numbers):
    stats = {
        'count': len(numbers),
        'mean': np.mean(numbers),
        'median': np.median(numbers),
        'std_dev': np.std(numbers)
    }
    return stats

number_stats = list_stats(numbers)
print(f"\nStatistics of the list of numbers: {number_stats}")

# Exercise 8: Generate a 5x5 matrix of random numbers and print it
random_matrix = np.random.rand(5, 5)
print("\n5x5 Matrix of random numbers:")
print(random_matrix)

# Exercise 9: Load a CSV file into a Pandas DataFrame and print summary statistics for each column
df = pd.read_csv('data.csv')
print("\nSummary statistics for each column in the CSV file:")
print(df.describe())

# Exercise 10: Implement a simple linear regression model using Scikit-Learn and print the model coefficients
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f"\nLinear Regression Model Coefficients: {model.coef_}")
print(f"Mean Squared Error: {mse}")

