#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/psychic-powers/
#Chintan Patel 10-1-2016

S = raw_input()
if S.find('000000') != -1 or S.find('111111') != -1:
	print 'Sorry, sorry!'
else:
	print 'Good luck!'