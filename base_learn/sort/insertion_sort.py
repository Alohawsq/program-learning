"""
插入排序
1.从第一个元素开始，该元素可以认为已经被排序
2.取出下一个元素，在已经排序的元素序列中从后向前扫描
3.如果该元素（已排序）大于新元素，将该元素移到下一位置
重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
将新元素插入到该位置后，重复步骤2~5
适用于：小规模数据或基本有序的数据
"""

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        # 当前需要插入的元素
        key = arr[i]
        j = i - 1     # 从当前元素的前一个元素开始比较
        # 只有当arr[j]的值比key大的时候才需要进行后移
        while j >= 0 and arr[j] > key:
            # 向后移动一位空出将要插入值的位置
            arr[j+1] = arr[j]
            j -= 1
        # 将key插入到正确位置
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    # 测试用例
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", test_array)

    sorted_array = insertion_sort(test_array)
    print("排序后数组:", sorted_array)

    # 测试空数组
    print("空数组测试:", insertion_sort([]))

    # 测试单个元素数组
    print("单元素数组测试:", insertion_sort([5]))

    # 测试已排序数组
    print("已排序数组测试:", insertion_sort([1, 2, 3, 4, 5]))

    # 测试重复元素数组
    print("重复元素数组测试:", insertion_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]))