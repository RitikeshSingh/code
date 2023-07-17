#User function Template for python3

class Solution:
    def segregateElements(self, arr, n):
        q=[]
        Q=[]
        a=0
        # Your code goes here
        for i in range(len(arr)):
            
            if arr[i]<0:
                q.append(arr[i])
            else:
                Q.append(arr[i])
        arr[:]=Q+q
              
        
                
                
        
       


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.segregateElements(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends