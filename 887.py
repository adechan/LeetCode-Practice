# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefixBetween2(self, string1, string2):
        longest = ""

        min_len = len(string1)
        if min_len > len(string2):
            min_len = len(string2)

        for i in range(0, min_len):
            if string1[0: i + 1] == string2[0: i + 1] and len(longest) < len(string1[0: i + 1]):
                longest = string1[0: i + 1]

        return longest

    def longestCommonPrefix(self, strs: list) -> str:
        if len(strs) == 0:
            return ""
        longest = strs[0]
        while len(strs) >= 1:
            longest = self.longestCommonPrefixBetween2(longest, strs[0])
            strs.pop(0)

        return longest


s = Solution()
strs = ["flower", "flow", "flight"]
print(s.longestCommonPrefix(strs))