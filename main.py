import pygame
from utilities import WIDTH, HEIGHT, BLACK
from MainMenu import MainMenu
from Game import Game

pygame.init()

def handleEvents(menu):
	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
			exit()
		
		elif (event.type == pygame.MOUSEBUTTONDOWN):
			result = menu.processClick(pygame.mouse.get_pos())
			return result

		elif (event.type == pygame.KEYDOWN):
			if (event.key == pygame.K_ESCAPE):
				return False

	return True

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Real Time Checkers")

def draw(menu):
	screen.fill(BLACK)
	menu.draw(screen)
	pygame.display.flip()

fps = 60
clock = pygame.time.Clock()

def menuTransistion(menuStr):
	menu = globals()[menuStr]()
	running = True
	while running:
		clock.tick(fps)
		result = handleEvents(menu)
		if (result != True) & (result != False) & (result != None):
			menuTransistion(result)
			result = True
		if (result == True) | (result == False):
			running = result
		draw(menu)

menuTransistion("MainMenu")