##  Write a function that takes a string as input and reverse only the vowels of a string.

#given string, reverse only its vowels
def reverseVowels(s):
        vowels = 'aeiou'
        s = list(s)
        indexes = []
        values = []
        
        for i in range(len(s)):
            if s[i] in vowels:
                indexes.append(i)
                values.append(s[i])
            if len(indexes) ==2 and len(values) == 2:
                first = s[indexes[0]]
                last = s[indexes[1]]
                s[i] = first
                s[indexes[0]] = last
                indexes, values = [], []
        print(s)
reverseVowels('helllo')
