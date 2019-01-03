class Character:
	def __init__(self):
		self.health = 100
		self.attack = 10
		self.defence = 5
		self.speed = 5

	def getHealth(self):
		return self.health
	def setHealth(self, newHealth):
		self.health = newHealth

	def getAttack(self):
		return self.attack
	def setAttack(self, newAttack):
		self.attack = newAttack

	def getDefence(self):
		return self.defence
	def setDefence(self, newDefence):
		self.defence = newDefence

	def getSpeed(self):
		return self.speed
	def setSpeed(self, newSpeed):
		self.speed = newSpeed

class Paladin(Character):
    def __init__(self):
        self.health = 200
        self.attack = 12
        self.defence = 10
        self.speed = 4

class Mage(Character):
	def __init__(self):
		self.health = 120
		self.attack = 18
		self.defence = 5
		self.speed = 8

class Warrior(Character):
	def __init__(self):
		self.health = 240
		self.attack = 16
		self.defence = 4
		self.speed = 8
