# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


data=pd.read_csv('usa_housing_price.csv')
data.head()
# %%
fig=plt.figure(figsize = (10,10))
fig1=plt.subplot(2,3,1)
plt.scatter(data.loc[:,'Avg. Area Income'],data.loc[:,'Price'])
plt.title('Avg. Area Income VS Price')
fig2=plt.subplot(2,3,2)
plt.scatter(data.loc[:,'Avg. Area House Age'],data.loc[:,'Price'])
plt.title('Avg. House Age VS Price')
fig3=plt.subplot(2,3,3)
plt.scatter(data.loc[:,'Avg. Area Number of Rooms'],data.loc[:,'Price'])
plt.title('Avg. Area Number of Rooms VS Price')
fig4=plt.subplot(2,3,4)
plt.scatter(data.loc[:,'Area Population'],data.loc[:,'Price'])
plt.title('Area Population VS Price')
fig5=plt.subplot(2,3,5)
plt.scatter(data.loc[:,'size'],data.loc[:,'Price'])
plt.title('Size VS Price')
plt.show()

# %%
X=data.loc[:,'size']
y=data.loc[:,'Price']
y.head()
X=np.array(X).reshape(-1,1)
y=np.array(y).reshape(-1,1)
print(X.shape)
# %%
LR1=LinearRegression()
LR1.fit(X,y)
# %%
y_predict_1=LR1.predict(X)
print(y_predict_1)
# %%
from sklearn.metrics import mean_squared_error,r2_score
mean_squared_error_1=mean_squared_error(y,y_predict_1)
r2_score_1=r2_score(y,y_predict_1)
print(mean_squared_error_1,r2_score_1)
# %%
X_multi=data.drop(['Price'],axis=1)
X_multi
# %%
LR_multi=LinearRegression()
LR_multi.fit(X_multi,y)

# %%
y_predict_multi=LR_multi.predict(X_multi)
print(y_predict_multi)
# %%
MSE_predict_multi=mean_squared_error(y,y_predict_multi)
R2_multi=r2_score(y,y_predict_multi)
print(MSE_predict_multi,R2_multi)

# %%
plt_final_1=plt.figure(figsize=(5,8))
plt.scatter(y,y_predict_multi)
plt.show()

# %%
a=LR_multi.coef_
b=LR_multi.intercept_
print(a,b)
# %%
X_test=[65000,5,5,30000,200]
X_test=np.array(X_test).reshape(1,-1)


# %%
y_predi=LR_multi.predict(X_test)
print(y_predi)
# %%

# %%
