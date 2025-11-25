class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if (k%2==0) | (k%5==0):
            return -1
        n=1
        dig=1
        while n%k!=0:
            n=(n*10)+1
            dig=dig+1
        
        return dig