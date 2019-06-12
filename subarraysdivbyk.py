#Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.
def subarraysDivByK(A, K):
        m, nsum, count = [-1]*K, 0, 0
        m[0] = 0
        for n in A:
            nsum = (nsum+n) % K
            m[nsum] += 1
            count += m[nsum]
        return count