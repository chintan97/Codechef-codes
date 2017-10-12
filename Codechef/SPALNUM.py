#https://www.codechef.com/problems/SPALNUM
#Chintan Patel 23-12-2016

T = input()
def pal(x,y):
	s = 0
	for i in range(x,y+1):
		temp = i
		ch = 0
		while temp > 0:
			ch = (temp%10) + (ch*10)
			temp /= 10
			
		if i == ch:
			s += i
			
	return s
	
while T>0:
	L,R = [int(x) for x in raw_input().split()]
	print pal(L,R)
	T -= 1