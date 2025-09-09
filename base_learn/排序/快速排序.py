"""
快速排序
采用分治策略，选择一个基准元素，将数组分成两部分，一部分比基准小，一部分比基准大，然后递归地对这两部分排序。
"""
def quick_sort(arr, left , right):
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


if __name__ == '__main__':
    arr = [5, 4, 3, 2, 1]
    print("快速排序结果：", quick_sort(arr, 0, len(arr)-1))