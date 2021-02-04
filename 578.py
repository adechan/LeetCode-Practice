# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums) -> bool:
        if len(nums) == len(set(nums)):
            return False
        return True


s = Solution()
list = [1,1,1,3,3,4,3,2,4,2]
print(s.containsDuplicate(list))