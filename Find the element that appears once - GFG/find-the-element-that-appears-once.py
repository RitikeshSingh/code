#User function Template for python3
class Solution:
    def search (self , A , N) :
        result = {}
        
        for i in A :
            if i in result :
                result[i] += 1
            else :
                result[i] = 1
                
        for i in result :
            if result[i] != 2 :
                return i



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		arr = list(map(int, input().split()))
		ob = Solution()
		print(ob.search(arr, n)) 
# } Driver Code Ends