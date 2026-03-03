class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s="0"
        for i in range(1,n):
            invert=""
            for i in s:
                dig=int(i)^1
                invert=invert+str(dig)
            s=s+"1"+invert[::-1]

        return s[k-1]