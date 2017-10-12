#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/the-great-kian/
#Chintan Patel 10-1-2016

n = input()
fc,sc,tc = 0,0,0
A = [int(x) for x in raw_input().split()]
for i in range(n):
	if i%3 == 0:
		fc += A[i]
	elif i%3 == 1:
		sc += A[i]
	else:
		tc += A[i]
print fc,sc,tc