#https://www.codechef.com/problems/CHEFCBA
#Chintan Patel 9-1-2016

a,b,c,d = [int(x) for x in raw_input().split()]
if a*b == c*d or a*c == b*d or a*d == b*c:
	print 'Possible'
else:
	print 'Impossible'