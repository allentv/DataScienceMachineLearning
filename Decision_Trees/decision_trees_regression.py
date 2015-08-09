# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 20:42:01 2015

@author: Allen Thomas Varghese
"""
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt

# Create a random dataset
rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(16))

# Fit regression model
clf_1 = DecisionTreeRegressor(max_depth=2)
clf_2 = DecisionTreeRegressor(max_depth=5)
clf_3 = DecisionTreeRegressor(max_depth=3)
clf_4 = DecisionTreeRegressor(max_depth=4)

clf_1.fit(X, y)
clf_2.fit(X, y)
clf_3.fit(X, y)
clf_4.fit(X, y)

# Predict
X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
y_1 = clf_1.predict(X_test)
y_2 = clf_2.predict(X_test)
y_3 = clf_3.predict(X_test)
y_4 = clf_4.predict(X_test)

# Plot the results
plt.figure()
plt.scatter(X, y, c="k", label="data")
#plt.plot(X_test, y_1, c="g", label="max_depth=2", linewidth=2)
plt.plot(X_test, y_2, c="r", label="max_depth=5", linewidth=2)
#plt.plot(X_test, y_3, c="b", label="max_depth=3", linewidth=2)
#plt.plot(X_test, y_4, c="y", label="max_depth=4", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Decision Tree Regression")
plt.legend()
plt.show()