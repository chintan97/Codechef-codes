#https://www.codechef.com/problems/CIELDIST
#Chintan Patel 3-1-2016

T = input()
while T:
	Ds,Dt,D = [int(x) for x in raw_input().split()]
	print max(0,D-Ds-Dt,Dt-D-Ds,Ds-D-Dt)
	T -= 1