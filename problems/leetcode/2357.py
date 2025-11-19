class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Solution approach:
        # - We must always choose x <= smallest non-zero element
        # - Optimal strategy: always choose x = smallest non-zero element
        # - This guarantees at least one value becomes 0 per operation
        # - Duplicate values are eliminated together in the same operation
        # - Therefore: # of operations = # of unique positive values
        #
        # {x for x in nums if x > 0} creates a set of unique positive numbers
        # len() returns the count of unique values
        return len({x for x in nums if x > 0})
