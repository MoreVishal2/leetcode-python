class Solution:
    def mySqrt(self, x: int) -> int:
        first=1
        last =x
        ans=0
        while first<=last:
            num=(first+last)//2
            num_sq=num*num
            if num_sq==x:
                return num
            elif num_sq>x:
                last=num-1
            else:
                first=num+1
                ans=num

        return ans