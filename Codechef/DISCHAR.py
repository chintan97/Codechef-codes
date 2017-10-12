#https://www.codechef.com/problems/DISCHAR
#Chintan Patel 5-1-2016 
 
T = input()
while T:
	A = raw_input()
	print len(set(A))
	T -= 1 