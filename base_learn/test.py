"""
桶排序
"""
def bucket_sort(arr):
    # 查找最大最小值
    min_val = min(arr)
    max_val = max(arr)
    # 排除已排序情况
    if min_val == max_val:
        return arr
    # 定义桶的划分区间
    bucket_range = (max_val - min_val) / len(arr)
    bucket_count = len(arr) + 1
    # 创建空桶
    buckets = [[] for _ in range(bucket_count)]
    # 遍历arr数组
    for num in arr:
        index = int((num - min_val)/bucket_range)
        if index == bucket_count:
            index = -1
        buckets[index].append(num)

    new_arr = []
    for bucket in buckets:
        new_arr.extend(sorted(bucket))
    return new_arr

"""
冒泡排序
"""
def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        swapped = False
        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            if not swapped:
                return arr
    return arr
if __name__ == '__main__':
    print("冒泡排序结果：", bucket_sort([5, 2, 3, 1.1, 4, 5.1, 1]))
    print("桶排序结果：", bucket_sort([5.2, 2, 3, 1.1, 4, 5.1, 1]))
