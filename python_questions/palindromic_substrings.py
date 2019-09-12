'''Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
'''

def countSubstrings(s):
        
        def searchPalindrome(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        res = 0
        for i in range(len(s)):
            res += searchPalindrome(i, i)
            if i+1 < len(s):
                res += searchPalindrome(i, i+1)
        return res



def countSubstringsinefficient(s):
    pals = []
    pairs = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            subset = s[i:j]
            if subset == subset[::-1] and subset not in pairs:  
                pairs.append([i,j])
                pals.append(subset)
    print(pals)
    return len(pals)

test = 'abasassssssasdfaaaaaaaffjfjfjfjfjfjfjfjfjfjfjfjfjfkfjfkfjfkfjfkfjfkfjafafafafafafafafafafafafafafafafafafafafafafafafafafafafafafafafafafafaffaldfjaasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfalkjhasdfasldkfjal;skdfjal;skdjfa;lskdfja;lskfja;lskdfja;lskdfj ;lskdjf;alskdfja;sldfja;lskdjfasdfkjalskdfj;alskdjf;laksdjf;lakjfasdfjalskjflaksjflaksjflaksdjflaksjdflaksjdflaskfasdfasdfasdfasdfasdfafafafafafafafafafafafafafafafafafafafafafafafafafafaf;alskdfja;sldkfja;lsdkfja;slkdfj;alskdfja;lskdfj;asdkfja;lskdfj;askfj;alskdfj;askdfjl;akdfj'
print(len(test))
print(countSubstrings(test))