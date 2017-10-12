#https://www.codechef.com/problems/COLOR
#Chintan Patel 21-12-2016

T = input()
while T>0:
	N = input()
	S = raw_input()
	rc = 0
	gc = 0
	bc = 0
	for i in S:
		if i == 'R':
			rc += 1
		elif i == 'G':
			gc += 1
		else:
			bc += 1
	
	max = rc if rc>=gc and rc>=bc else gc if gc>=rc and gc>=bc else bc
	print N-max
	T -= 1