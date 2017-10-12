#https://www.codechef.com/problems/FLOW014
#Chintan Patel 23-12-2016

T = input()
while T>0:
	h,c,t = [float(x) for x in raw_input().split()]
	
	if h > 50 and c < 0.7 and t > 5600:
		gr = 10
	elif h > 50 and c < 0.7:
		gr = 9
	elif c < 0.7 and t > 5600:
		gr = 8
	elif h > 50 and t > 5600:
		gr = 7
	elif h > 50 or c < 0.7 or t > 5600:
		gr = 6
	else:
		gr = 5
	
	print gr
	T -= 1