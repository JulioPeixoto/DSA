class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        u_index = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[u_index]:
                u_index += 1
                nums[u_index] = nums[i]
                
        return u_index + 1
