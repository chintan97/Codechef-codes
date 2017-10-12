#https://www.codechef.com/problems/AMR15A
#Chintan Patel 23-12-2016

N = input()
A = list()
A = [int(x) for x in raw_input().split()]
oc = 0
ec = 0
for i in A:
	if i%2 == 0:
		ec += 1
	else:
		oc += 1
		
if ec > oc:
	print 'READY FOR BATTLE'
else:
	print 'NOT READY'