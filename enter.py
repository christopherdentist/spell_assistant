userinput = "y"
while userinput is "y":

	print("✨ Entering a new spell ✨")
	newspell = {}
	userinput = ""

	while userinput is "":
		userinput = input("Spell name: ")
	newspell["name"] = userinput

	userinput = ""
	while userinput is "":
		userinput = input("Spell description: ")
	newspell["description"] = userinput

	userinput = ""
	while userinput is "":
		userinput = input("Spell level: ")
	newspell["level"] = userinput

	userinput = ""
	while userinput is "":
		userinput = input("Spell school: ")
	newspell["school"] = userinput

	userinput = input("Spell range (ft, 0=touch, -1=self): ")
	if userinput is not "":
		newspell["range"] = userinput

	userinput = input("vsm? ")
	if "v" in userinput:
		newspell["v"] = 1
	if "s" in userinput:
		newspell["s"] = 1
	if "m" in userinput:
		newspell["m"] = 1
		newspell["materials"] = {}
		
		userinput = input("\tMaterial description: ")
		if userinput is not "":
			newspell["materials"]["description"] = userinput
		
		userinput = input("\tMaterial cost (in copper): ")
		if userinput is not "":
			newspell["materials"]["cost"] = userinput
		
		userinput = input("\tMaterial consumed? ")
		if userinput is not "":
			newspell["materials"]["consumed"] = userinput

	print("Cost: ")
	userinput = input("\tAction: ")
	if userinput is not "":
		newspell["cost"] = {}
		newspell["cost"]["actionsMajor"] = userinput

	userinput = input("\tBonus action: ")
	if userinput is not "":
		if not "cost" in newspell:
			newspell["cost"] = {}
		newspell["cost"]["actionsBonus"] = userinput

	userinput = input("\tReactions: ")
	if userinput is not "":
		if not "cost" in newspell:
			newspell["cost"] = {}
		newspell["cost"]["reactions"] = userinput

	userinput = input("\tMinutes: ")
	if userinput is not "":
		if not "cost" in newspell:
			newspell["cost"] = {}
		newspell["cost"]["reactions"] = userinput

	userinput = input("\tRitual? ")
	if userinput is not "":
		if not "cost" in newspell:
			newspell["cost"] = {}
		newspell["cost"]["reactions"] = userinput

	print("Duration")
	userinput = input("\tDuration (minutes): ")
	if userinput is not "":
		newspell["duration"] = {}
		newspell["duration"]["minutes"] = userinput

	userinput = input("\tDuration (rounds): ")
	if userinput is not "":
		if not "duration" in newspell:
			newspell["duration"] = {}
		newspell["duration"]["reactions"] = userinput

	userinput = input("\tConcentration? ")
	if userinput is not "":
		if not "duration" in newspell:
			newspell["duration"] = {}
		newspell["duration"]["concentration"] = userinput

	userinput = input("Damage? y/n ")
	if "y" in userinput:
		newspell["damage"] = []
		
		newdamage = {}
		userinput = "y"
		while "y" in userinput:
			
			newdamage["damageType"] = []
			userinput = input("\tDamage type: ")
			while userinput is not "":
				newdamage["damageType"].append(userinput)
				userinput = input("\tDamage type: ")
			
			userinput = input("\tInstantaneous? ")
			if userinput is not "":
				newdamage["instantaneous"] = userinput
			
			userinput = input("\tDie type: ")
			if userinput is not "":
				newdamage["dieType"] = userinput
			
			userinput = input("\tDie count: ")
			if userinput is not "":
				newdamage["dieCount"] = userinput
			
			newspell["damage"].append(newdamage)
			newdamage = {}
			
			userinput = input("Another damage? y/n ")

	print(newspell)
	
	userinput = input("✨ Another spell? y/n ")