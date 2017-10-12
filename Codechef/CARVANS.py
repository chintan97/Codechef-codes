#https://www.codechef.com/problems/CARVANS
#Chintan Patel 27-12-2016

T = input()
S = list()
while T>0:
	N = input()
	S = [int(x) for x in raw_input().split()]
	m = S[0]
	cnt = 1
	for i in range(1,N):
		if m >= S[i]:
			cnt += 1
		
		m = min(m,S[i])
		
	print cnt	
	T -= 1