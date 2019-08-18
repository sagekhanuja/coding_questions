## Given a set of distinct integers, nums, return all possible subsets w/out duplicates (the power set).

def subsets(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        method: recursion
        """
        if not nums: return [[]]
        prefix = subsets(nums[:-1])
        return prefix + [pre + [nums[-1]] for pre in prefix]
        
print(subsets([1,2,3,4]))
