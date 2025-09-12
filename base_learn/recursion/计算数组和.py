"""
分而治之
计算数组的和
"""
def sum_arr(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sum_arr(arr[1:])

if __name__=='__main__':
    arr = [2, 4, 6, 8]
    result = sum_arr(arr)
    print(f"数组: {arr}的求和结果为: {result}")