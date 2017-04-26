from player import Player

#name1 = raw_input("Enter Player 1 name: ")
#name2 = raw_input("Enter Player 2 name: ")

name1 = "Kutepa"
name2 = "Tamindarova"

player1 = Player(name1)
player2 = Player(name2)


while player1.is_alive() and player2.is_alive():
	force = input("%s, enter force: " % player1.name)
	player1.kick(player2, force)
	if (player2.is_alive()):
		force = input("%s, enter force: " % player2.name)
		player2.kick(player1, force)

print "GAME OVER...HA-HA-HA"