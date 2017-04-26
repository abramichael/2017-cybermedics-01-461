from random import random
class Player:

	def __init__(self, name):
		self.hp = 50
		self.name = name

	def kick(self, p, force):
		pr = random()
		f = force / 10.0 - 0.02
		if pr < f:
			print "%s missed." % self.name
		else:
			p.hp -= force
			print "%s kicked %s. HP of %s is %s" \
				% (self.name, p.name, p.name, p.hp)

	def is_alive(self):
		#if self.hp > 0:
		#	return True
		#else:
		#	return False
		return self.hp > 0

