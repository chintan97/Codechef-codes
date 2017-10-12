#https://www.codechef.com/problems/CFRTEST
#Chintan Patel 21-12-2016

T = input()
a = list()
while T>0:
	n = input()
	a = [int(x) for x in raw_input().split()]
	cnt = 0
	for i in range(0,n):
		temp = a[i]
		for j in range(i+1,n):
			if temp == a[j]:
				break
			elif j == n-1 and temp != a[j]:
				cnt += 1
			
	print cnt+1	
	T -= 1