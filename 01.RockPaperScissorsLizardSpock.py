import random

print """Welcome to rock - paper - scissors - lizard - Spock!
The rules are simple:\n
1. Scissors cuts Paper
2. Paper covers Rock
3. Rock crushes Lizard
4. Lizard poisons Spock
5. Spock smashes Scissors
6. Scissors decapitates Lizard
7. Lizard eats Paper
8. Paper disproves Spock
9. Spock vaporizes Rock
10. Rock crushes Scissors\n"""

weapons = ('rock', 'Spock', 'paper', 'lizard', 'scissors')

while True:
	player_choice = raw_input("Choose your weapon or type 'exit' to quit: ")

	#check if player's choice is valid
	if player_choice in weapons:
		player_number = weapons.index(player_choice)
	elif player_choice == "exit":
		print "GAME OVER"
		print "Thank you for playing!\n"
		break
	else:
		print "You have to choose between rock, paper, scissors, lizard or Spock (case-sensitive). Please, try again.\n"
		continue

	#generate random choice for the computer
	comp_number = random.randrange(5)

	print "Player chooses", weapons[player_number]
	print "Computer chooses", weapons[comp_number]

	#check who wins the game and print result
	result = (player_number - comp_number) % 5
	if result == 0:
		print "Player and computer tie!\n"
	elif result == 1 or result == 2:
		print "Player wins!\n"
	else:
		print "Computer wins!\n"
