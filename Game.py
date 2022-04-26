import pygame
from utilities import WIDTH, HEIGHT, WHITE, RED, BLUE, HEADER_FONT, PARAGRAPH_FONT, rowColFromCoord
from Board import Board
from TextBox import TextBox

class Game:
	def __init__(self):
		self.board = Board()
		self.whitePieces = 12
		self.redPieces = 12
		self.winner = ""

	def reducePieceCount(self, color):
		if (color == WHITE):
			self.whitePieces -= 1
		elif (color == RED):
			self.redPieces -= 1
		if (self.whitePieces == 0):
			self.winner = "Red"
		elif (self.redPieces == 0):
			self.winner = "White"

	def processClick(self, mousePos):
		rowCol = rowColFromCoord(mousePos)
		capturedPiece = self.board.movePiece(rowCol)
		if (capturedPiece != None):
			self.reducePieceCount(capturedPiece.color)

	def draw(self, screen):
		self.board.draw(screen)
		if (self.winner != ""):
			winText = TextBox(self.winner + " wins!", WHITE, BLUE, {"center": (WIDTH/2, HEIGHT/2)}, 16, pygame.font.SysFont(*HEADER_FONT))
			winText.draw(screen)
		whiteText = TextBox("White Pieces: " + str(self.whitePieces), WHITE, None, (0,0), 0, pygame.font.SysFont(*PARAGRAPH_FONT))
		redText = TextBox("Red Pieces: " + str(self.redPieces), WHITE, None, {"topright": (WIDTH, 0)}, 0, pygame.font.SysFont(*PARAGRAPH_FONT))
		whiteText.draw(screen)
		redText.draw(screen)