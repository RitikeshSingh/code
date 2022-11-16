
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = s = 0
        Map = {}
        Map[0] = 1 
        for i in range(len(nums)):
            s += nums[i]
            if s - k in Map:
                count += Map.get(s-k)
            Map[s] = Map.get(s,0) +1 
        return count 