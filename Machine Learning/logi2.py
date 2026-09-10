# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %%
data=pd.read_csv('chip_test.csv')
print (data.head() )
# %%
mask=data.loc[:,'pass']==1
print(mask)
# %%
plt2=plt.figure(figsize=(10,10))
passed=plt.scatter(data.loc[:,'test1'][mask],data.loc[:,'test2'][mask])
failed=plt.scatter(data.loc[:,'test1'][~mask],data.loc[:,'test2'][~mask])
plt.title('Exam-data')
plt.xlabel('Exam1')
plt.ylabel('Exam2')
plt.legend((passed,failed),('Passed','Failed'))
plt.show()
plt.show()
# %%
X=data.drop(['pass'],axis=1)
y=data.loc[:,'pass']
X1=data.loc[:,'test1']
X2=data.loc[:,'test2']
X1.head()
print(X.shape)
# %%
X1_2=X1*X1
X2_2=X2*X2
X1_X2=X1*X2
X1_new=X1.sort_values()
print(X1,X1_new)
# %%
X_data_frame={'X1':X1,'X2':X2,'X1_2':X1_2,'X2_2':X2_2,'X1_X2':X1_X2}
X_data_frame=pd.DataFrame(X_data_frame)
print(X_data_frame)
# %%
from sklearn.linear_model import LogisticRegression
LR2=LogisticRegression()
LR2.fit(X_data_frame,y)

# %%
from sklearn.metrics import accuracy_score
predict_2=LR2.predict(X_data_frame)
accuracy2=accuracy_score(y,predict_2)
print(accuracy2)
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
plt2=plt.figure(figsize=(10,10))
passed=plt.scatter(data.loc[:,'test1'][mask],data.loc[:,'test2'][mask])
failed=plt.scatter(data.loc[:,'test1'][~mask],data.loc[:,'test2'][~mask])
plt.title('Exam-data')
plt.xlabel('Exam1')
plt.ylabel('Exam2')
plt.legend((passed,failed),('Passed','Failed'))

#fig4 = plt.figure()
plt.plot(X1_new, X2_new_boundary, 'r')

plt.show()

# %%
def f(x):
    a=theta4
    b=theta5*x+theta2
    c=theta0+theta1*x+theta3*x*x
    x1_newboundary=(-b+np.sqrt(b*b-4*a*c))/(2*a)
    x2_newboundary=(-b-np.sqrt(b*b-4*a*c))/(2*a)
    return x1_newboundary,x2_newboundary
# %%
X2_new_boundary1=[]
X2_new_boundary2=[]

for x in X1_new:
    X2_new_boundary1.append(f(x)[0])
    X2_new_boundary2.append(f(x)[1])
print(X2_new_boundary1,X2_new_boundary2)
# %%
plt3=plt.figure(figsize=(10,10))
passed=plt.scatter(data.loc[:,'test1'][mask],data.loc[:,'test2'][mask])
failed=plt.scatter(data.loc[:,'test1'][~mask],data.loc[:,'test2'][~mask])
plt.title('Exam-data')
plt.xlabel('Exam1')
plt.ylabel('Exam2')
plt.legend((passed,failed),('Passed','Failed'))

#fig4 = plt.figure()
plt.plot(X1_new, X2_new_boundary1, 'r')
plt.plot(X1_new, X2_new_boundary2, 'g')
plt.show()

# %%
X1_range=[-0.9+x/10000 for x in range(0,30000)]
X1_range=np.array(X1_range)
X2_new_boundary1=[]
X2_new_boundary2=[]

for x in X1_range:
    X2_new_boundary1.append(f(x)[0])
    X2_new_boundary2.append(f(x)[1])
# %%
plt4=plt.figure(figsize=(10,10))
passed=plt.scatter(data.loc[:,'test1'][mask],data.loc[:,'test2'][mask])
failed=plt.scatter(data.loc[:,'test1'][~mask],data.loc[:,'test2'][~mask])
plt.title('Exam-data')
plt.xlabel('Exam1')
plt.ylabel('Exam2')
plt.legend((passed,failed),('Passed','Failed'))

#fig4 = plt.figure()
plt.plot(X1_range, X2_new_boundary1, 'r')
plt.plot(X1_range, X2_new_boundary2, 'g')
#plt.legend((passed,failed),('Passed','Failed'))

plt.show()

# %%

# %%

# %%

# %%
