class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = {}
        for i, n in enumerate(nums):
            a[nums[i]] = a.get(nums[i], 0) + 1
            if a[nums[i]] > 1:
                return True
        return False