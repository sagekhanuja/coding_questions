def powerofthreefast(n):
        while n % 3 == 0 and n != 0:
                n /= 3
        if n == 1: 
            return True
        return False


def powerofthreeslow(n):
    nums = [3]

    while nums[-1]<n:
        nums.append(nums[-1]*3)
    return n == nums[-1]

print(powerofthreefast(81))