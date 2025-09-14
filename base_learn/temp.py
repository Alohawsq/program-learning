
def quick_sort1(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort1(left) + middle + quick_sort1(right)

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
    arr[left], arr[i] = arr[i], pivot
    quick_sort2(arr, left, i - 1)
    quick_sort2(arr, i + 1, right)
    return arr

if __name__=='__main__':
    arr = [5.2, 2, 3, 1.1, 4, 5.1, 1]
    result = quick_sort1(arr)
    print(f"使用快速排序方法的排序结果为: {result}")
    arr = [5.2, 2, 3, 1.1, 4, 5.1, 1]
    result = quick_sort2(arr, 0, len(arr)-1)
    print(f"使用快速排序方法的排序结果为: {result}")
