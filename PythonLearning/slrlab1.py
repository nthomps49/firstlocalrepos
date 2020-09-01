import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np

df = pd.read_csv(r"C:\Users\natha\Documents\GitHub\firstlocalrepos\PythonLearning\FuelConsumptionCo2.csv")
print(df.head())
#summarize the data
print(df.describe())
#Select some features to explore
cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
print(cdf.head(9))
#we can plot each of these features
#viz = cdf[['CYLINDERS','ENGINESIZE','CO2EMISSIONS','FUELCONSUMPTION_COMB']]
#viz.hist()
#plt.show()
#now plot each of these features vs emissions to see how linear the relationship is
#plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS,  color='blue')
#plt.xlabel("FUELCONSUMPTION_COMB")
#plt.ylabel("Emission")
#plt.show()
#create an array of the given shape and populate it with random samples
msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]
#Train data distribution
#plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
#plt.xlabel("Engine size")
#plt.ylabel("Emission")
#plt.show()
#using sklearn package to model data
from sklearn import linear_model
regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit (train_x, train_y)
# The coefficients
print ('Coefficients: ', regr.coef_)
print ('Intercept: ',regr.intercept_)
#plot the fit line over the data
plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], '-r')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()
#now use MSE to calcuate accuarcy of the model based on the test set
#mean absolute error is mean of absolute value of the errors.
#R-squred is not error put popular to measure accuracy of the model
from sklearn.metrics import r2_score
test_x = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
test_y_ = regr.predict(test_x)
print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y_ , test_y) )
