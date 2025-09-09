from typing import List


class Solution:
    """
    冒泡排序，时间复杂度O(n**2),空间复杂度O(1)
    以[5,2,3,1]为例子
    5和2比较交换，5和3比较交换，5和1比较交换 i=0 j最大到2 所以j<length-i-1 此时5是最大的已经可以确定最后一位是最大的值
    2和3比较、3和1比较 i=1 j最大到1 j<length-i-1 此时3是最大的已经确定
    2和1比较 i=2 j最大到0 此时2是最大的已经确定
    相当于外层循环（0，3） 内层循环 （0，length - i -1）
    """
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(length-1):
            swapped = False
            for j in range(length - i -1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True
            if not swapped:
                break
        return nums
if __name__ == '__main__':
    s = Solution()
    print(s.sortArray([5,2,3,1]))