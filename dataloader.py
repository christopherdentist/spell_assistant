import pymysql.cursors
import spellslist as sp

class dataloader:
	
	def __init__(self):
		print("Connecting to server... ", end="")
		self.connection = pymysql.connect(
			user="root",
			password="",
			host='127.0.0.1',
			db='sasp',
			cursorclass=pymysql.cursors.DictCursor)
		print("Done.")
		try:
			with self.connection.cursor() as cursor:
				print("Beginning data input", end="")
				spells = sp.SpellList()
				for spell in spells.spellsList:
					
					# Populate the "school" table.
					tschool = spell.get("school")
					cursor.execute("""insert ignore into school (school.name) values (%s)""", tschool)
					self.connection.commit()
					cursor.execute("""select idschool from school where school.name=%s""", tschool)
					#self.connection.commit()
					schoolID = cursor.fetchone()["idschool"]

					# Populate the "spell" table.
					tspell = [spell.get("name"), spell.get("level"), spell.get("v"), spell.get("s"), spell.get("m"), spell.get("description"), spell.get("range"), spell.get("rangeExtra"), schoolID]
					tspell = self.parseForInvalids(tspell)
					cursor.execute("""insert ignore into spell (spell.name, spell.level, spell.verbal, spell.somatic, spell.material, spell.description, spell.range, spell.rangeExtra, spell.school) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", tuple(tspell))
					self.connection.commit()
					cursor.execute("""select max(idspell) as sid from spell""")
					#self.connection.commit()
					sid = cursor.fetchone()["sid"]
					if sid is None:
						continue
					
					# Populate the "material" table.
					mat = spell.get("materials")
					if mat is not None:
						tmaterial = self.parseForInvalids([sid, mat.get("description"), mat.get("cost"), mat.get("consumed")])
						cursor.execute("""insert ignore into material (material.idmaterial, material.description, material.cost, material.consumed) values (%s, %s, %s, %s)""", tmaterial)
						self.connection.commit()
					
					# Populate the "cost" table.
					cost = spell.get("cost")
					if cost is not None:
						tcost = self.parseForInvalids([sid, cost.get("actionsMajor"), cost.get("actionsBonus"), cost.get("reactions"), cost.get("extraText"), cost.get("minutes"), cost.get("ritual")])
						cursor.execute("""insert ignore into cost values (%s, %s, %s, %s, %s, %s, %s)""", tcost)
						self.connection.commit()
					
					# Populate the "duration" table.
					dur = spell.get("duration")
					if dur is not None:
						tduration = self.parseForInvalids([sid, dur.get("minutes"), dur.get("rounds"), dur.get("concentration"), dur.get("extraText")])
						cursor.execute("""insert ignore into duration values (%s, %s, %s, %s, %s)""", tduration)
						self.connection.commit()
					
					# Populate the "type" table.
					damageList = spell.get("damage")
					if damageList is not None:
						for dam in damageList:
							dams = dam.get("damageType")
							if dams is None:
								dams = ["other"]
							ttype = self.parseForInvalids(dams)
							types = []
							for type in ttype:
								cursor.execute("""insert ignore into type (type.name) values (%s)""", type)
								self.connection.commit()
								cursor.execute("""select idtype from type where type.name=%s""", type)
								types.append(cursor.fetchone()["idtype"])
							
							# Populate the "damage" table.
							tdamage = self.parseForInvalids([sid, dam.get("instantaneous"), dam.get("dieType"), dam.get("dieCount")])
							cursor.execute("""insert ignore into damage (damage.spellreference, damage.instantaneous, damage.dieType, damage.dieCount) values (%s, %s, %s, %s)""", tdamage)
							self.connection.commit()
							cursor.execute("""select max(iddamage) as did from damage""")
							did = cursor.fetchone()["did"]
						
							# Populate the "damagetotype" table.
							for t in types:
								cursor.execute("""insert ignore into damagetotype (iddamagetotype, idtypetodamage) values (%s, %s)""", (did, t))
					
					print(".", end="")
				print("Done.")

		finally:
			self.connection.close()
	
	def parseForInvalids(self, array):
		tspell = array[:]
		for i in range(len(tspell)):
			if type(tspell[i]) is str:
				for index,char in enumerate(tspell[i]):
					if char=='’':
						tspell[i] = tspell[i][:index-1] + "'" + tspell[i][index + 1:]
		return tspell

dataloader()
