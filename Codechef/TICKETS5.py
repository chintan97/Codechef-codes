#https://www.codechef.com/problems/TICKETS5
#Chintan Patel 21-12-2016

T = input()
while T>0:
	S = raw_input()
	
	a = S[0]
	b = S[1]
	
	if a == b:
		print "NO"
	else:
		temp = 0
		x = len(S)
		for i in S:
			if temp%2 == 0 and i == a:
				temp += 1
				continue
			elif temp%2 == 1 and i == b:
				temp += 1
				continue
			else:
				break
		
		if temp == len(S):
			print "YES"
		else:
			print "NO"
			
	T -= 1