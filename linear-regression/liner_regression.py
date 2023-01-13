from sklearn.linear_model import LinearRegression

# X is a matrix of predictor variables
# y is a vector of response variables

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Print the coefficients (beta values)
print(model.intercept_, model.coef_)

# Make predictions using the model
y_pred = model.predict(X)

#calculate the R-squared
from sklearn.metrics import r2_score
r_squared = r2_score(y, y_pred)
print("R-squared : ", r_squared)


