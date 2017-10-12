#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/final-destination-cakewalk/
#Chintan Patel 10-1-2016

x,y = 0,0
S = raw_input()
for i in S:
	if i == 'L':
		x -= 1
	elif i == 'R':
		x += 1
	elif i == 'U':
		y += 1
	else:
		y -= 1
print x,y