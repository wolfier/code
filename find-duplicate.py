# Source: Interview Cakes

# In Find a duplicate, Space Edition™, we were given a list of integers where:
# 1. the integers are in the range 1..n
# 2. the list has a length of n+1

# These properties mean the list must have at least 1 duplicate.
# Our challenge was to find a duplicate number, while optimizing for space. 
# We used a divide and conquer approach, iteratively cutting the list in half
# to find a duplicate integer in O(nlgn) time and O(1) space (sort of a modified binary search).

# But we can actually do better. We can find a duplicate integer in O(n) time
# while keeping our space cost at O(1).