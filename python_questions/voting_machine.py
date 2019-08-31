'''
On election day, a voting machine writes data in the form (voter_id, candidate_id) to a text file. 
Write a program that reads this file as a stream and returns the top 3 candidates at any given time. 
If you find a voter voting more than once, report this as fraud.
'''

##refer to votes.txt for the text document

from collections import Counter
import numpy as np
##file
f = open('votes.txt', 'r')

voter = []
candidate = []
for x in f:
    if x[0] != 'V':
        voter.append(int(x[0]))
    if x[12] != 'n':
        candidate.append(int(x[12]))

candidate_count = Counter(candidate)
voter_count = Counter(voter)

cand_vals = []
vote_num = [] ##how many people voted for each candidate

for vote in set(voter):
    if voter_count[vote]>1:
        print('voter ' + str(vote) + ' is a fraud!!')

for cand in set(candidate_count):
    cand_vals.append(cand)
    vote_num.append(candidate_count[cand])

print('top 3 candidates')
print([cand_vals[i] for i in np.argsort(vote_num)][::-1])

f.close()


