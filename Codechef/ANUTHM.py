#https://www.codechef.com/problems/ANUTHM
#Chintan Patel 5-1-2016 
 
T = input()
while T:
	N,M = [int(x) for x in raw_input().split()]
	print N+M-1
	T -= 1 