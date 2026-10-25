class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1

        buckets = [[] for i in range(len(nums) + 1)]

        for n in count:
            buckets[count[n]].append(n)

        res = []

        for i in range(len(nums), 0, -1):
            for n in buckets[i]:
                res.append(n)

                if len(res) == k:
                    return res