# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum1(self, nums: list, target: int):
        for i in range(0, len(nums)):
            to_find = target - nums[i]
            if to_find in nums[i + 1:]:
                return [i, nums.index(to_find, i + 1)]

s = Solution()
nums = [2,7,11,15]
target = 9
nums = [3, 3]
target = 6
print(s.twoSum1(nums, target))