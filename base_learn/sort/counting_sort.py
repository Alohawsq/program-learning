"""
计数排序：
1.确定范围
2，统计频率
3.生成排序结果
适合小范围的整数排序
"""
def counting_sort(nums):
    # 确定范围
    max_val = max(nums)
    min_val = min(nums)
    arr = [0 for i in range(max_val - min_val + 1)]
    # 统计频率
    for i in nums:
        arr[i - min_val] += 1
    # 生成排序结果
    new_arr = []
    for index, count in enumerate(arr):
            new_arr.extend([index+min_val]*count)
    return new_arr

if __name__=='__main__':
    # 测试
    arr = [4, 2, 2, 8, 3, 3, 1]
    print("计数排序结果:", counting_sort(arr))  # 输出: [1, 2, 2, 3, 3, 4, 8]
