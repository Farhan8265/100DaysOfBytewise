import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt

# Step 1: Load the dataset
file_name = 'BostonHousing.csv'
data = pd.read_csv(file_name)
print(data.head())

#Impute missing values
imputer = SimpleImputer(strategy='mean')
data[['rm']] = imputer.fit_transform(data[['rm']])
data[['medv']] = imputer.fit_transform(data[['medv']])

# Select the features and target variable
X = data[['rm']].values
Y = data['medv'].values  

#Split the dataset into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Step 2: Train the linear regression model
model = LinearRegression()
model.fit(X_train, Y_train)

# Step 3: Print the model's coefficients and intercept
print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)

# Step 4: Predict housing prices on the test set
Y_pred = model.predict(X_test)

# Calculate and print the mean squared error
mse = mean_squared_error(Y_test, Y_pred)
print("Mean Squared Error:", mse)

# Step 5: Visualize the regression line and data points
plt.scatter(X_test, Y_test, color='blue', label='Actual Prices')
plt.plot(X_test, Y_pred, color='red', linewidth=2, label='Regression Line')
plt.xlabel('Average number of rooms per dwelling (rm)')
plt.ylabel('Median value of owner-occupied homes in $1000s (medv)')
plt.title('Actual vs Predicted Housing Prices')
plt.legend()
plt.show()
