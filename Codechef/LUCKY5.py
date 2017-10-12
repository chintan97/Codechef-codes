#https://www.codechef.com/problems/LUCKY5
#Chintan Patel 31-12-2016

T = input()
while T>0:
	N = raw_input().strip()
	cnt = 0
	for i in N:
		if i != '4' and i != '7':
			cnt += 1
			
	print cnt
	T -= 1