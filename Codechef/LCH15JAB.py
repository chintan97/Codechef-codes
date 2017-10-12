#https://www.codechef.com/problems/LCH15JAB
#Chintan Patel 22-12-2016

T = input()
while T>0:
	str = raw_input()
	cnt = 1
	
	for i in str:
		if str.count(i) > cnt:
			cnt = str.count(i)
			
	if len(str) == 2*cnt:
		print 'YES'
	else:
		print 'NO'
	T -= 1