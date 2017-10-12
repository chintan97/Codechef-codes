#https://www.codechef.com/problems/LUCKYSTR
#Chintan Patel 2-1-2016

K,N = [int(x) for x in raw_input().split()]
L = []
for i in range(K):
	L.append(str(raw_input()))
for i in range(N):
	S = str(raw_input())
	if len(S) >= 47:
		print 'Good'
	else:
		flag = 0
		for j in range(K):
			if S.find(L[j]) != -1:
				print 'Good'
				flag = 1
				break
		if flag == 0:
			print 'Bad'