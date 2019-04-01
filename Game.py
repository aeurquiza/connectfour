import Board 
import Player
import Piece

class Game():

	def play(self):
		play_again = 'y'
		while( play_again == 'y' ):
			print "Please choose the board spacing: "
			board_size = int(raw_input())
			game_board =  Board.Board(board_size)
			print "Type the column in which you wish to move."
			turn_counter = 1
			players = (Player.Player('R',1), Player.Player('B',2))
			player_turn = 0
			while( game_board.winner != True):
				game_board.print_board()
				print "Turn %i: Player %i (%s), choose your move: "%(turn_counter, players[player_turn].number, players[player_turn].color)
				selection = int(raw_input())
				print "\n"
				move_made = game_board.make_move(selection - 1, Piece.Piece(players[player_turn].color) )
				if not move_made:
					print "Invalid move, Try Again."
				else:
					if player_turn == 0:
						player_turn = 1
					else:
						player_turn = 0
				if game_board.is_board_full():
					print "ITS A TIE"
					break
			print "Play again? (y/n): "
			play_again = raw_input()
		print "Goodbye! "

