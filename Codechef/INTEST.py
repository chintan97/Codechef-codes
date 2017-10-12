#https://www.codechef.com/problems/INTEST
#Chintan Patel 24-12-2016

n,k = [int(x) for x in raw_input().split()]
cnt = 0
for i in range(0,n):
	if input()%k == 0: cnt += 1
	
print cnt