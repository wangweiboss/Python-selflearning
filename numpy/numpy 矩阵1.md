

```python
import numpy as np
def numpysum(n):
    a = np.arange(n)*2
    b = np.arange(n)*3
    c = a+b
    return c

def pythonsum(n):
    a = range(n)
    b = range(n)
    c = []
    for i in range(n):
        a[i] = a[i]*2
        b[i] = b[i]*3
        c.append(a[i]+b[i])
    
    return c

import datetime as dt
start = dt.datetime.now()
c1 = numpysum(1000)
deltatime = dt.datetime.now()-start #numpy花的时间少
print "numpysum spend time in microseconds:",deltatime.microseconds

start = dt.datetime.now()
c2 = pythonsum(1000)
deltatime = dt.datetime.now()-start #python比numpy效率低
print "pythonsum spend time in microseconds:",deltatime.microseconds
```

    numpysum spend time in microseconds: 0
    pythonsum spend time in microseconds: 0
    


```python
import numpy as np
a = np.arange(5)
a.dtype
```




    dtype('int32')




```python
a
```




    array([0, 1, 2, 3, 4])




```python
a.shape#维度属性的存储方式是元组tuple
```




    (5L,)




```python
b = np.array([0,1])
```


```python
b
```




    array([0, 1])




```python
b = np.array([[0,1],[0,1])
```


      File "<ipython-input-6-9d8fdda7579b>", line 1
        b = np.array([[0,1],[0,1])
                                 ^
    SyntaxError: invalid syntax
    



```python
b = np.array([[0,1],[0,1]])#创建多维数组，注意array接受列表类型的对象
```


```python
b
```




    array([[0, 1],
           [0, 1]])




```python
b[0,0]#选取数组中特定元素。注意从0开始
```




    0




```python
b[0,1]#选取数组中特定元素
```




    1




```python
complex(2.0)
```




    (2+0j)




```python
a=np.arange(3,dtype=int64
```


      File "<ipython-input-12-e1fc1c57bc1e>", line 1
        a=np.arange(3,dtype=int64
                                 ^
    SyntaxError: unexpected EOF while parsing
    



```python
a=np.arange(3,dtype=int64)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-13-4727eab3bdbc> in <module>()
    ----> 1 a=np.arange(3,dtype=int64)
    

    NameError: name 'int64' is not defined



```python
a=np.arange(3,dtype=int32)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-14-acaf49354405> in <module>()
    ----> 1 a=np.arange(3,dtype=int32)
    

    NameError: name 'int32' is not defined



```python
a=np.arange(3,dtype=int)#用dtype指定数组类型
```


```python
a
```




    array([0, 1, 2])




```python
a.dtype
```




    dtype('int32')




```python
a.dtype()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-18-0ff82c073f15> in <module>()
    ----> 1 a.dtype()
    

    TypeError: 'numpy.dtype' object is not callable



```python
a.dtype.itemsize#int占4个字节
```




    4




```python
a=np.arange(3,dtype=float)
```


```python
a.dtype.itemsize
```




    8




```python
a=np.arange(3,dtype=np.int32)#int32是numpy中定义的
```


```python
a.dtype.itemsize
```




    4




```python
a=np.arange(3,dtype=np.int64)
```


```python
a.dtype.itemsize
```




    8




```python
a=arange(5,dtype=np.float64)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-26-6e3cfd457cf2> in <module>()
    ----> 1 a=arange(5,dtype=np.float64)
    

    NameError: name 'arange' is not defined



```python
a=np.arange(5,dtype=np.float64)
```


```python
a.dtype.itemsize
```




    8




```python
import numpy as np
a = np.arange(24).reshape(2,3,4)
a[0,0,0]
a[0]
a[0,0]
```




    array([0, 1, 2, 3])




```python
a
```




    array([[[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11]],
    
           [[12, 13, 14, 15],
            [16, 17, 18, 19],
            [20, 21, 22, 23]]])




```python
a[0,0,0]
```




    0




```python
a[0]
```




    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])




```python
a[::-1]
```




    array([[[12, 13, 14, 15],
            [16, 17, 18, 19],
            [20, 21, 22, 23]],
    
           [[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11]]])




