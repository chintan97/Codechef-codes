#https://www.codechef.com/problems/COPS
#Chintan Patel 22-12-2016

T = input()
H = list()
while T>0:
	M,x,y = [int(a) for a in raw_input().split()]
	H = [int(a) for a in raw_input().split()]
	max = x*y
	oh = []
	for i in range(0,101):
		oh.append(0)
	
	for i in H:
		l = i-max
		r = i+max
		if l<1:
			l = 1
		if r>100:
			r=100
				
		for j in range(l,i+1):
			oh[j] = 1
		for j in range(i,r+1):
			oh[j] = 1
			
	cnt = 0
	for i in range(1,101):
		if oh[i] == 0:
			cnt += 1
		
	print cnt
	T -= 1