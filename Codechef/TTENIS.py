#https://www.codechef.com/problems/TTENIS
#Chintan Patel 20-12-2016

T = input()
while T>0:
	S = raw_input()
	flag = 0
	zcnt = 0
	ocnt = 0
	for i in S:
		if zcnt >= 10 and ocnt >= 10:
			if i == '1' and pre == '1':
				flag = 0
			elif i == '0' and pre == '0':
				flag = 1
				
		if i == '1':
			ocnt += 1
			pre = '1'
		else:
			zcnt += 1
			pre = '0'
		
	if ocnt >= 11 and flag == 0:
		print "WIN"
	else:
		print "LOSE"
		
	T -= 1