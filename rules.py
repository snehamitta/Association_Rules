from itertools import combinations
import numpy as np

input = ['A','B','C','D','E','F','G']

#Number of Itemsets Possible
d = (np.size(input))
print ('The total number of possible itemsets are', 2**d - 1)

# Q1 - (b to h)
print ('All the possible 1 - itemsets are', list(combinations(input,1)))
print ('All the possible 2 - itemsets are', list(combinations(input,2)))
print ('All the possible 3 - itemsets are', list(combinations(input,3)))
print ('All the possible 4 - itemsets are', list(combinations(input,4)))
print ('All the possible 5 - itemsets are', list(combinations(input,5)))
print ('All the possible 6 - itemsets are', list(combinations(input,6)))
print ('All the possible 7 - itemsets are', list(combinations(input,7)))


