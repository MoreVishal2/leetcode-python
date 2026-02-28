class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operation=0
        for i in nums:
            if i%3!=0:
                operation+=1
            
        return operation
