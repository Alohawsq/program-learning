"""
快速排序
采用分治策略，选择一个基准元素，将数组分成两部分，一部分比基准小，一部分比基准大，然后递归地对这两部分排序。
"""
def quick_sort_bak(arr, left , right):
    if left > right:
        return arr
    pivot = arr[left]
    i, j = left, right
    while i < j :
        while arr[j] >= pivot and i < j:
            j = j - 1
        while arr[i] <= pivot and i < j:
            i = i + 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], pivot
    quick_sort(arr, left, i-1)
    quick_sort(arr, i+1, right)

def quick_sort(arr, left, right):
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
    arr[left], arr[i] = arr[j], pivot
    quick_sort(arr, left, i-1)
    quick_sort(arr, i+1, right)

def quick_sort_two(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    right = [y for y in arr if y > pivot]
    middle = [z for z in arr if z == pivot]
    return quick_sort_two(left) + middle + quick_sort_two(right)

if __name__ == '__main__':
    arr = [5.2, 2, 3, 1.1, 4, 5.1, 1]
    quick_sort(arr, 0, len(arr) - 1)
    print("快速排序结果：", arr)
    arr = [5.2, 2, 3, 1.1, 4, 5.1, 1]
    new_arr = quick_sort_two(arr)
    print("快速排序结果2：", new_arr)