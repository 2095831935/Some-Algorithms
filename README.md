# Some-Algorithms
Record some interesting algorithms

## discrete.py
``` python
def discrete(a):
    """
    type a: list[int]
    """
```
实现：返回i的概率为a[i]
原理分析：`r = random()`在(0,1)区间均匀采样，显然`r<=a[0]`的概率为a[0],若`sum(a[:i-1])<r<=sum(a[:i])`，则返回i，r在此区间的概率为a[i]

## shuffle.py
``` python
def shuffle(a):
    """
    type a: list[int]
    """
```
