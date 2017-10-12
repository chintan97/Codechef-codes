#https://www.codechef.com/problems/WALK
#Chintan Patel 31-12-2016

T = input()
while T:
	N = input()
	W = [int(x) for x in raw_input().split()]
	a = list()
	for i in range(N):
		a.append(i+W[i])
	print max(a)
	T -= 1