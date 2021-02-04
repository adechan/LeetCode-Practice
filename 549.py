# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

class Solution:
    def singleNumber(self, nums) -> int:
        nums.sort()
        if len(nums) == 1:
            return nums[0]

        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
            else:
                return nums[len(nums) - 1]

    def singleNumber1(self, nums):
        for i in range(0, len(nums)):
            if nums[i] in nums[i + 1:] or nums[i] in nums[0: i]:
                continue
            else:
                return nums[i]

    def singleNumber2(self, nums):
        while len(nums) > 1:
            save = nums[0]
            count = nums.count(save)
            if count == 2:
                for _ in range(count):
                    nums.remove(save)
            elif count == 1:
                return nums[0]
        return nums[0]

    def singleNumber3(self, nums):
        result = {}
        for element in nums:
            if element in result:
                result[element] += 1
            else:
                result[element] = 1

        for key, value in result.items():
            if value == 1:
                return key

s = Solution()
l = [1, 2, 1, 3, 2, 3, 4, 4, 5]
l = [2, 2, 1]
l = [1, 1, 2, 3, 2]
print(s.singleNumber3(l))
