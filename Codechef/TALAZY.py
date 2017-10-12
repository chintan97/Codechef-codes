#https://www.codechef.com/problems/TALAZY
#Chintan Patel 20-12-2016

T = input()
while T>0:
	N,B,M = [int(x) for x in raw_input().split()]
	t = 0
	
	while N>0:
		if N%2 == 0:
			temp = N/2
		else:
			temp = (N/2)+1
		
		t += (temp)*M
		t += B
		N -= temp
		M *= 2
	
	print t-B
			
	T -= 1