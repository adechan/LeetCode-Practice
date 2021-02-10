# Given two strings s and t , write a function to determine if t is an anagram of s.

class Solution:
    def toDictionary(self, s):
        result = {}
        for char in s:
            if char not in result.keys():
                result[char] = 1
            else:
                result[char] += 1

        return result

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_appearances = self.toDictionary(s)
        t_appearances = self.toDictionary(t)

        if len(s_appearances) != len(t_appearances):
            return False

        for char_t in t:
            if char_t in s_appearances.keys() and char_t in t_appearances.keys():
                if s_appearances[char_t] != t_appearances[char_t]:
                    return False
                else:
                    continue
            else:
                return False
        return True

    def isAnagram1(self, s, t):
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if len(sorted_s) != len(sorted_t):
            return False

        for i in range(0, len(s)):
            if sorted_s[i] != sorted_t[i]:
                return False
            else:
                continue
        return True

s = Solution()
print(s.isAnagram1("anagram", "nagaram"))