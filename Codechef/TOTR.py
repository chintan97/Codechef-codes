#https://www.codechef.com/problems/TOTR
#Chintan Patel 31-12-2016

T,M = [str(x) for x in raw_input().split()]
T = int(T)
while T>0:
	S = raw_input()
	ans = []
	for i in S:
		if i == '_':
			ans.append(' ')
		elif i.isalpha():
			if i.isupper():
				temp = ord(i)-65
				ans.append(M[temp].upper())
			else:
				temp = ord(i)-97
				ans.append(M[temp])
		else:
			ans.append(i)
				
	print ''.join(ans)
	T -= 1