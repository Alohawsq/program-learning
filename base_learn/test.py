"""
桶排序
"""
def bucket_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    bucket_range = (max_val - min_val)/len(arr)
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    new_arr = []
    for num in arr:
        index = int((num - min_val) / bucket_range)
        if index >= bucket_count:
            index = -1
        buckets[index].append(num)

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
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            return arr
    return arr

"""
快速排序
"""
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def quick_sort2(arr, left, right):
    if left > right:
        return arr
    pivot = arr[left]
    i, j = left, right

    while i < j:
        while arr[j] >= pivot and i < j:
            j -= 1
        while arr[i] <= pivot and i < j:
            i += 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[i], pivot
    quick_sort2(arr, left, j - 1)
    quick_sort2(arr, j + 1, right)


if __name__ == '__main__':
    print("冒泡排序结果：", bubble_sort([5, 2, 3, 1.1, 4, 5.1, 1]))
    print("桶排序结果：", bucket_sort([5.2, 2, 3, 1.1, 4, 5.1, 1]))
    arr = [5.2, 2, 3, 1.1, 4, 5.1, 1]
    new_arr = quick_sort(arr)
    print("快速排序1结果：", new_arr)
    arr2 = [5.2, 2, 3, 1.1, 4, 5.1, 1]
    quick_sort2(arr2, 0, len(arr)-1)
    print("快速排序2结果：", arr2)

