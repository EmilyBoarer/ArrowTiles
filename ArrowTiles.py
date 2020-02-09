import pygame
import random
import sys
import time

data=[]
for n in range(10):
	data.append(random.randint(0,2))

score=0

WIDTH=256+128		
HEIGHT=512+128		

LENGTH=200			
move=0				

colour=(17,142,11)
										
pygame.init()
pygame.font.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
scorefont=pygame.font.SysFont('Century Gothic', 75)

def press(col):
	global score
	global move
	global LENGTH
	global colour
	if data[0] == col:
		data.pop(0)							
		score+=1							
		data.append(random.randint(0,2))	
		move=LENGTH						
		time.sleep(0.1)
		colour=(17,142,11)
	else:								
		score-=3						
		time.sleep(0.1)
		colour=(200,0,0)
	
while True:
	#update
	for event in pygame.event.get():
		if event.type == 12:
			pygame.quit()
			sys.exit()
	if move <= LENGTH-(LENGTH/3):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			press(0)							
		if keys[pygame.K_DOWN]:
			press(1)							
		if keys[pygame.K_RIGHT]:
			press(2)							
	
	if move > 0:	move-=2
	if move < 0:	move=0
	#draw
	screen.fill((204,204,204))
	c=colour
	for i in range(5):																						#	loop through visible tiles
		x=(WIDTH/3)*data[i]
		y=(HEIGHT-100)-(((i+1)*LENGTH)+move)
		pygame.draw.rect(screen, c, (x,y,WIDTH/3,LENGTH), 0)											#	render tiles
		c=(0,0,0)																						#	set colour back to black for other tiles
	screen.blit(scorefont.render(str(score), False, (0, 0, 0)),(15,HEIGHT-90))								#	render text
	pygame.display.flip()


