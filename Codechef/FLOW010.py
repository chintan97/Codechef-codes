#https://www.codechef.com/problems/FLOW010
#Chintan Patel 24-12-2016

T = input()
while T>0:
	ch = raw_input()
	if ch.lower() == 'b':
		print 'BattleShip'
	elif ch.lower() == 'c':
		print 'Cruiser'
	elif ch.lower() == 'd':
		print 'Destroyer'
	else:
		print 'Frigate'
	T -= 1