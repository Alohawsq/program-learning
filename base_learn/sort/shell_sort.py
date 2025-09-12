"""
希尔排序
插入排序的升级版，
将数组分成多个子序列进行插入排序
"""

def shell_sort(arr):
    n = len(arr)
    # 初始增量（间隔）为数组长度的一半
    gap = n // 2

    # 当增量大于0时继续排序
    while gap > 0:
        # 对每个子序列进行插入排序
        for i in range(gap, n):
            # 保存当前元素
            temp = arr[i]
            j = i
            # 对子序列进行插入排序
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


if __name__ == "__main__":
    # 测试用例
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", test_array)

    sorted_array = shell_sort(test_array)
    print("排序后数组:", sorted_array)

    # 测试空数组
    print("空数组测试:", shell_sort([]))

    # 测试单个元素数组
    print("单元素数组测试:", shell_sort([5]))

    # 测试已排序数组
    print("已排序数组测试:", shell_sort([1, 2, 3, 4, 5]))

    # 测试重复元素数组
    print("重复元素数组测试:", shell_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]))