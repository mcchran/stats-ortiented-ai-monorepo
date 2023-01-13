import numpy as np

def likelihood(X, y, beta):
    # X is a matrix of predictor variables
    # y is a vector of response variables
    # beta is a vector of parameters for the linear regression model
    # Assumes a normal distribution for the errors
    n = len(y)
    y_pred = X @ beta
    sigma = 1 # Assume a known variance
    likelihood = 1 / (np.sqrt(2 * np.pi * sigma)) ** n * np.exp(-1 / (2 * sigma) * np.sum((y - y_pred) ** 2))
    return likelihood