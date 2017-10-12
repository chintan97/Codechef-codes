#https://www.codechef.com/problems/FLOW005
#Chintan Patel 24-12-2016

T = input()
while T > 0:
	N = input()
	coin = 100
	cnt = 0
	while N > 0:
		cnt += N/coin
		N -= coin * (N/coin)
		if (coin == 100): coin = 50
		elif (coin == 50): coin = 10
		elif (coin == 10): coin = 5
		elif (coin == 5): coin = 2
		elif (coin == 2): coin = 1
		
	print cnt
	T -= 1