class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_map = dict()
    
        for num in nums:
            f_map[num] = f_map.get(num, 0) + 1
    
        b = [[] for _ in range(len(nums)+1)]
    
        for num, freq in f_map.items():
            b[freq].append(num)
        
        r = []
    
        for freq in range(len(nums),0,-1):
            for num in b[freq]:
                r.append(num)
                if len(r) == k:
                    return r
    
        return r