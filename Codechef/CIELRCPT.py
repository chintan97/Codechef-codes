#https://www.codechef.com/problems/CIELRCPT
#Chintan Patel 3-1-2016
 
T = input()
A = []
while T:
	sum = 0
	p = input()
	temp = 1
	while temp <= p and temp<=2048:
		A.append(temp)
		temp *= 2
	for i in range(len(A)-1,-1,-1):
		if p >= A[i]:
			temp = p/A[i]
			sum += temp
			p -= (temp*A[i])
		if p == 0:
			break
			
	print sum
	T -= 1 