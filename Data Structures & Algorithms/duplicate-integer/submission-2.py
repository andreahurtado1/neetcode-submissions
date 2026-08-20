class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = {} # store {#: occurances}
        for num in nums:
            if num not in duplicates:
                duplicates[num] = 1
            else:
                return True
        
        return False
            
        