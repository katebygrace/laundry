# This is a program to take inputs of type of clothes and output instructions on storing it; folding or hanging; and where to place it.
# I love my partner, but he doesn't know how to sort laundry. This is all in good fun (and his idea!)

####TODO
#Deal with spaces
#define hung vs hung pants vs folded and instructions on how to execute
#Add a random gen (one in 100) joke; for fun
#wrinkly if doghouse = true loop to zero


####DEFINITIONS

#hungOrFolded; to be refactored out later to specify instructions for hung and folded
hungOrFolded = "hung or folded" #or balled for socks! or hung pants

#definitions of JOSH locations
joshOwned = "Josh's "
whiteTeePile = "pile of white t-shirts"
coloredTeePile = "pile of colored t-shirts "
joshHang = "hangers where Josh's clothes get hung"
sportShortsPile = "pile of sport shorts"
jeansPile = "pile of jeans"
blackSockPile = "Black sock bucket"
whiteSockPile = "White sock bucket"
kitchenTowelPile = "kitchen bucket where towels go"

#definitions of KATE locations
kateOwned = "Kate's "
kateHang = "hangers where kates shirts get hung"
kateSockPile = "bucket where kate's socks go"
wrinklyPile = "the hanger section where wrinkly shirts go to get steamed/ironed"
tankTopPile = "the pile of tank tops"
pantsPile = "the pile of pants"
shortsPile = "the pile of shorts"
leggingsPile = "the pile of leggings"

#errordefs
unknownType = "The type could not be determined. "
useDiscretion = "Use discretion, or file an RFE. "

def steam():
	print("This will be a while wrinkled = true loop; but for now; for each wrinked clothes item; steam it. Also, be better.") #Eventually add while wrinkled loop

def dogHouse():
	areYouIn = input("Are you in the dog house? (Y/N) ").lower()
	if areYouIn == "yes" or areYouIn == 'y':
		steam()
		exit()
	else:
		print("Good. ")

def output(hung, typeOf, owned, final):
	print("Place the " + hung + " " + typeOf + " in " + owned + final)

def socks():
	yesOrNo = input("Warning! For efficiency, do socks at end. Is this your last items to put away?").lower()
	if yesOrNo == "yes" or yesOrNo == "y":
		kateSocks = input("Are there any littler socks?")
		if kateSocks == "yes" or kateSocks == "y":
			finalLocation = kateSockPile
			output(hungOrFolded, typeOfClothing, kateOwned, finalLocation)
		#This assumes there will be josh socks heh heh but there never won't be so ¯\_(ツ)_/¯
		print("Sort Josh socks into white or black socks and place in " + whiteSockPile + " or " + blackSockPile + ", respectively")
	else:
		print("Get back to work!!!!!!")

def JoshWardrobe():
	if typeOfClothing == "shirt":
		typeOfJoshShirt = input("What type of shirt? whiteTee, coloredTee, jersey, or dressShirt?").lower()
		if typeOfJoshShirt == "whitetee":
			finalLocation = whiteTeePile
			#fold(whiteTee)
		elif typeOfJoshShirt == "coloredtee":
			finalLocation = coloredTeePile
			#fold(coloredTee)
		elif typeOfJoshShirt == "dressshirt" or "jersey":
			finalLocation = joshHang
			#hang(dressShirt)
		else:
			finalLocation = joshHang
			print("(Error 1)" + unknownType + "This likely means its a Josh shirt that gets hung. " + useDiscretion)
			exit()
	elif typeOfClothing == "pants":
		typeOfJoshPants = input("What type of pants? dresspants, sportshorts, jeans, or other?").lower()
		if typeOfJoshPants == "dresspants":
			finalLocation = joshHang
			#hangPants(dresspants)
		elif typeOfJoshPants == "sportshorts":
			finalLocation = sportShortsPile
			#fold(sportShorts)
		elif typeOfJoshPants == "jeans":
			finalLocation = jeansPile
			#fold(jeans)
		else:
			finalLocation = sportShortsPile
			#fold(other)
			print("(Error 2) " + unknownType + "This likely means its a misc josh pant that gets folded." + useDiscretion)
			exit()
	else:
		print("(Error 3) " + unknownType + " Use discretion, or file an RFE. ")
		exit()
	output(hungOrFolded, typeOfClothing, joshOwned, finalLocation)

def wrinkly():
	wrinkly = input("Is it wrinkly (Y/N)?").lower()
	if wrinkly == "yes" or wrinkly == 'y':
		finalLocation = wrinklyPile
		output(hungOrFolded, typeOfClothing, kateOwned, finalLocation)
		exit()

#definition for Kate's wardrobe
def KateWardrobe():
#Add exception for certain type of wrinkly shirt later
	if typeOfClothing == "shirt":
		wrinkly()
		typeOfKateShirt = input("What type of shirt? tshirt, tanktop, sports tank top, jersey?").lower()
		if (typeOfKateShirt == "tshirt") or (typeOfKateShirt == "jersey") or (typeOfKateShirt == "dressshirt"):
			finalLocation = kateHang
			#fold(whiteTee)
		elif typeOfKateShirt == "tanktop":
			finalLocation = tankTopPile
			#fold(coloredTee)
		else:
			print("(Error 4) " + unknownType + " This likely means its a shirt that gets hung." + useDiscretion)
	elif typeOfClothing == "pants":
		typeOfKatePants = input("What type of pants? Leggings, pants, sportshorts, or shorts?").lower()
		if typeOfKatePants == "leggings":
			finalLocation = leggingsPile
			#hangPants(dresspants)
		elif typeOfKatePants == "pants":
			finalLocation = pantsPile
			#fold(sportShorts)
		elif typeOfKatePants == "jeans":
			finalLocation = athleticPile
			#fold(jeans)
		else:
			finalLocation = sportShortsPile
			#fold(other)
			print("(Error 5) The type could not be determined. This likely means it gets folded and put in " + sportShortsPile + ". Use discretion, or file an RFE.")
			exit()
			# 	if "pants"
	elif typeOfClothing == "dress":
		wrinkly()
	else:
		print("The type could not be determined. Use discretion, or file an RFE. ")
	output(hungOrFolded, typeOfClothing, kateOwned, finalLocation)

#definition for other placement
def OtherPlacement():
	whatIsIt = input("Is it a kitchen towel? (Y/N)").lower()
	if whatIsIt == "yes" or whatIsIt == "y":
		print("Place in " + kitchenTowelPile)
	else:
		print("You've reached an item without an owner that isn't categorized. Please file an RFE. ")

####EXECUTION

#Welcome Message, what typeOfClothing
print("Hello! Welcome to the laundry placement program.")
typeOfClothing = input("What is the type of clothing? Please type shirt, pants, dress, socks, or other? ").lower()
if typeOfClothing == "socks" or typeOfClothing == "sock":
	socks()
else:
	#Who does it belong to?
	owner = input("Who is the owner? ").lower()
	#Are you in the doghouse
	dogHouse()
	#execute wardrobe programs
	if owner == "josh":
		JoshWardrobe()
	elif owner == "kate":
		KateWardrobe()
	else:
		OtherPlacement()
