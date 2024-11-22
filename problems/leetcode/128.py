class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        
        sorted_list = sorted(nums)
        x = 1
        z = 1
        for i in range(0, len(sorted_list) - 1): 
            if sorted_list[i] + 1 == sorted_list[i+1]:
                z += 1  
                if z > x:
                    x = z
            elif sorted_list[i] == sorted_list[i+1]:
                pass
            else:
                z = 1
        
        return(x)