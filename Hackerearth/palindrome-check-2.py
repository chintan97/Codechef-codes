#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/palindrome-check-2/
#Chintan Patel 10-1-2016

S = raw_input()
if S == S[::-1]:
	print 'YES'
else:
	print 'NO'