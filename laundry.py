# This is a program to take inputs of type of clothes and output instructions on storing it; folding or hanging; and where to place it.
# I love my partner, but he doesn't know how to sort laundry. This is all in good fun (and his idea!)

####DEFINITIONS 

#hungOrFolded; to be refactored out later to specify instructions for hung and folded  
hungOrFolded = "hung or folded" #or balled for socks!

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


def steam():
	print("This will be a while wrinkled = true loop; but for now; for each wrinked clothes item; steam it. Also, be better.")

def dogHouse():
	areYouIn = input("Are you in the dogHouse? Y/N ").lower()
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
		kateSocks = input("Are there any little and cute socks?")
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
			output(hungOrFolded, typeOfClothing, joshOwned, finalLocation)
			#fold(whiteTee)
		elif typeOfJoshShirt == "coloredtee":
			finalLocation = coloredTeePile
			output(hungOrFolded, typeOfClothing, joshOwned, finalLocation)
			#fold(coloredTee)
		elif typeOfJoshShirt == "dressshirt" or "jersey":
			finalLocation = joshHang
			output(hungOrFolded, typeOfClothing, joshOwned, finalLocation)
			#hang(dressShirt)
		else: 
			finalLocation = joshHang
			print("The type could not be determined. This likely means its a Josh shirt that gets hung. Use discretion, or file an RFE.")
	elif typeOfClothing == "pants":
		typeOfJoshPants = input("What type of pants? dresspants, sportshorts, jeans, or other?").lower()
		if typeOfJoshPants == "dresspants": 
			finalLocation = joshHang
			#hangPants(dresspants)
			output(hungOrFolded, typeOfClothing, joshOwned, finalLocation)
		elif typeOfJoshPants == "sportshorts":
			finalLocation = sportShortsPile
			#fold(sportShorts)
			output(hungOrFolded, typeOfClothing, joshOwned, finalLocation)
		elif typeOfJoshPants == "jeans":
			finalLocation = joshHang
			#fold(jeans)
			output(hungOrFolded, typeOfClothing, joshOwned, finalLocation)
		else: 
			finalLocation = sportShortsPile
			#fold(other)
			print("The type could not be determined. This likely means its a misc josh pant that gets folded. Use discretion, or file an RFE.")
	else: 
		print("The type could not be determined. Use discretion, or file an RFE. ")



#definition for Kate's wardrobe 
def KateWardrobe():
	if typeOfClothing == "shirt":
		typeOfKateShirt = input("What type of shirt? tshirt, tank top, sports tank top, jersey, ?").lower()
		if typeOfKateShirt == "whitetee": 
			finalLocation = whiteTeePile
			output(hungOrFolded, typeOfClothing, joshOwned, finalLocation)
			#fold(whiteTee)
		elif typeOfJoshShirt == "coloredtee":
			finalLocation = coloredTeePile
			output(hungOrFolded, typeOfClothing, joshOwned, finalLocation)
			#fold(coloredTee)
		elif typeOfJoshShirt == "dressshirt":
			finalLocation = joshHang
			output(hungOrFolded, typeOfClothing, joshOwned,  finalLocation)
			#hang(dressShirt)
		else: 
			finalLocation = kateHang
			print("The type could not be determined. This likely means its a kate shirt that gets hung. Use discretion, or file an RFE.")
			# 	if "Shirt"
# 		input "type of shirt?"
# 			shirt
# 			jersey
# 			tankTop
# 				if 
# 			Tee
# 			sportsTankTop
# 				if quality "sportsBra" = true
# 					sportsTankTop = true 
# 					location = athleticPile
# 			dressShirt

# 		input "wrinkly?"
# 			bool wrinkle
	elif typeOfClothing == "pants":
		typeOfJoshPants = input("What type of pants? dresspants, sportshorts, jeans, or other?").lower()
		if typeOfJoshPants == "dresspants": 
			finalLocation = joshHang
			#hangPants(dresspants)
			output(hungOrFolded, typeOfClothing, finalLocation)
		elif typeOfJoshShirt == "sportshorts":
			finalLocation = sportShortsPile
			#fold(sportShorts)
			output(hungOrFolded, typeOfClothing, finalLocation)
		elif typeOfJoshShirt == "jeans":
			finalLocation = joshHang
			#fold(jeans)
			output(hungOrFolded, typeOfClothing, finalLocation)
		else: 
			finalLocation = sportShortsPile
			#fold(other)
			print("The type could not be determined. This likely means its a misc josh pant that gets folded. Use discretion, or file an RFE.")
			# 	if "pants"
# 		input "athletic shorts, shorts or pants?"
# 			if shorts
# 				location = shortPile 
# 			if athleticShorts 
# 				location = athleticPile
# 		input "sweatpants"
# 			location = sweatPantPile
# 		input "does it have a seam down the front?"
# 			if yes 
# 				location = pantsPile
# 			if no 
# 				location = leggingsPile

	elif typeOfClothing == "pants":
		typeOfJoshPants = input("What type of pants? dresspants, sportshorts, jeans, or other?").lower()
		if typeOfJoshPants == "dresspants": 
			finalLocation = joshHang
			#hangPants(dresspants)
			output(hungOrFolded, typeOfClothing, finalLocation)
		elif typeOfJoshShirt == "sportshorts":
			finalLocation = sportShortsPile
			#fold(sportShorts)
			output(hungOrFolded, typeOfClothing, finalLocation)
		elif typeOfJoshShirt == "jeans":
			finalLocation = joshHang
			#fold(jeans)
			output(hungOrFolded, typeOfClothing, finalLocation)
		else: 
			finalLocation = sportShortsPile
			#fold(other)
			print("The type could not be determined. This likely means its a misc josh pant that gets folded. Use discretion, or file an RFE.")		
			# if kate: 
# input "Type of clothing?"


# 	if "dress"
# 		input "wrinkly?"
# 			if wrinkle = true
# 				location = toSteam
# 			else if wrinkle = false
# 				DressPile
# type Clothe struct {
# 	Kind (shirt, leggings, jersey,  tankTop, Tee, Sweater, sportsTankTop, dressShirt, jean, )
# 	metadata (stretchy(bool), graphic(bool), pantSeam(bool), stiff(bool), relaxed(bool), wrinkleToleration(bool), skinTight(bool)
# 	Wrinkle (bool)
# 	Hung (bool)
# 	Location (hangTopRight, hangBottomRight, tankTopPile, whiteTeePile, toSteam, 
# if Tee.graphic, Tee.graphic.beerAdvocate {
# 	selfhang
# }


	else: 
		print("The type could not be determined. Use discretion, or file an RFE. ")	
	


#definition for other placement
def OtherPlacement():
	whatIsIt = input("Is it a towel? (Y/N)").lower()
	if whatIsIt == "yes" or whatIsIt == "y":
		print("Place in " + kitchenTowelPile)
	else: 
		print("You've reached an item without an owner that isn't categorized. Please file an RFE. ")


###########defs for fold, hang, fluff, smoothe, hangpants
# Function steam() {
# 	turn wrinkle = true to wrinkle = false 
# }

# def Fold(location)
# 	fluff()
# 	smoothe()
# 	fold in half
# 	fold in thirds 
# 	place at location 

# def hang(locataion)
# 	fluff()
# 	smoothe()
# 	set on hanger
# 	adjust shoulders to parallel 
# 	place at location 

# def fluff()
# 	wave up and down to reudce wrinkle;

# def smoothe()
# 	smoothe out shirt 

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
