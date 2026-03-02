class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n=len(grid)
        l1=[0]*n

        for i in range(n):
            count=0
            for j in range(-1,-n-1,-1):
                if grid[i][j] ==0:
                    count+=1
                else:
                    break
            l1[i]=count
        
        swap=0

        for i in range(len(l1)):
            j=i
            required=n-i-1

            while j<n and l1[j]<required:
                j+=1

            if j==n:
                return -1

            while j>i:
                l1[j], l1[j - 1] = l1[j - 1], l1[j]
                swap += 1
                j -= 1
        
        return swap

       
