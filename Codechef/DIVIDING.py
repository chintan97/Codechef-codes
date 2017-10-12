#https://www.codechef.com/problems/DIVIDING
#Chintan Patel 28-12-2016

N = input()
C = [int(x) for x in raw_input().split()]
if sum(C) == ((N*(1+N))/2): print 'YES'
else: print 'NO'