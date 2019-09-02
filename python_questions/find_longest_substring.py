def lengthOfLongestSubstringefficient(self, s):
        n = len(s)
        if n <= 1: return n

        freq = [0 for _ in range(256)]
        l, r = 0, -1
        res = 0

        while r+1 < n:
            char = ord(s[r+1])
            if freq[char] == 0:
                freq[char] += 1
                r += 1
            else:
                freq[ord(s[l])] -= 1
                l += 1
            res = max(res, r-l+1)

        return res




def find_longest_substring(arr):
        count = []
        for i in range(len(arr)):
            counter = 0
            new_arr = arr[i:]
            val = new_arr[0]
            for j in range(len(new_arr)-1):
                if new_arr[j] != val:
                    break
                counter+=1
            count.append(counter)
        print(count)
        return max(count)