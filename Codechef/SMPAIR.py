#https://www.codechef.com/problems/SMPAIR
#Chintan Patel 24-12-2016

T = input()
a = list()
while T>0:
	N = input()
	a = [int(x) for x in raw_input().split()]
	temp = min(a)
	a.remove(temp)
	print temp+min(a)
	T -= 1