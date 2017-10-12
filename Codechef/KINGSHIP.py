#https://www.codechef.com/problems/KINGSHIP
#Chintan Patel 3-1-2016
 
T = input()
while T:
	N = input()
	P = [int(x) for x in raw_input().split()]
	temp = min(P)
	ans = 0
	for i in P:
		if i != temp:
			ans += i*temp
	print ans
	T -= 1 