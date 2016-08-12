

```python
import numpy as np
a = np.arange(6).reshape(2,3)
b = a*2
hstack(a,b)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-1-e02fb4f500c1> in <module>()
          2 a = np.arange(6).reshape(2,3)
          3 b = a*2
    ----> 4 hstack(a,b)
    

    NameError: name 'hstack' is not defined



```python
np.hstack(a,b)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-2-00c158e06a9c> in <module>()
    ----> 1 np.hstack(a,b)
    

    TypeError: hstack() takes exactly 1 argument (2 given)



```python
np.hstack((a,b))#水平组合、接受ndarray对象构成的元组
```




    array([[ 0,  1,  2,  0,  2,  4],
           [ 3,  4,  5,  6,  8, 10]])




```python
np.concatenate((a,b))
```




    array([[ 0,  1,  2],
           [ 3,  4,  5],
           [ 0,  2,  4],
           [ 6,  8, 10]])




```python
n.concatenate((a,b),axis=1)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-5-5a6561951906> in <module>()
    ----> 1 n.concatenate((a,b),axis=1)
    

    NameError: name 'n' is not defined



```python
np.concatenate((a,b),axis=1)#用concatenate合并，指定哪个维度
```




    array([[ 0,  1,  2,  0,  2,  4],
           [ 3,  4,  5,  6,  8, 10]])




```python
np.vstack((a,b))#垂直组合
```




    array([[ 0,  1,  2],
           [ 3,  4,  5],
           [ 0,  2,  4],
           [ 6,  8, 10]])




```python
np.dstack((a,b))#深度组合
```




    array([[[ 0,  0],
            [ 1,  2],
            [ 2,  4]],
    
           [[ 3,  6],
            [ 4,  8],
            [ 5, 10]]])




```python
np.column_stack((a.b))
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-9-b60e1e1522af> in <module>()
    ----> 1 np.column_stack((a.b))
    

    AttributeError: 'numpy.ndarray' object has no attribute 'b'



```python
np.column_stack(a,b)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-10-0a01137b67b3> in <module>()
    ----> 1 np.column_stack(a,b)
    

    TypeError: column_stack() takes exactly 1 argument (2 given)



```python
np.column_stack((a,b))#列组合
```




    array([[ 0,  1,  2,  0,  2,  4],
           [ 3,  4,  5,  6,  8, 10]])




```python
c=np.row_stack((a,b))#行组合
```


```python
c
```




    array([[ 0,  1,  2],
           [ 3,  4,  5],
           [ 0,  2,  4],
           [ 6,  8, 10]])




```python
import numpy as np
a = np.arange(24).reshape(2,3,4)
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
np.hsplit(a,2)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-3-6824bd587f4d> in <module>()
    ----> 1 np.hsplit(a,2)
    

    H:\Anaconda\lib\site-packages\numpy\lib\shape_base.pyc in hsplit(ary, indices_or_sections)
        560         raise ValueError('hsplit only works on arrays of 1 or more dimensions')
        561     if len(ary.shape) > 1:
    --> 562         return split(ary, indices_or_sections, 1)
        563     else:
        564         return split(ary, indices_or_sections, 0)
    

    H:\Anaconda\lib\site-packages\numpy\lib\shape_base.pyc in split(ary, indices_or_sections, axis)
        498         if N % sections:
        499             raise ValueError(
    --> 500                 'array split does not result in an equal division')
        501     res = array_split(ary, indices_or_sections, axis)
        502     return res
    

    ValueError: array split does not result in an equal division



```python
np.split(a,4)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-4-50c4ca31ccab> in <module>()
    ----> 1 np.split(a,4)
    

    H:\Anaconda\lib\site-packages\numpy\lib\shape_base.pyc in split(ary, indices_or_sections, axis)
        498         if N % sections:
        499             raise ValueError(
    --> 500                 'array split does not result in an equal division')
        501     res = array_split(ary, indices_or_sections, axis)
        502     return res
    

    ValueError: array split does not result in an equal division



```python
np.hsplit(a,2)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-5-6824bd587f4d> in <module>()
    ----> 1 np.hsplit(a,2)
    

    H:\Anaconda\lib\site-packages\numpy\lib\shape_base.pyc in hsplit(ary, indices_or_sections)
        560         raise ValueError('hsplit only works on arrays of 1 or more dimensions')
        561     if len(ary.shape) > 1:
    --> 562         return split(ary, indices_or_sections, 1)
        563     else:
        564         return split(ary, indices_or_sections, 0)
    

    H:\Anaconda\lib\site-packages\numpy\lib\shape_base.pyc in split(ary, indices_or_sections, axis)
        498         if N % sections:
        499             raise ValueError(
    --> 500                 'array split does not result in an equal division')
        501     res = array_split(ary, indices_or_sections, axis)
        502     return res
    

    ValueError: array split does not result in an equal division



```python
a=np.arange(6).reshape(2,3)
```


```python
a
```




    array([[0, 1, 2],
           [3, 4, 5]])




```python
np.hsplit(a,3)
```




    [array([[0],
            [3]]), array([[1],
            [4]]), array([[2],
            [5]])]




```python
a = np.arange(24).reshape(2,3,4)
a
```




    array([[[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11]],
    
           [[12, 13, 14, 15],
            [16, 17, 18, 19],
            [20, 21, 22, 23]]])




```python
np.hsplit(a,4)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-10-a6f2bb24403b> in <module>()
    ----> 1 np.hsplit(a,4)
    

    H:\Anaconda\lib\site-packages\numpy\lib\shape_base.pyc in hsplit(ary, indices_or_sections)
        560         raise ValueError('hsplit only works on arrays of 1 or more dimensions')
        561     if len(ary.shape) > 1:
    --> 562         return split(ary, indices_or_sections, 1)
        563     else:
        564         return split(ary, indices_or_sections, 0)
    

    H:\Anaconda\lib\site-packages\numpy\lib\shape_base.pyc in split(ary, indices_or_sections, axis)
        498         if N % sections:
        499             raise ValueError(
    --> 500                 'array split does not result in an equal division')
        501     res = array_split(ary, indices_or_sections, axis)
        502     return res
    

    ValueError: array split does not result in an equal division



```python
np.column_split(a,4)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-11-026a0bd57fb2> in <module>()
    ----> 1 np.column_split(a,4)
    

    AttributeError: 'module' object has no attribute 'column_split'



```python

```
