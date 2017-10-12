#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/count-divisors/
#Chintan Patel 10-1-2016

cnt = 0
l,r,k = [int(x) for x in raw_input().split()]
for i in range(l,r+1):
	if i%k == 0:
		cnt += 1
print cnt