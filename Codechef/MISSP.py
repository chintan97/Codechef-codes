#https://www.codechef.com/problems/MISSP
#Chintan Patel 23-12-2016

T = input()
while T>0:
	N = input()
	left = list()
	
	for i in range(0,N):
		t = input()
		if t in left:
			left.remove(t)
		else:
			left.append(t)
			
	print left[0]
	T -= 1