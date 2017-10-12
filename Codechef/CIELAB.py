#https://www.codechef.com/problems/CIELAB
#Chintan Patel 26-12-2016

A,B = [int(x) for x in raw_input().split()]
ans = A-B
if ans%10 != 9:
	print ans+1
else:
	print ans-1