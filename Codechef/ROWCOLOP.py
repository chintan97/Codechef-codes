#https://www.codechef.com/problems/ROWCOLOP
#Chintan Patel 2-1-2016

N,Q = [int(x) for x in raw_input().split()]
A = [0]*(N*N)
while Q:
	I,J,K = [str(x) for x in raw_input().split()]
	if I == 'RowAdd':
		for i in range(int(J)-1,int(J)*N):
			A[i] += int(K)
	else:
		for i in range(int(J)-1,N*N,N):
			A[i] += int(K)
	Q -= 1
print max(A)