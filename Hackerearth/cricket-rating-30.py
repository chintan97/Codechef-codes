#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/cricket-rating-30/
#Chintan Patel 11-1-2016

N = input()
def max_subarray(A):
    max_ending_here = max_so_far = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
if N == 0:
	print 0
else:
	A = [int(x) for x in raw_input().split()]
	print max_subarray(A)