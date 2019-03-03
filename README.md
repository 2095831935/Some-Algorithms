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
实现：随机将列表a中的元素排序  
原理分析：若a中有N个元素，则 1. 显然a[0]出现在任一个位置的概率为1/N；2. 对于a[1]，与a[0]交换的概率为1/N，出现在其他位置的概率则为 (1-1/N)/(N-1)=1/N; 3. 以此类推，可以发现每个元素出现在任一位置的概率均为1/N；
