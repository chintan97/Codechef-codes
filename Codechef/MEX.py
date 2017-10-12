#https://www.codechef.com/OCT17/problems/MEX
#Chintan Patel 8-10-2017

T = input()
while T:
	N, K = [int(x) for x in raw_input().split()]
	S = [int(x) for x in raw_input().split()]
	S.sort()
	i, j = 0, 0
	S.append(-1)
	if K == 0:
		while True:
			if j < N and i == S[j]:
				i += 1
				j += 1
			else:
				print i
				break
	else:
		while True:
			if j < N and i == S[j] and S[j] == S[j+1]:
				j += 1
			elif j < N and i == S[j] and S[j] != S[j+1]:
				i += 1
				j += 1
			elif j < N and K > 0 and i != S[j]:
				K -= 1
				i += 1
			else:
				break
		print i+K
	T -= 1