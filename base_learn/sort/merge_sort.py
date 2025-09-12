"""
分而治之
归并排序（适用于大型数据集）：
1. 分解：将当前数组从中间分成两个子数组，直到子数组只剩下一个元素（自然有序）。
2. 解决：递归地对两个子数组进行归并排序。
3. 合并：将两个有序子数组合并成一个有序数组。
"""
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    # 分解数组
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    # 递归地对左右两部分进行拆解并在拆解完成后逐步合并
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # 合并序列
    return merge_nums(left_sorted, right_sorted)

def merge_nums(left, right):
    new_arr = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            new_arr.append(left[i])
            i += 1
        else:
            new_arr.append(right[j])
            j += 1
    if i < len(left):
        new_arr.extend(left[i:])
    if j < len(right):
        new_arr.extend(right[j:])
    return new_arr


if __name__ == "__main__":
    # 测试用例
    test_array = [64, 34, 25, 12, 22, 11, 90, 88]
    print("原始数组:", test_array)
    sorted_array = merge_sort(test_array)
    print("排序后数组:", sorted_array)
    # 测试空数组
    print("空数组测试:", merge_sort([]))
    # 测试单个元素数组
    print("单元素数组测试:", merge_sort([5]))
    # 测试已排序数组
    print("已排序数组测试:", merge_sort([1, 2, 3, 4, 5]))
    # 测试重复元素数组
    print("重复元素数组测试:", merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]))