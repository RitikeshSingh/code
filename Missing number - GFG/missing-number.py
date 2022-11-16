#User function Template for python3

def missingNumber( A, N):
     
    q=0
    a=N*(N+1)//2
    for i in range(len (A)):
        q+=A[i]
    return a-q


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(missingNumber(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends