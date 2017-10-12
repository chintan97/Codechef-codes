#https://www.codechef.com/problems/RIGHTRI
#Chintan Patel 28-12-2016

N = input()
cnt = 0
while N>0:
	x1,y1,x2,y2,x3,y3 = [int(x) for x in raw_input().split()]
	d1 = ((x1-x2)**2 + (y1-y2)**2)
	d2 = ((x1-x3)**2 + (y1-y3)**2)
	d3 = ((x2-x3)**2 + (y2-y3)**2)
	if d1 == d2+d3 or d2 == d1+d3 or d3 == d1+d2:
		cnt += 1
	
	N -= 1
print cnt