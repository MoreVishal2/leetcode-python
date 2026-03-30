class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s1_od=dict()
        s1_even=dict()
        s2_od=dict()
        s2_even=dict()
        for i in range(len(s1)):
            if i%2==0:
                if s1[i] in s1_even:
                    s1_even[s1[i]]+=1
                else:
                    s1_even[s1[i]]=1
                    
                if s2[i] in s2_even :
                    s2_even[s2[i]]+=1
                else:
                    s2_even[s2[i]]=1

            else:
                if s1[i] in s1_od:
                    s1_od[s1[i]]+=1
                else:
                    s1_od[s1[i]]=1
                    
                if s2[i] in s2_od :
                    s2_od[s2[i]]+=1
                else:
                    s2_od[s2[i]]=1

        if (s1_od==s2_od) and (s1_even==s2_even):
            return True
        else:
            return False