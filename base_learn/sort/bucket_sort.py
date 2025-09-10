"""
桶排序：
将数组分到有限数量的桶里，每个桶再分别排序。
1.为什么分成n个区间？
当有n个元素时，理想情况下我们希望每个桶平均包含约1个元素
2.为什么桶的长度要为len(arr) + 1？
当 num 非常接近 max_val 时，由于浮点舍入误差，(num - min_val) / bucket_range 可能略大于 n
"""
def bucket_sort(arr):
    # 创建空桶
    max_val = max(arr)
    min_val = min(arr)

    # 处理所有元素相同的情况
    if max_val == min_val:
        return arr

    # 这里将桶的范围分成了len(arr)个区间，在理想情况下，每个桶中大约有一个元素
    bucket_range = (max_val - min_val) / len(arr)
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    # 将元素分配到桶中
    for num in arr:
        index = int((num - min_val) / bucket_range)
        # 边界检查，对于由于浮点数计算不准确或者num=max_val的情况，确保数组不会越界
        if index == bucket_count:
            index = -1
        buckets[index].append(num)

    # 对每个桶排序并合并
    result = []
    for bucket in buckets:
        result.extend(sorted(bucket))

    return result


if __name__ == '__main__':
    # print(bucket_sort([9, 2, 3, 1, 4]))
    print(bucket_sort([5.2, 2, 3, 1.1, 4, 5.1, 1]))
