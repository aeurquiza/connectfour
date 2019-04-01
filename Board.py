import Piece 
from time import sleep
from random import randint

class Board:
	GRID_WIDTH = 7
	GRID_HEIGHT = 6
	SIMULATION_SPEED = .1

	def __init__(self, game_size):
		self.grid = [ [ None for x in range(self.GRID_WIDTH) ] for y in range(self.GRID_HEIGHT) ]
		self.full_columns = set()
		self.winner = False
		self.game_size = game_size

	def is_board_full(self):
		return len(self.full_columns) == 7

	def simulate_activity(self):
		color_dict = { True: "O", False: "I" }
		selection = True
		while( len(self.full_columns) != 7 and not self.winner ):
			self.make_move(randint(0,6), Piece.Piece(color_dict[selection]))
			selection = not selection
		if not self.winner:
			print "ITS A TIE!"

	def print_board(self):
		board_state = "+"+7*(self.game_size*2*"-"+"-+")+"\n"
		for row in self.grid:
			board_state += "+"
			for piece in row:
				if piece == None:
					board_state += 2*self.game_size*" "+" |"
				else:
					board_state += (self.game_size*" ")+str(piece.get_piece_color())+(self.game_size*" ")+"|"
			board_state += "\n+"+7*(self.game_size*2*"-"+"-+")+"\n"
		board_state += " "+self.game_size*" "+(2*self.game_size*" "+" ").join(['1','2','3','4','5','6','7'])
		print board_state + "\n"

	def first_available_index(self, column):
		if self.grid[0][column] != None:
			return -1
		if self.grid[5][column] == None:
			return 5

		for i in range(1, 6):
			if self.grid[i][column] != None:
				return i - 1


	def make_move(self, slot, piece):
		insert_index = self.first_available_index(slot)
		if insert_index != -1:
			self.simulate_insertion(slot, piece, insert_index)
			self.grid[insert_index][slot] = piece
			self.print_board()
			if self.check_win(insert_index, slot, piece.get_piece_color()):
				self.winner = True
				print piece.get_piece_color() + " WINS!"
			return True
		else:
			self.full_columns.add(slot)
			print "Column is full"
			return False

	def simulate_insertion(self, slot, piece, insert_index):
		for i in range(0, insert_index):
			self.grid[i][slot] = piece
			self.print_board()
			self.grid[i][slot] = None
			sleep(self.SIMULATION_SPEED)

	def check_win(self, pos, col, color):
		return self.check_vertical(pos,col,color) or self.check_horizontal(pos,col,color) or self.check_diagonals(pos,col,color)

	def check_diagonals(self, pos, col, color):
		return self.check_right_diagonal(pos,col, color) or self.check_left_diagonal(pos, col, color)

	def check_vertical(self, pos, col, color):
		match_counter = 0
		for i in range(pos, 6):
			if self.grid[i][col].get_piece_color() == color:
				match_counter += 1
			else:
				return False
			if match_counter == 4:
				return True
		return False

	def check_horizontal(self, pos, col, color):
		match_counter = 0
		slider = 1
		searching_right = True
		reach_left_edge = False
		while searching_right:
			if (col + slider ) < 7 and self.grid[pos][col+slider] != None and self.grid[pos][col+slider].get_piece_color() == color:
				match_counter += 1
				slider += 1
			else:
				searching_right = False
		slider = -1
		while not reach_left_edge:
			if (col + slider ) > -1 and self.grid[pos][col+slider] != None and self.grid[pos][col+slider].get_piece_color() == color:
				match_counter += 1
				slider -= 1
			else:
				reach_left_edge = True
		return match_counter >= 3

	def check_right_diagonal(self, pos, col, color):
		match_counter = 0
		right_slider = 1
		up_slider = 1
		searching_right = True
		reach_left_edge = False
		while searching_right:
			if (col + right_slider ) < 7 and( pos + up_slider ) < 6 and self.grid[pos + up_slider][col+ right_slider] != None and self.grid[pos + up_slider][col+right_slider].get_piece_color() == color:
				match_counter += 1
				right_slider += 1
				up_slider += 1
			else:
				searching_right = False
		right_slider = -1
		up_slider = -1
		while not reach_left_edge:
			if (col + right_slider ) > -1 and( pos + up_slider ) > -1  and self.grid[pos + up_slider][col+ right_slider] != None and self.grid[pos + up_slider][col+right_slider].get_piece_color() == color:
				match_counter += 1
				right_slider -= 1
				up_slider -=1
			else:
				reach_left_edge = True
		return match_counter >= 3

	def check_left_diagonal(self, pos, col, color):
		match_counter = 0
		right_slider = 1
		up_slider = -1
		searching_right = True
		reach_left_edge = False
		while searching_right:
			if (col + right_slider ) < 7 and ( pos + up_slider ) > -1 and self.grid[pos + up_slider][col+ right_slider] != None and self.grid[pos + up_slider][col+right_slider].get_piece_color() == color:
				match_counter += 1
				right_slider += 1
				up_slider -= 1
			else:
				searching_right = False
		right_slider = -1
		up_slider = 1
		while not reach_left_edge:
			if (col + right_slider ) > -1 and ( pos + up_slider ) < 6  and self.grid[pos + up_slider][col+ right_slider] != None and self.grid[pos + up_slider][col+right_slider].get_piece_color() == color:
				match_counter += 1
				right_slider -= 1
				up_slider +=1
			else:
				reach_left_edge = True
		return match_counter >= 3