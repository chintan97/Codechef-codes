#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/digit-problem/
#Chintan patel 10-1-2016

ans = []
X,K = [str(x) for x in raw_input().split()]
K = int(K)
for i in X:
	if i != '9' and K > 0:
		ans.append('9')
		K -= 1
	else:
		ans.append(i)
print ''.join(ans)