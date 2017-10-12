n, m = [int(x) for x in raw_input().split()]
min_array = [0]*n
for i in range(n):
	X = [int(val) for val in raw_input().split()]
	min_array[i] = min(X)
print max(min_array)