#https://www.codechef.com/problems/ERROR
#Chintan Patel 28-12-2016

T = input()
while T>0:
	S = raw_input()
	if S.find('010') == -1 and S.find('101') == -1:
		print 'Bad'
	else:
		print 'Good'
	T -= 1 