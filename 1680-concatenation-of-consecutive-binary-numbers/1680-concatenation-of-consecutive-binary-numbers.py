class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod=10**9+7
        num=0
        length=0

        for i in range(1,n+1):
            if (i & (i-1))==0:
                length=length+1

            num= ((num<<length) |  i ) % mod

        return num