"""
桶排序
"""
def bucket_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    if max_val == min_val:
        return arr
    bucket_range = (max_val - min_val) / len(arr)
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]
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
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            return arr
    return arr

"""
快速排序
"""
def quick_sort(arr, left, right):
    if left > right:
        return arr
    pivot = arr[left]
    i, j = left, right
    while i < j:
        while arr[j] >= pivot and i < j:
            j = j - 1
        while arr[i] <= pivot and i < j:
            i = i + 1
        if i < j:
            arr[j], arr[i] = arr[i], arr[j]
    arr[j], arr[left] = pivot, arr[j]
    quick_sort(arr, left, j - 1)
    quick_sort(arr, j + 1, right)



def maximalSquare(matrix) -> int:
    rows = len(matrix)
    if not rows:
        return 0
    cols = len(matrix[0]) if rows else 0
    sides = [[0 for j in range(cols)] for i in range(rows)]
    max_side = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:
                    side = int(matrix[i][j])
                else:
                    side = min(int(sides[i - 1][j]), int(sides[i][j - 1]), int(sides[i - 1][j - 1])) + 1
                sides[i][j] = side
                if side > max_side:
                    max_side = side
    print(max_side)
    return max_side * max_side


if __name__ == '__main__':
    # print("冒泡排序结果：", bucket_sort([5, 2, 3, 1.1, 4, 5.1, 1]))
    # print("桶排序结果：", bucket_sort([5.2, 2, 3, 1.1, 4, 5.1, 1]))
    # arr = [5.2, 2, 3, 1.1, 4, 5.1, 1]
    # quick_sort(arr, 0, len(arr)-1)
    # print("快速排序结果：", arr)

    matrix = [["1", "1", "1", "1", "0"], ["1", "1", "1", "1", "0"], ["1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1"],
     ["0", "0", "1", "1", "1"]]
    maximalSquare(matrix)

