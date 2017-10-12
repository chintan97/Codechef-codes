#https://www.codechef.com/problems/PPSUM
#Chintan Patel 21-12-2016

T = input()
def S(x):
	sum = 0
	for i in range(1,x+1):
		sum += i
	return sum
	
while T>0:
	D,N = [int(x) for x in raw_input().split()]
	res = S(N)
	while D>1:
		res = S(res)
		D -= 1
	print res
	T -= 1