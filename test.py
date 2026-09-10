# %%
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv('test.csv')
data.head()
# %%
data.head()
print(type(data),data.shape)
# %%
x=data.loc[:,'x']
y=data.loc[:,'y']
print(x,y)
# %%
plt.figure(figsize=(8,5))
plt.scatter(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
# %%
x=np.array(x)
x=x.reshape(-1,1)
y=np.array(y)
y=y.reshape(-1,1)
print(type(x),x.shape)

# %%
lr_model=LinearRegression()
lr_model.fit(x,y)

# %%
y_predict=lr_model.predict(x)
print(y_predict)
# %%
y_3=lr_model.predict([[3.5]])
print(y_3)

# %%
print(y)
# %%
a=lr_model.coef_
b=lr_model.intercept_
print(a,b)
# %%
from sklearn.metrics import mean_squared_error,r2_score
MSE=mean_squared_error(y,y_predict)
R2=r2_score(y,y_predict)
print(MSE,R2)
# %%
plt.figure()
plt.plot(x,y_predict,'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression prediction')

plt.show()

# %%

# %%
