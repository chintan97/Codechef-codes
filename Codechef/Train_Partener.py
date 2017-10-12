#https://www.codechef.com/problems/ANKTRAIN
#Chintan Patel 17-12-2016
x = list()
n = input()
for i in range(int(n)):
	num = input()
	x.append(int(num))
	
for i in range(int(n)):
	if x[i] in(3,6):
		if x[i]==3:
			print('6UB')
		else:
			print('3UB')
	if x[i] in(1,4):
		if x[i]==1:
			print('4LB')
		else:
			print('1LB')
	if x[i] in(2,5):
		if x[i]==2:
			print('5MB')
		else:
			print('2MB')
	if x[i] in (7,8):
		if x[i]==7:
			print('8SU')
		else:
			print('7SL')