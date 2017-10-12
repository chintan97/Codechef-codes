#https://www.codechef.com/problems/TACHSTCK
#Chintan Patel 2-1-2016

N,D = [int(x) for x in raw_input().split()]
C = list()
cnt = 0
for i in range(N):
	C.append(input())
C.sort()
i = 0
while i < len(C)-1:
	if abs(C[i]-C[i+1]) <= D:
		cnt += 1
		i += 2
	else:
		i += 1
		
print cnt