def threesum(nums):
    nums.sort()
    N, result = len(nums), []
    for i in range(N):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        target = nums[i]*-1
        s,e = i+1, N-1
        while s<e:
            if nums[s]+nums[e] == target:
                result.append([nums[i], nums[s], nums[e]])
                s = s+1
                while s<e and nums[s] == nums[s-1]:
                    s = s+1
            elif nums[s] + nums[e] < target:
                s = s+1
            else:
                e = e-1
    return result





def suminefficient(nums): 
    sets = []
    nums.sort()
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                nums1 = nums[i]
                nums2 = nums[j]
                nums3 = nums[k]
                if nums1+nums2+nums3 == 0 and [nums1,nums2,nums3] not in sets:
                    sets.append([nums1,nums2,nums3])
                
    return sets

print(sum([1,-1,0,2,-3,1,2]))