#https://www.codechef.com/JAN17/problems/CAPIMOVE
 
T = input()
A = list()
while T:
	del A[:]
	N = input()
	P = [int(x) for x in raw_input().split()]
	arr_temp = list(P)
	#print arr_temp
	for i in range(N-1):
		A.append(raw_input())
	for i in range(N):
		#print P
		temp = P.index(max(P[:i]+P[i+1:]))+1
		x = str(str(i+1) + " " + str(temp))
		y = str(str(temp) + " " + str(i+1))
		#print x,y
		if A.count(x) == 0 and A.count(y) == 0:
			print temp,
		else:
			while True:
				P.remove(P[temp-1])
				if len(P) != 1:
					temp = P.index(max(P[:i]+P[i+1:]))+1
				x = str(str(i+1) + " " + str(temp))
				y = str(str(temp) + " " + str(i+1))
				if A.count(x) == 0 and A.count(y) == 0:
					print temp,
					P = list(arr_temp)
					break
				elif len(P) == 1:
					print 0,
					P = list(arr_temp)
					break
	print '\n'
	T -= 1 