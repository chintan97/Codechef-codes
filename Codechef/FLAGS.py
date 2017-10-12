#https://www.codechef.com/problems/FLAGS
#Chintan Patel 9-1-2016

T = input()
while T:
	N = input()
	ans = N*(N-1)*(2*(N-1)+(N-2)+2*(N-2)*(N-2))
	print ans 
	T -= 1