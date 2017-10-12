#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/warcakewalk/
#Chintan Patel 11-1-2016

T = input()
while T:
	N = input()
	A = [int(x) for x in raw_input().split()]
	B = [int(x) for x in raw_input().split()]
	bob = max(A)
	alice = max(B)
	if bob > alice:
		print 'Bob'
	elif bob < alice:
		print 'Alice'
	else:
		print 'Tie'
	T -= 1