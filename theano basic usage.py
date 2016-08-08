
# coding: utf-8

# In[1]:

import numpy as ny
from theano import function
import theano.tensor as T

#coding:utf-8
#定义函数输入、输出、函数体
x = T.dscalar('x')
y = T.dscalar('y')
z = x+y
f = function([x,y],z)

#调用函数
print f([2,3])#传参格式错误


# In[2]:

print f(2,3)#传参不用[]


# In[3]:

#定义函数输入、输出、函数体
X = T.dmatrix('X')
Y = T.dmatrix('Y')
Z = X+Y
f = function([X,Y],Z)

#调用函数
print f(ny.arrange(12).reshape(3,4),10*np.ones(3,4))


# In[4]:

print f(ny.arange(12).reshape(3,4),10*np.ones(3,4))#arange不是arrange


# In[5]:

print f(ny.arange(12).reshape(3,4),10*ny.ones(3,4))#注意ones的使用方法ones(shape, dtype, order)


# In[6]:

print(f(ny.arange(12).reshape((3,4)), 10*ny.ones((3,4))))


# In[7]:

print f(ny.arange(12).reshape((3,4)), 10*ny.ones((3,4)))


# In[8]:

ny.arange(12)


# In[9]:

ny.arange(12).reshape((3,4))


# In[10]:

ny.arange(12).reshape(3,4)


# In[11]:

10*ny.ones(3,4)#注意ones的使用方法ones(shape, dtype, order)


# In[12]:

10*ny.ones((3,4))


# 
