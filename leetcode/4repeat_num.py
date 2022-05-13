# -*- coding : utf-8 -*-
"""
作者： admin
日期：2022年04月17日
"""

# nums = [1, 2, 3, 2]
# x = len(nums)
# y = set(nums)
# print(x)
# print(y)
# print(len(y))


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #解法一
        nums.sort()
        i = 1
        while i < len(nums):
            if nums[i - 1] == nums[i]:
                return True
            else:
                i += 1
        return False
        # 解法二
        return len(set(nums)) != len(nums)