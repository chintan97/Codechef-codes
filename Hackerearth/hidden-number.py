T = input()
while T:
	N = input()
	A = [int(x) for x in raw_input().split()]
	for i in set(A):
		if A.count(i) == 1:
			print i
			break
	T -= 1