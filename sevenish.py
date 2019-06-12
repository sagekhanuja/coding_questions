#problem: sevenish numbers are added powers of 7 or powers of 7. return nth sevenish number
def sevenish(input):
    nums = [1,7,8,49]
    if input<=4:
        print(nums[input-1])
    else:
        i = 3
        while i < input-1:
            if i%2 == 1:
                nums.append(nums[-1]+nums[-3])
            elif i%2 == 0:
                nums.append(7**i)
            i+=1
        print(nums)
        print(nums[-1])

sevenish(5)
