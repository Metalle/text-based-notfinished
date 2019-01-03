from characters import *
#import characters

def main():
	pala = Paladin()
	warr = Warrior()
	mage = Mage()
	
	print("Paladin's health -> " + str(pala.getHealth()))
	pala.setHealth(4000)
	print("Paladin's new health -> " + str(pala.getHealth()))

main()