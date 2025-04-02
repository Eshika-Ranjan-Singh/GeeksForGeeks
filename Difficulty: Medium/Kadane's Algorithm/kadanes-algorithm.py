class Solution:
    def maxSubArraySum(self, arr):
        # Your code here
        maxh=0
        maxf=float('-inf')
        for num in arr:
            maxh=max(num, maxh+num)
            maxf=max(maxf,maxh)
        return maxf    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends