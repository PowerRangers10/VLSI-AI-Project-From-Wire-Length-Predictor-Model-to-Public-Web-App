import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the data from your master CSV file
df = pd.read_csv('master_metrics.csv')

# Define the multiple input variables (X)
# Make sure your master_metrics.csv file has the FP_ASPECT_RATIO column
X = df[['FP_CORE_UTIL', 'FP_ASPECT_RATIO']]

# Define the output variable (y)
y = df['wire_length']

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X, y)

print("Multivariable model training complete!")

# Use the trained model to make a prediction
# Let's predict wire length for a utilization of 75 and aspect ratio of 1.2
new_data = [[75, 1.2]]
predicted_wire_length = model.predict(new_data)

print(f"\nPredicted wire length for a utilization of 75% and aspect ratio of 1.2: {predicted_wire_length[0]:.2f} micrometers")

# Print the model's learned coefficients for both inputs
print("\nLearned coefficients:", model.coef_)
print("Learned intercept:", model.intercept_)

