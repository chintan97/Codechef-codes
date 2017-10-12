#https://www.codechef.com/problems/CSUB
#Chintan Patel 2-1-2016

T = input()
while T:
	N = input()
	num = raw_input()
	temp = num.count('1')
	print (temp*(temp+1))/2
	T -= 1