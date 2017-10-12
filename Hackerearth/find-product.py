#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-product/
#Chintan Patel 10-1-2016

N = input()
A = [int(x) for x in raw_input().split()]
ans = 1
for i in A:
	ans *= i
print ans%1000000007