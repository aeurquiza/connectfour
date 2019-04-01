import Board 
import Player
import Piece

class Game():

	def play(self):
		play_again = 'y'
		print "Please choose the board spacing:",
		board_size = int(raw_input())
		print "Type the column in which you wish to move."
		while( play_again == 'y' ):
			game_board =  Board.Board(board_size)
			game_board.print_board()
			turn_counter = 1
			players = (Player.Player('R',1), Player.Player('B',2))
			player_turn = 0
			while( game_board.winner == False and not game_board.is_board_full()):
				print "Turn %i: Player %i (%s), choose your move:"%(turn_counter, players[player_turn].number, players[player_turn].color),
				selection = int(raw_input())
				if selection < 1 or selection > 7:
					print "Invalid move, outside board, try again: "
				else: 
					move_made = game_board.make_move(selection - 1, Piece.Piece(players[player_turn].color) )
					if game_board.winner != False:
						if game_board.winner == 'B':
							print "Player 2 Wins! ",
						else:
							print "Player 1 Wins! ",
						break
					if game_board.is_board_full():
						print "Tie Game! ",
						break
					elif move_made != -1:
						print "Invalid move, column %i is full, try again: "%(move_made+1)
					else:
						turn_counter+=1
						if player_turn == 0:
							player_turn = 1
						else:
							player_turn = 0
			play_again = raw_input("Play again? (y/n): ")[0]
		print "Goodbye!"

