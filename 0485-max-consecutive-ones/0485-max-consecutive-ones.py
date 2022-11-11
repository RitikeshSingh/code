class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums.append(0)
        a=0
        q=[]
        for i in nums:
            if i==1:
                a=a+1
            else:
                q.append(a)
                a=0
        return max(q)
        