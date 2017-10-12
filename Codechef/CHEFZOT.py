#https://www.codechef.com/problems/CHEFZOT
#Chintan Patel 2-1-2016

N = input()
A = [int(x) for x in raw_input().split()]
i = 0
max = 0
while i < N:
	cnt = 0
	while True:
		if i < N and A[i] != 0:
			cnt += 1
			i += 1
		else:
			i += 1
			if max < cnt:
				max = cnt
			break
print max