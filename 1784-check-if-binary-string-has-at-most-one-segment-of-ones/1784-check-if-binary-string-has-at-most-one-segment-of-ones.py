class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        count=0
        zero=0
        for i in s:
            if (i=='1') and (zero==0):
                count=count+1
            elif (count>0) and (i=='0'):
                zero=zero+1
            elif (zero>0) and (i=='1'):
                return False

        return True