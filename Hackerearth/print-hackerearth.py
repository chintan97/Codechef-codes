#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/print-hackerearth/
#Chintan Patel 10-1-2016

N = input()
S = raw_input()
hc = S.count('h')/2
ac = S.count('a')/2
cc = S.count('c')
kc = S.count('k')
ec = S.count('e')/2
rc = S.count('r')/2
tc = S.count('t')
print min(hc,ac,cc,kc,ec,rc,tc)