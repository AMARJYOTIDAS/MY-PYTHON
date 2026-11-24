class Solution:
    def longestCommonPrefix(self, strs):
        strs.sort()
        s = ""
        i = 0
        length = len(strs)

        while i < len(strs[0]):
            if strs[0][i] == strs[length - 1][i]:
                s += strs[0][i]
            else:
                break
            i += 1

        return s

prefixes = Solution()
print(prefixes.longestCommonPrefix(["flower", "flow", "flight"]))  # Output
print(prefixes.longestCommonPrefix(["dog", "racecar", "car"]))  # Output
# print(prefixes.longestCommonPrefix([123, 456, 789]))  # Output
print(prefixes.longestCommonPrefix(["interspecies", "interstellar", "interstate"]))  # Output