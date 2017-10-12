#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/addition-aint-simple/
#Chintan Patel 11-1-2016

T = input()
ans = []
while T:
	del ans[:]
	S = raw_input().lower()
	i = 0
	j = len(S)-1
	while i <= j:
		temp = ((ord(S[i])-96)+(ord(S[j])-97))%26
		ans.append(chr(temp+97))
		i += 1
		j -= 1
	A = ''.join(ans)
	if len(S)%2 == 1:
		temp = A[:len(A)-1]
		B = A+temp[::-1]
	else:
		B = A+A[::-1]
	print B
	T -= 1