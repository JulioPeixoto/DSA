# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/description/?envType=daily-question&envId=2025-06-24
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        idx_arr=[]
        for j in range(0, len(nums)):
            if nums[j] == key:
                for i in range(0, len(nums)):
                    if abs(i - j) <= k: idx_arr.append(i)

        return list(set(idx_arr))
