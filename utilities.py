import pygame

WIDTH = 640
HEIGHT = 480

BOARD_ROW_OFFSET = HEIGHT / 8
BOARD_COL_OFFSET = 0
if WIDTH > HEIGHT:
	BOARD_COL_OFFSET = ((WIDTH - HEIGHT) / 2) + BOARD_ROW_OFFSET / 2
elif HEIGHT > WIDTH:
	BOARD_ROW_OFFSET += (HEIGHT - WIDTH) / 2

SQUARE_SIZE = (min(WIDTH, HEIGHT - BOARD_ROW_OFFSET) / 8)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# SysFont(name, size, bold, italic)
HEADER_FONT = ("verdana", int(WIDTH/16), True)
PARAGRAPH_FONT = ("verdana", int(WIDTH/32), True)

def rowColFromCoord(coord):
	x, y = coord
	row = int((y - BOARD_ROW_OFFSET) // SQUARE_SIZE)
	col = int((x - BOARD_COL_OFFSET) // SQUARE_SIZE)
	return row, col