```python
a[,::-1]#::-1表示翻转
```


      File "<ipython-input-6-d57d682d0520>", line 1
        a[,::-1]
          ^
    SyntaxError: invalid syntax
    



```python
a[:,::-1]
```




    array([[[ 8,  9, 10, 11],
            [ 4,  5,  6,  7],
            [ 0,  1,  2,  3]],
    
           [[20, 21, 22, 23],
            [16, 17, 18, 19],
            [12, 13, 14, 15]]])




```python
a[:,:,::-1]
```




    array([[[ 3,  2,  1,  0],
            [ 7,  6,  5,  4],
            [11, 10,  9,  8]],
    
           [[15, 14, 13, 12],
            [19, 18, 17, 16],
            [23, 22, 21, 20]]])




```python
a[0,::2,:]#::表示间隔
```




    array([[ 0,  1,  2,  3],
           [ 8,  9, 10, 11]])




```python
a[0,0,1:2]
```




    array([1])




```python
a[0,0,1:3]
```




    array([1, 2])




```python
a[0,0,1:4]
```




    array([1, 2, 3])




```python
a.reshape(1,24)
```




    array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
            17, 18, 19, 20, 21, 22, 23]])




```python
a
```




    array([[[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11]],
    
           [[12, 13, 14, 15],
            [16, 17, 18, 19],
            [20, 21, 22, 23]]])




```python
a= a.reshaoe(1,24)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-15-dee35fbf8441> in <module>()
    ----> 1 a= a.reshaoe(1,24)
    

    AttributeError: 'numpy.ndarray' object has no attribute 'reshaoe'



```python
a= a.reshape(1,24)
```


```python
a
```




    array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
            17, 18, 19, 20, 21, 22, 23]])




```python
a=a.resize(2,3,4)
```


```python
a
```


```python
a
```


```python
a=a.resize((2,3,4))
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-21-b052f20235ee> in <module>()
    ----> 1 a=a.resize((2,3,4))
    

    AttributeError: 'NoneType' object has no attribute 'resize'



```python
a=np.arange(24)
```


```python
a
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19, 20, 21, 22, 23])




```python
a=a.resize((2,3,4))
```


```python
a
```


```python
a=np.arange(24)
```


```python
a.resize((2,3,4))
```


```python
a
```




    array([[[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11]],
    
           [[12, 13, 14, 15],
            [16, 17, 18, 19],
            [20, 21, 22, 23]]])




```python
a.resize(1,24)
```


```python
a
```




    array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
            17, 18, 19, 20, 21, 22, 23]])




```python
a.transpose
```




    <function transpose>




```python
a
```




    array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
            17, 18, 19, 20, 21, 22, 23]])




```python
a.reshape(2,3,4)
```




    array([[[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11]],
    
           [[12, 13, 14, 15],
            [16, 17, 18, 19],
            [20, 21, 22, 23]]])




```python
a
```




    array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
            17, 18, 19, 20, 21, 22, 23]])




```python
a=a.reshape(2,3,4)
```


```python
a
```




    array([[[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11]],
    
           [[12, 13, 14, 15],
            [16, 17, 18, 19],
            [20, 21, 22, 23]]])




```python
a.tanspose
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-37-dd22a1cf0846> in <module>()
    ----> 1 a.tanspose
    

    AttributeError: 'numpy.ndarray' object has no attribute 'tanspose'



```python
a.transpose()#转置
```




    array([[[ 0, 12],
            [ 4, 16],
            [ 8, 20]],
    
           [[ 1, 13],
            [ 5, 17],
            [ 9, 21]],
    
           [[ 2, 14],
            [ 6, 18],
            [10, 22]],
    
           [[ 3, 15],
            [ 7, 19],
            [11, 23]]])




```python
a.flattern()#拉直
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-39-7bd00970905f> in <module>()
    ----> 1 a.flattern()
    

    AttributeError: 'numpy.ndarray' object has no attribute 'flattern'



```python
a.flatten()#拉直
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19, 20, 21, 22, 23])




```python

```
