#https://www.codechef.com/problems/LAPIN
#Chintan Patel 27-12-2016

T = input()
while T>0:
	S = raw_input()
	flag = 1
	if len(S)%2 == 0:
		ls = S[:len(S)/2]
		rs = S[len(S)/2:]
	else: 
		ls = S[:len(S)/2]
		rs = S[len(S)/2+1:]	
			
	for i in ls:
		if ls.count(i) == rs.count(i): 
			continue
		else:
			flag = 0
			break
	
	if flag == 0: print "NO"
	else: print "YES"
	T -= 1