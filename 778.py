# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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

    def toDictionary(self, anagrams):
        dictionary = dict()
        for anagram in anagrams:
            key = ''.join(sorted(anagram[0]))
            if key not in dictionary.keys():
                dictionary[key] = [anagram]
            else:
                dictionary[key].append(anagram)

        return dictionary

    def groupAnagrams1(self, strs):
        anagrams = []
        for i in range(0, len(strs)):
            group_anagrams = [strs[i]]

            for j in range(i + 1, len(strs)):
                if self.isAnagram(strs[i], strs[j]):
                    group_anagrams.append(strs[j])

            anagrams.append(group_anagrams)

        unique_anagrams = []
        dictionary = self.toDictionary(anagrams)

        for key, values_list in dictionary.items():
            max = len(values_list[0])
            for value_list in values_list:
                if max < len(value_list):
                    max = len(value_list)

                if len(value_list) == max:
                    unique_anagrams.append(value_list)


        return unique_anagrams

    def groupAnagrams(self, strs):
        anagrams = dict()

        for string in strs:
            key = "".join(sorted(string))
            if key not in anagrams.keys():
                anagrams[key] = [string]
            else:
                anagrams[key].append(string)

        unique_anagrams = []
        for key in anagrams.keys():
            unique_anagrams.append(anagrams[key])

        return unique_anagrams


s = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(strs))