"""
选择排序
1.初始化：将整个序列分为已排序部分（初始为空）和未排序部分（整个序列）
2.查找最大值：在未排序部分中找到最小元素
3.交换位置：将找到的最小元素与未排序部分的第一个元素交换位置
4.更新边界：将已排序部分的边界向右移动一位
重复：重复步骤2-4，直到所有元素都排序完毕
"""
def selection_sort(arr):
    n = len(arr)
    # 遍历所有数组
    for index in range(n):
        # 假设当前索引i处的元素是最小的
        min_index = index
        # 在未排序部分中查找最小元素的索引
        for i in range(index+1, n):
            if arr[i] < arr[min_index]:
                min_index = i
        # 将找到的最小元素与第i个位置的元素进行交换
        arr[index], arr[min_index] = arr[min_index], arr[index]
    return arr


if __name__ == "__main__":
    # 测试用例
    test_array = [64, 25, 12, 22, 11]
    print("原始数组:", test_array)

    sorted_array = selection_sort(test_array.copy())
    print("排序后数组:", sorted_array)

    # 可视化排序过程
    print("\n排序过程演示:")
    arr = [64, 25, 12, 22, 11]
    print(f"初始数组: {arr}")

    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # 交换元素
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"第{i + 1}轮: {arr} (交换了{arr[i]}:位置 {i} 和 {arr[min_idx]}:{min_idx})")