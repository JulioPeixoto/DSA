# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/?envType=daily-question&envId=2025-06-24
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result = set()
        for i, num in enumerate(nums):
            if num == key:
                start = max(0, i - k)
                end = min(len(nums) - 1, i + k)
                for j in range(start, end + 1):
                    result.add(j)
        return sorted(result)
