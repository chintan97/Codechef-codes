#https://www.codechef.com/problems/MAXDIFF
#Chintan Patel 28-12-2016

T = input()
while T>0:
	N,K = [int(x) for x in raw_input().split()]
	W = [int(x) for x in raw_input().split()]
	if K > N/2:
		K = N-K
	W.sort()
	W_kid = W[:K]
	W_chef = W[K:]
	print sum(W_chef) - sum(W_kid)
	T -= 1