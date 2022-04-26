import pygame
from utilities import *
from Piece import Piece

class Board:
	def __init__(self):
		self.selected = None
		self.board = [[None for i in range(8)] for j in range(8)]
		for row in range(3):
			offset = -1
			if (row % 2 == 0):
				offset = 1
			for col in range(((row % 2)), 8, 2):
				self.board[row][col] = Piece(WHITE)
			for col in range((row % 2) + offset, 8, 2):
				self.board[row + 5][col] = Piece(RED)
	
	def movePiece(self, rowCol):
		row, col = rowCol
		if (row >= 0) & (row < 8) & (col >= 0) & (col < 8): # if selecting within the board
			piece = self.board[row][col]
			if (piece != None): # if there is a piece to select
				self.selected = (rowCol, piece)
			elif (self.selected != None) & (piece == None): # if there is a selection and the tile is empty
				selectedRow, selectedCol = self.selected[0]
				rowOffset = row - selectedRow
				colOffset = col - selectedCol
				absRowOffset = abs(rowOffset)
				# if move is diagonal & move is no further than 2 tiles
				if (absRowOffset == abs(colOffset)) & (absRowOffset <= 2):
					canMove = True
					selectedPiece = self.selected[1]
					if (selectedPiece.isKing == False): # if not a king
						if (selectedPiece.color == WHITE) & (rowOffset < 0): # white piece moving up
							canMove = False
						elif (selectedPiece.color == RED) & (rowOffset > 0): # red piece moving down
							canMove = False
					if (canMove == True):
						capturePiece = None
						if (absRowOffset == 2): # if moving 2 spaces
							capturePiece = self.board[int(selectedRow + rowOffset * 0.5)][int(selectedCol + colOffset * 0.5)]
							if (capturePiece != None): # if there is a piece to capture
								if (capturePiece.color != selectedPiece.color): # if not the same piece color
									self.board[selectedRow][selectedCol] = None
									self.board[row][col] = selectedPiece
									self.board[int(selectedRow + rowOffset * 0.5)][int(selectedCol + colOffset * 0.5)] = None
									self.selected = None
						elif (absRowOffset == 1): # if moving 1 space
							self.board[selectedRow][selectedCol] = None
							self.board[row][col] = selectedPiece
							self.selected = None
						if (self.selected == None): # if the move was successful
							# check if the piece can become a king
							if (selectedPiece.color == WHITE) & (row == 7):
								self.board[row][col].isKing = True
							elif (selectedPiece.color == RED) & (row == 0):
								self.board[row][col].isKing = True
							if (capturePiece != None):
								return capturePiece

	def draw(self, screen):
		for row in range(8):
			for col in range(8):
				if (col % 2) == ((row + 1) % 2): # red board square (black squares are the background)
					pygame.draw.rect(screen,RED,((col*SQUARE_SIZE)+BOARD_COL_OFFSET,(row*SQUARE_SIZE)+BOARD_ROW_OFFSET,SQUARE_SIZE,SQUARE_SIZE))
				piece = self.board[row][col]
				if piece != None:
					piecePos = ((col*SQUARE_SIZE)+BOARD_COL_OFFSET+SQUARE_SIZE/2,(row*SQUARE_SIZE)+BOARD_ROW_OFFSET+SQUARE_SIZE/2)
					pieceRadius = SQUARE_SIZE * 0.4
					if (self.selected != None):
						if (self.selected[1] == piece):
							pygame.draw.circle(screen, GREEN, piecePos, pieceRadius * 1.1) # piece selected circle
					pygame.draw.circle(screen, piece.color, piecePos, pieceRadius) # piece
					if (piece.isKing == True):
						pygame.draw.circle(screen, YELLOW, piecePos, pieceRadius * 0.5) # king indicator