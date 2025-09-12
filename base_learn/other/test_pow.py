"""
计算3的100次幂
如果n=0则返回1
如果n=1则返回a
如果n是偶数，计算a^(n/2)，然后返回结果的平方
如果n是奇数，计算a^((n-1)/2)，然后返回结果的平方乘以a
"""

def test_pow(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    # n是奇数
    if n % 2:
        return test_pow(a, (n - 1) / 2) * test_pow(a, (n - 1) / 2) * a
    else:
        return test_pow(a, n / 2) * test_pow(a, n / 2)



if __name__=='__main__':
    num = test_pow(3, 6)
    print(num)