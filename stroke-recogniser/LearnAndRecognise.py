import sys, pygame
from random import shuffle

from StrokeRecogniser import StrokeRecogniser

pygame.init()

screen = pygame.display.set_mode((320, 240))
paths = []
letters = [chr(c) for c in range (ord('a'), ord('c'))] * 3
g = StrokeRecogniser([])

print "You will be asked to draw the letters 'a' and 'b' three times."
print "After that you may draw the letters a and b at random and they will be recognised."
print "Draw the letters with a single stroke."
print "learning:", letters[0]

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		
		if event.type == pygame.MOUSEBUTTONDOWN:
			g.PenDown(event.pos)
			paths.append(g.path.points)
		if event.type == pygame.MOUSEMOTION:
			if g.down:
				g.PenTo(event.pos)
		if event.type == pygame.MOUSEBUTTONUP:
			if len(letters):
				g.Learn(letters[0], g.path.points)
				letters = letters[1:]
				if len(letters):
					print "learning:", letters[0]
				g.PenUp(event.pos)
			else:
				print "found:", g.PenUp(event.pos)
	
	screen.fill([255, 255, 255])
	[pygame.draw.aalines(screen, [0, 0, 0], False, p, 1) for p in paths if len(p) > 1]
	pygame.display.flip()

