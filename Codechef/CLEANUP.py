#https://www.codechef.com/problems/CLEANUP
#Chintan Patel 26-12-2016

T = input()
D = list()
W = list()
while T>0:
	del D,W
	n,m = [int(x) for x in raw_input().split()]
	D = [int(x) for x in raw_input().split()]
	W = list()
	for i in range(1,n+1):
		flag = 1
		for j in range(0,m):
			if D[j] == i:
				flag = 0
				break
		
		if flag == 1:
			W.append(i)
			
	for i in range(0,n-m):
		if i%2 == 0:
			print W[i],
		
	print "\n"
	for i in range(0,n-m):
		if i%2 == 1:
			print W[i],
	
	print "\n"
	T -= 1