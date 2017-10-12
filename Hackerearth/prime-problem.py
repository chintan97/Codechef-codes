#https://www.hackerearth.com/challenge/college/cc4/algorithm/prime-problem/
import math
T = input()
while T:
	val = input()
	i = 3
	flag = 0
	if val == 2:
		flag = 0
	elif val % 2 == 0 or val == 0 or val == 1:
		flag = 1
	else:
		x = math.floor(math.sqrt(val))
		while i <= x:
			if val % i == 0:
				flag = 1
				break
			i += 2
	print "True" if flag == 0 else "False"
	T -= 1