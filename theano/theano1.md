

```python
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
```

    DEBUG: nvcc STDOUT mod.cu
       ���ڴ����� C:/Users/xiaowei/AppData/Local/Theano/compiledir_Windows-10-10.0.10240-Intel64_Family_6_Model_60_Stepping_3_GenuineIntel-2.7.12-64/tmpjum6xa/265abc51f7c376c224983485238ff1a5.lib �Ͷ��� C:/Users/xiaowei/AppData/Local/Theano/compiledir_Windows-10-10.0.10240-Intel64_Family_6_Model_60_Stepping_3_GenuineIntel-2.7.12-64/tmpjum6xa/265abc51f7c376c224983485238ff1a5.exp
    
    Using gpu device 0: GeForce GTX 950M (CNMeM is enabled with initial size: 10.0% of memory, cuDNN 5005)
    


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-1-7d19c61f9a51> in <module>()
         11 
         12 #调用函数
    ---> 13 print f([2,3])
    

    H:\Anaconda2\lib\site-packages\theano\compile\function_module.pyc in __call__(self, *args, **kwargs)
        784                         s.storage[0] = s.type.filter(
        785                             arg, strict=s.strict,
    --> 786                             allow_downcast=s.allow_downcast)
        787 
        788                     except Exception as e:
    

    H:\Anaconda2\lib\site-packages\theano\tensor\type.pyc in filter(self, data, strict, allow_downcast)
        175             raise TypeError("Wrong number of dimensions: expected %s,"
        176                             " got %s with shape %s." % (self.ndim, data.ndim,
    --> 177                                                         data.shape))
        178         if not data.flags.aligned:
        179             try:
    

    TypeError: ('Bad input argument to theano function with name "<ipython-input-1-7d19c61f9a51>:10"  at index 0(0-based)', 'Wrong number of dimensions: expected 0, got 1 with shape (2L,).')



```python
print f(2,3)#传参不用[]
```

    5.0
    


```python
#定义函数输入、输出、函数体
X = T.dmatrix('X')
Y = T.dmatrix('Y')
Z = X+Y
f = function([X,Y],Z)

#调用函数
print f(ny.arrange(12).reshape(3,4),10*np.ones(3,4))
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-3-de4011df9384> in <module>()
          6 
          7 #调用函数
    ----> 8 print f(ny.arrange(12).reshape(3,4),10*np.ones(3,4))
    

    AttributeError: 'module' object has no attribute 'arrange'



```python
print f(ny.arange(12).reshape(3,4),10*np.ones(3,4))#arange不是arrange
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-4-d363815e20a2> in <module>()
    ----> 1 print f(ny.arange(12).reshape(3,4),10*np.ones(3,4))
    

    NameError: name 'np' is not defined



```python
print f(ny.arange(12).reshape(3,4),10*ny.ones(3,4))#注意ones的使用方法ones(shape, dtype, order)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-5-2a246d184bb4> in <module>()
    ----> 1 print f(ny.arange(12).reshape(3,4),10*ny.ones(3,4))
    

    H:\Anaconda2\lib\site-packages\numpy\core\numeric.pyc in ones(shape, dtype, order)
        188 
        189     """
    --> 190     a = empty(shape, dtype, order)
        191     multiarray.copyto(a, 1, casting='unsafe')
        192     return a
    

    TypeError: data type not understood



```python
print(f(ny.arange(12).reshape((3,4)), 10*ny.ones((3,4))))
```

    [[ 10.  11.  12.  13.]
     [ 14.  15.  16.  17.]
     [ 18.  19.  20.  21.]]
    


```python
print f(ny.arange(12).reshape((3,4)), 10*ny.ones((3,4)))
```

    [[ 10.  11.  12.  13.]
     [ 14.  15.  16.  17.]
     [ 18.  19.  20.  21.]]
    


```python
ny.arange(12)
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])




```python
ny.arange(12).reshape((3,4))
```




    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])




```python
ny.arange(12).reshape(3,4)
```




    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])




```python
10*ny.ones(3,4)#注意ones的使用方法ones(shape, dtype, order)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-11-42eb9239c9c9> in <module>()
    ----> 1 10*ny.ones(3,4)
    

    H:\Anaconda2\lib\site-packages\numpy\core\numeric.pyc in ones(shape, dtype, order)
        188 
        189     """
    --> 190     a = empty(shape, dtype, order)
        191     multiarray.copyto(a, 1, casting='unsafe')
        192     return a
    

    TypeError: data type not understood



```python
10*ny.ones((3,4))
```




    array([[ 10.,  10.,  10.,  10.],
           [ 10.,  10.,  10.,  10.],
           [ 10.,  10.,  10.,  10.]])




