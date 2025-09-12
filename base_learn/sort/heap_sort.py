"""
堆排序
1.将待排序的序列构建成一个大顶堆（或小顶堆）。
2.此时，整个序列的最大值（或最小值）就是堆顶的根节点。
3.将其与堆数组的末尾元素进行交换，此时末尾就是最大值（或最小值）。
4.然后将剩余的n-1个序列重新构造成一个堆，这样就会得到n个元素中的次大值（或次小值）。
5.如此反复执行，便能得到一个有序序列了。
"""

def heap_sort(arr):
    n = len(arr)
    # 1.构建最大堆，从最后一个非叶子结点开始向前遍历
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)

    # 2.逐个提取元素
    for i in range(n-1, 0, -1):
        # 将当前最大节点的值移动到数组的末尾
        arr[i], arr[0] = arr[0], arr[i]
        # 为什么传入的堆大小为i，传入的节点索引值为0？
        # 由于前面已经将最大值移至末尾所以目前的最大值到i
        # 至于节点的索引值，由于除了0处的根节点，其余部分都符合根节点大于叶子结点的值，
        # 所以对0处的根节点进行排序即可获知此次的最大节点，且还可以对后续节点进行再次排序以便为下次获取最大值做准备
        heapify(arr, i, 0)
    return arr

def heapify(arr, n, i):
    """
    调整堆，使其满足堆的性质
    :param arr: 待调整的数组
    :param n: 堆的大小，数组的长度
    :param i: 当前节点的索引，第一次为最后一个非叶子结点
    """
    largest = i    # 最大值的索引位置
    left = 2 * i + 1  # 左叶子节点
    right = 2 * i + 2  # 右叶子结点

    # 如果左叶子结点存在且左叶子节点比根节点的值大，更新最大索引位置
    if left < n and arr[left] > arr[largest]:
        largest = left
    # 如果右叶子结点存在且右叶子结点的值比根节点的大，更新最大索引位置
    if right < n and arr[right] > arr[largest]:
        largest = right
    # 如果当前最大值索引的位置不是根节点，则进行节点交换
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        # 递归调整交换前最大节点后续的子节点，确保以当前最大节点为根节点的后续节点都符合最大堆的条件
        heapify(arr, n, largest)



if __name__ == "__main__":
    # 测试用例
    test_array = [64, 34, 25, 12, 22, 11, 90, 88]
    print("原始数组:", test_array)

    sorted_array = heap_sort(test_array)
    print("排序后数组:", sorted_array)

    # 测试空数组
    print("空数组测试:", heap_sort([]))

    # 测试单个元素数组
    print("单元素数组测试:", heap_sort([5]))

    # 测试已排序数组
    print("已排序数组测试:", heap_sort([1, 2, 3, 4, 5]))

    # 测试重复元素数组
    print("重复元素数组测试:", heap_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]))
