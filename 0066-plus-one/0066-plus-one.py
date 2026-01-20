class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]==9:
            digits[-1]=0
            is_nine=True
            for i in range(len(digits)):
                if i+1==1:
                    continue
                if digits[-(i+1)]==9:
                    digits[-(i+1)]=0
                else:
                    digits[-(i+1)]=digits[-(i+1)]+1
                    is_nine=False
                    break
            if is_nine:
                digits.insert(0,1)
            return digits


        else:
            digits[-1]=digits[-1]+1
            return digits