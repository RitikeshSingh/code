#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        a=0
        b=[]
        q=0
        c=[]
        for i in arr:
            if i<0:
                q+=1
        for i in arr:
            a+=i
            c.append(a)
            if a<0:
                b.append(a-i)
                a=0
        
        b.append(a)
        
        if q==len(arr):
            return max(arr)
        else:
            return max(max(b),max(c))
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends