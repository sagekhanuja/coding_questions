##Given a non-empty array of integers, return the k most frequent elements.
from collections import Counter
import heapq

def find_k(nums,k):
    count = Counter(nums)   
    return heapq.nlargest(k, count.keys(), key=count.get) 



