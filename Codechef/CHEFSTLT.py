#https://www.codechef.com/problems/CHEFSTLT
#Chintan Patel 23-12-2016

T = input()
while T>0:
	s1 = raw_input()
	s2 = raw_input()
	min = 0
	max = 0
	for i in range(0,len(s1)):
		if s1[i] != '?' and s2[i] != '?':
			if s1[i] != s2[i]:
				min += 1
				max += 1
		
		elif s1[i] == '?' or s2[i] == '?':
			max += 1
		
		elif s1[i] == '?' and s2[i] == '?':
			max += 1
		
	print min,max		
	T -= 1