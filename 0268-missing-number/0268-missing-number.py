class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a= len(nums) +1
        for i in range(a):
            if i not in nums:
                return i