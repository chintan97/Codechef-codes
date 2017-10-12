#https://www.codechef.com/problems/CHEFSTUD
#Chintan Patel 19-12-2016

T = input()
while T>0:
	i = 0
	cnt = 0
	str = raw_input()
	while i<len(str)-1:
		if str[i]=='<' and str[i+1]=='>':
			cnt += 1
			i += 2
		else:
			i += 1
	
	print cnt
	T -= 1