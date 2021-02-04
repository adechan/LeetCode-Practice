# Given two arrays, write a function to compute their intersection.
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.

class Solution:
    def to_dictionary(self, list):
        result = {}
        for value in list:
            if value in result:
                result[value] += 1
            else:
                result[value] = 1

        return result

    def get_min(self, a, b):
        if a > b:
            return b
        else:
            return a

    def intersect(self, nums1, nums2) -> list:
        dict1 = self.to_dictionary(nums1)
        dict2 = self.to_dictionary(nums2)

        result = []
        for element in set(nums1):
            if element in dict1.keys() and element in dict2.keys():
                min = self.get_min(dict1[element], dict2[element])
                for _ in range(min):
                    result.append(element)

        return result

s = Solution()
nums11 = [1,2,2,1]
nums12 = [2,2]

nums21 = [4,9,5]
nums22 = [9,4,9,8,4]
print(s.intersect(nums21, nums22))
