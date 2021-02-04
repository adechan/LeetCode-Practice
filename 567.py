# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for el in nums:
            if el == 0:
                count += 1

        while count:
            nums.remove(0)
            nums.insert(len(nums), 0)
            count -= 1

        return nums

    def moveZeroes1(self, nums):
        size = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[size] = nums[i]
                size += 1
            else:
                continue

        while size < len(nums):
            nums[size] = 0
            size += 1

        return nums


s = Solution()
l = [0, 1, 0, 2, 12]
print(s.moveZeroes1(l))
