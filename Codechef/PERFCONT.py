#https://www.codechef.com/OCT17/problems/PERFCONT
#Chintan Patel 7-10-2017

T = input()
while T:
	N, P = [int(x) for x in raw_input().split()]
	solve = [int(x) for x in raw_input().split()]
	hard_count, cakewalk_count, i = 0, 0, 0
	hard_limit = int(P/10)
	cakewalk_limit = int(P/2)
	while True:
		if hard_count > 2 or cakewalk_count > 1:
			break
		else:
			if i == N:
				break
			if solve[i] <= hard_limit:
				hard_count += 1
			elif solve[i] >= cakewalk_limit:
				cakewalk_count += 1
			i += 1
	print "yes" if hard_count == 2 and cakewalk_count == 1 else "no"
	T -= 1