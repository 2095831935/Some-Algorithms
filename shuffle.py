def shuffle(a):
    """
    type a: list[int]
    随机将a列表中元素排序
    """
    import random
    N = len(a)
    for i in range(N):
        r = i + random.randint(0, N-i-1)
        a[i], a[r] = a[r], a[i]
