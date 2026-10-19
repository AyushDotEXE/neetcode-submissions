class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: 
        count = {}

        for i,n in enumerate(nums):

            if n in count:
                return True

            count[n] = i

        return False

