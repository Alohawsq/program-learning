from typing import List


class Solution:
    """
    冒泡排序，时间复杂度O(n**2),空间复杂度O(1)
    """
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(length):
            swapped = False
            for j in range(0, length - i -1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True
            if not swapped:
                break
        return nums
if __name__ == '__main__':
    s = Solution()
    print(s.sortArray([5,2,3,1]))