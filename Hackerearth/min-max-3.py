#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/min-max-3/
#Chintan Patel 10-1-2016

flag = 0
N = input()
A = [int(x) for x in raw_input().split()]
maxv = max(A)
B = list(set(A))
for i in range(1,len(B)+1):
	if i == B[i-1]:
		continue
	else:
		flag = 1
		print 'NO'
		break
if flag != 1:
	print 'YES'