"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组是数组中的一个连续部分。
"""
# 动态规划方法求解
def solution_dynamic(arr):
    n = len(arr)
    if n == 0:
        return 0
    dp = [0 for i in range(n)]
    dp[0] = nums[0]
    max_length = dp[0]
    for i in range(1, n):
        dp[i] = max(nums[i] + dp[i-1], nums[i])
        if dp[i] > max_length:
            max_length = dp[i]
    return max_length

# 分而治之方法求解
def solution_divide(arr):
    n = len(arr)
    def divide_and_conquer(left, right):
        if left == right:
            return arr[left]
        mid = (left + right) // 2
        # 1. 递归计算左右两边的最大子数组和
        left_sum = divide_and_conquer(left, mid)
        right_sum = divide_and_conquer(mid + 1, right)

        # 2. 计算跨越中点的最大子数组和
        # 2.1 向左扫描
        left_cross_sum = -float('inf')
        current_sum = 0
        for i in range(mid, left - 1, -1):
            current_sum += nums[i]
            left_cross_sum = max(left_cross_sum, current_sum)
        # 2.2 向右扫描
        right_cross_sum = -float('inf')
        current_sum = 0
        for j in range(mid + 1, right + 1):
            current_sum += nums[j]
            right_cross_sum = max(right_cross_sum, current_sum)
        cross_sum = left_cross_sum + right_cross_sum

        # 3. 返回三者中的最大值
        return max(left_sum, right_sum, cross_sum)

    return divide_and_conquer(0, len(nums) - 1)


if __name__=='__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    result = solution_dynamic(nums)
    print(f"数组{nums}的最大字数组和为: {result}")
    result = solution_divide(nums)
    print(f"数组{nums}的最大字数组和为: {result}")
