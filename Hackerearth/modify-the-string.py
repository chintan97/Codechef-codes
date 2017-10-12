#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/modify-the-string/
#Chintan Patel 23-12-2016

S = raw_input()
ans = list()
for i in S:
	if i.isupper():
		ans.append(i.lower())
	else:
		ans.append(i.upper())

print ''.join(ans)