import pygame
from utilities import WIDTH, HEIGHT, WHITE, BLUE, PARAGRAPH_FONT
from TextBox import TextBox

class MainMenu:
	def __init__(self):
		self.buttons = [
			[TextBox("Start", WHITE, BLUE, {"center": (WIDTH/2, HEIGHT/2)}, 32, pygame.font.SysFont(*PARAGRAPH_FONT)), "Game"]
		]
	
	def processClick(self, mousePos):
		for button in self.buttons:
			buttonRect = button[0].get_rect()
			if (buttonRect.collidepoint(mousePos)):
				return button[1]
		
	def draw(self, screen):
		for button in self.buttons:
			button[0].draw(screen)
