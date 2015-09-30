import time
from msvcrt import getch

x = 1
y = 6
z = 1

Spooky = "Spooky visits you"

Spooky2 = "Spooky snake visits you"
spookystart = 12
spookyChange = 17

def drawSpooky(start, finish):
	##Draws Spooky's body
	time.sleep(.07)
	for x in range (start, finish):
		print "",
	print Spooky
	
def drawHead(start, finish):
	##Draws spookys head
	time.sleep(.07)
	for x in range (start, finish):
		print "",
	print Spooky2[:-(spookyChange)]
	
	
	
for z in range (0, 9):
	drawHead(0, spookystart)
	spookyChange = spookyChange - 2
	spookystart = spookystart - 1

while True:
	drawSpooky(0, y)
	if y == 1 or y ==  7:
		drawSpooky(0, y)
		drawSpooky(0, y)
	if y == 2 or y == 6:
		drawSpooky(0, y)
	if y ==  7:
		y = 6
		z =  7
	elif y == 1:
		y = 2
		z = 1
	elif y > z:
		y = y + 1
		z = z + 1
	else:
		y = y - 1
		z = z - 1



