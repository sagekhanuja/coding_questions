'''
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard
 like the image below.
'''
def find_keyboard_words(words):
    
    List=[]
    for word in words:
        flag=[0,0]
        tem=0
        for wd in range(len(word)):
            i=wd%2
            if word[wd] in 'qwertyuiopQWERTYUIOP':
                flag[i]=1
            elif word[wd] in 'asdfghjklASDFGHJKL':
                flag[i]=2
            else:
                flag[i]=3
            if flag[0]!=flag[1] and flag[1]!=0:
                tem=1
                break
        if tem==0:
            List.append(word)
        return List
