
class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i

print(Solution().removeElement([3, 2, 2, 3], 3))  # Output: 2
print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))  # Output: 5