#https://www.hackerearth.com/challenge/college/cc4/algorithm/hateful-three/

from fractions import gcd
import math
T = input()
def lcm(x, y):
	return (x*y) // gcd(x, y)
while T:
	A = []
	N = input()
	if N == 1:
		print 1
	elif N == 2:
		print 2
	elif N == 3:
		print 6
	elif N == 4:
		print 12
	elif N == 5 or N == 6:
		print 60
	else:
		if N % 6 == 0:
			print lcm(N-1, lcm(N-2, N-3))
		elif N % 2 == 0:
			print lcm(N, lcm(N-1, N-3))
		else:
			print lcm(N, lcm(N-1, N-2))
	T -= 1