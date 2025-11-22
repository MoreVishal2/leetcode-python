class Solution:
    def isValid(self, s: str) -> bool:
        li=[]
        for i in s:
            if i in ('(','[','{'):
                li.append(i)
            else :
                if len(li)==0:
                    return False
                if (i==')') & (li[len(li)-1]=='('):
                    li.pop()
                elif (i==']') & (li[len(li)-1]=='['):
                    li.pop()
                elif (i=='}') & (li[len(li)-1]=='{'):
                    li.pop()
                else:
                    return False

        if len(li)==0:
            return True
        else:
            return False