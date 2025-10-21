class Solution:
    def isPalindrome(self, x: int) -> bool:
        x2=x
        rev=0
        if x<0:
            return False

        while x2>0:
            rev=(rev*10)+(x2%10)
            x2=x2//10
        
        if x==rev:
            return True
        else :
            return False