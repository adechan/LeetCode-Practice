# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# Clarification:
# Confused why the returned value is an integer but your answer is an array?
# Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

class Solution:
    def removeDuplicates(self, nums) -> int:
        size = 0
        for i in range(0, len(nums)):
            if nums[size] == nums[i]:
                continue
            else:
                size += 1
                nums[size] = nums[i]

        nums[size + 1:] = []
        return len(nums), nums

s = Solution()
list = [0, 0, 1, 1, 2, 2, 3, 3, 5, 6]
print(s.removeDuplicates(list))
