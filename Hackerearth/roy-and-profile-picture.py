#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/roy-and-profile-picture/
#Chintan Patel 10-1-2016

L = input()
N = input()
while N:
	W,H = [int(x) for x in raw_input().split()]
	if W == H and W >= L:
		print 'ACCEPTED'
	elif W < L or H < L:
		print 'UPLOAD ANOTHER'
	else:
		print 'CROP IT' 
	N -= 1