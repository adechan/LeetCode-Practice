# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

class Solution:
    def toDictionary(self, list):
        result = {}
        for element in list:
            if element in result.keys():
                result[element] += 1
            else:
                result[element] = 1

        return result

    def firstUniqChar(self, s: str) -> int:
        count_elements = self.toDictionary(s)

        for key, value in count_elements.items():
            if value == 1:
                return s.index(key)
                break
        return -1

    def hasDuplicates(self, char, list):
        if char in list:
            return True
        else:
            return False

    def firstUniqChar1(self, s: str):
        if len(s) == 0:
            return -1

        for i in range(0, len(s)):
            if self.hasDuplicates(s[i], s[0: i]) or self.hasDuplicates(s[i], s[i + 1:len(s)]):
                if i == len(s) - 1:
                    return -1
                else:
                    continue
            else:
                return i



s = Solution()
string = "abcbcdadeef"
print(s.firstUniqChar1(string))
