# %%
from IPython.core.pylabtools import find_gui_and_backend
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from stack_data import Line

# %%
data=pd.read_csv('examdata.csv')
print (data.head() )
# %%
plt1=plt.figure(figsize=(10,10))
plt.scatter(data.loc[:,'Exam1'],data.loc[:,'Exam2'])
plt.title('Examdata')
plt.xlabel('Exam1')
plt.ylabel('Exam2')
plt.show()
# %%
mask=data.loc[:,'Pass']==1
print(mask)
# %%
plt2=plt.figure(figsize=(10,10))
passed=plt.scatter(data.loc[:,'Exam1'][mask],data.loc[:,'Exam2'][mask])
failed=plt.scatter(data.loc[:,'Exam1'][~mask],data.loc[:,'Exam2'][~mask])
plt.title('Examdata')
plt.xlabel('Exam1')
plt.ylabel('Exam2')
plt.legend((passed,failed),('Passed','Failed'))
plt.show()
plt.show()
# %%
X=data.drop(['Pass'],axis=1)
y=data.loc[:,'Pass']
X1=data.loc[:,'Exam1']
X2=data.loc[:,'Exam2']
X1.head()
print(X.shape)
# %%
from sklearn.linear_model import LogisticRegression
LR_1=LogisticRegression()
LR_1.fit(X,y)
# %%
y_predict=LR_1.predict(X)
print(y_predict)

# %%
from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y,y_predict)
print(accuracy)
# %%
y_test=LR_1.predict([[70,65]])
print('passed'if y_test[0]==1 else 'failed')
# %%
theta1,theta2=LR_1.coef_[0][0],LR_1.coef_[0][1]
theta0=LR_1.intercept_
print(theta0,theta1,theta2)

# %%
X2_new=-(theta0+theta1*X1)/theta2
print(X2_new)
# %%
fig2=plt.figure(figsize=(10,10))
plt.plot(X1,X2_new,'r')
# %%
X1_2=X1*X1
X2_2=X2*X2
X1_X2=X1*X2
# %%
X_data_frame={'X1':X1,'X2':X2,'X1_2':X1_2,'X2_2':X2_2,'X1_X2':X1_X2}
X_data_frame=pd.DataFrame(X_data_frame)
print(X_data_frame)
# %%
LR2=LogisticRegression()
#model = LogisticRegression(max_iter=1000, solver='lbfgs')
LR2.fit(X_data_frame,y)
# %%
X1_new=X1.sort_values()
print(X1,X1_new)

# %%
predict_2=LR2.predict(X_data_frame)
accuracy2=accuracy_score(y,predict_2)
print(accuracy2)
# %%
LR2.coef_
print(LR2.coef_)
# %%
theta0=LR2.intercept_
theta1,theta2,theta3,theta4,theta5=LR2.coef_[0][0],LR2.coef_[0][1],LR2.coef_[0][2],LR2.coef_[0][3],LR2.coef_[0][4]
print(theta0,theta1,theta2,theta3,theta4,theta5)
#二阶边界函数
a=theta4
b=theta5*X1_new+theta2
c=theta0+theta1*X1_new+theta3*X1_new*X1_new
X2_new_boundary=(-b+np.sqrt(b*b-4*a*c))/(2*a)
print(X2_new_boundary)

# %%
fig4=plt.figure()
plt.plot(X1_new,X2_new_boundary,'r')
passed=plt.scatter(data.loc[:,'Exam1'][mask],data.loc[:,'Exam2'][mask])
failed=plt.scatter(data.loc[:,'Exam1'][~mask],data.loc[:,'Exam2'][~mask])
plt.title('Examdata')
plt.xlabel('Exam1')
plt.ylabel('Exam2')
plt.legend((passed,failed),('Passed','Failed'))
plt.show()
# %%

# %%
