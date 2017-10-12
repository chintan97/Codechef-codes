#https://www.codechef.com/problems/POTATOES
#Chintan Patel 30-12-2016

T = input()
def isPrime(x):
	if x%2 == 0:
		return False
	for i in range(3,(x/2)+1):
		if x%i == 0:
			return False
	
	return True
while T>0:
	x,y = [int(i) for i in raw_input().split()]
	j = x+y+1
	while True:
		if isPrime(j):
			print j-x-y
			break
		j += 1
			
	T -= 1