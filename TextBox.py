import pygame

class TextBox:
	def __init__(self, text, color, bgColor, rectProps, padding, font):
		self.text = font.render(text, True, color) # render(text, antialias, color, background)
		self.textRect = self.text.get_rect() # get_rect(**kwargs) kwargs = pygame rect attributes https://bit.ly/3EldFKR
		if (isinstance(rectProps, dict)):
			for rectProp in rectProps:
				setattr(self.textRect, rectProp, rectProps[rectProp])
		self.boundingBox = self.textRect.inflate(padding, padding)
		self.bgColor = bgColor

	def get_rect(self):
		return self.boundingBox

	def draw(self, screen):
		if (self.bgColor != None):
			pygame.draw.rect(screen, self.bgColor, self.boundingBox)
		screen.blit(self.text, self.textRect) # blit(source, dest)