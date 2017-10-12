#https://www.hackerearth.com/challenge/college/cc4/algorithm/keep-counting/

N, T = [int(x) for x in raw_input().split()]
A = [int(x) for x in raw_input().split()]
count = 0
def subset_sum(numbers, target, partial=[]):
	global count
	s = sum(partial)
	
	if s == target:
		count += 1
	if s >= target:
		return
	for i in range(len(numbers)):
		n = numbers[i]
		remaining = numbers[i+1:]
		subset_sum(remaining, target, partial + [n])
	return count
print subset_sum(A, T)