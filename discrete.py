def discrete(a):
    """
    type a: list[int]
    根据离散概率随机返回整数（出现i的概率为a[i]）
    a中各元素之和必须等于1
    """
    import random
    r = random.random()
    cdf = 0
    for i in range(len(a)):
        cdf += a[i]
        if cdf >= r:
            return i
    return -1
