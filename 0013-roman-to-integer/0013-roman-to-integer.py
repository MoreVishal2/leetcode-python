class Solution:
    def romanToInt(self, s: str) -> int:
        num=0
        i=1
        length=len(s)
        preChar_value= 0

        while i<=len(s):
            char_value = self.getvalue(s[-i])
            
            if i!=len(s):
                if  self.getvalue(s[-i-1]) < char_value:
                    num = num + (char_value - self.getvalue(s[-i-1]))
                    i=i+2
                else :
                    num = num + char_value
                    i=i+1
            else :
                num = num + char_value
                i=i+1

        return num




    def getvalue(self,character):
        if character=='I':
            return 1
        elif character=='V':
            return 5
        elif character=='X':
            return 10
        elif character=='L':
            return 50
        elif character=='C':
            return 100
        elif character=='D':
            return 500
        else:
            return 1000