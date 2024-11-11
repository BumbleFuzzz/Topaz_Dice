import random as r

class DICE:
		def __init__(self, am, si):
				self.amount = am
				self.sides = si
				self.name = str(self.amount) + "d" + str(self.sides)
		def roll(self):
				rolled = []
				for x in range(1, self.amount + 1):
						rolled.append(r.randint(1, self.sides))
				return rolled

def rollADice(whatDice):				
		whatDice = whatDice.lower()

		l = len(whatDice)
		i = 0
		numberOfDice = ""
		numberOfSides = ""

		while True:
				if whatDice[i] != "d":
						numberOfDice = numberOfDice + whatDice[i]
						i += 1
				elif whatDice[0] == "d":
					numberOfDice = "1"
					i += 1
					numberOfSides = numberOfSides + whatDice[i:]
					break
				else:
						i += 1
						numberOfSides = numberOfSides + whatDice[i:]
						break

		rolledDice = DICE(int(numberOfDice), int(numberOfSides))
		theRoll = rolledDice.roll()
		return theRoll
		