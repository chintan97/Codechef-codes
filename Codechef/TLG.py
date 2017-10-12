#https://www.codechef.com/problems/TLG
#Chintan Patel 3-1-2016

N = input()
max = 0
S1,S2 = 0,0
for i in range(N):
	P1, P2 = [int(x) for x in raw_input().split()]
	S1 += P1
	S2 += P2
	if max < S1-S2 and S1 > S2:
		max = S1-S2
		W = 1
	elif max < S2-S1 and S2 > S1:
		max = S2-S1
		W = 2
print W,max