class SpellList(object):
	
	def __init__(self):
		self.spellsList = [
			{
				"name": "Alarm",
				"description": """You set an alarm against unwanted intrusion. Choose a door, a window, or an area within range that is no larger than a 20-foot cube. Until the spell ends, an alarm alerts you whenever a Tiny or larger creature touches or enters the warded area. When you cast the spell, you can designate creatures that won’t set off the alarm. You also choose whether the alarm is mental or audible.
A mental alarm alerts you with a ping in your mind if you are within 1 mile of the warded area. This ping awakens you if you are sleeping.
An audible alarm produces the sound of a hand bell for 10 seconds within 60 feet.""",
				"level": 1,
				"range": 30,
				"school": "abjuration",
				"v": 1,
				"s": 1,
				"m": 1,
				"materials": {
					"description": "a tiny bell and a piece of fine silver wire"
				},
				"cost": {
					"minutes": 1,
					"ritual": 1
				},
				"duration": {
					"minutes": 480
				}
			},
			{
				"name": "Destructive Wave",
				"description": """You strike the ground, creating a burst of divine energy that ripples outward from you. Each creature you choose within 30 feet of you must succeed on a Constitution saving throw or take 5d6 thunder damage, as well as 5d6  radiant or necrotic damage (your choice), and be knocked prone. A creature that succeeds on its saving throw takes half as much damage and isn’t knocked prone.""",
				"level": 5,
				"range": -1,
				"rangeExtra": "30-foot radius",
				"school": "evocation",
				"v": 1,
				"cost": {
					"action": 1
				},
				"duration": {
					"minutes": 0
				},
				"damage": [
					{
						"damageType": ["thunder"],
						"instantaneous": 1,
						"dieType": 6,
						"dieCount": 5
					},
					{
						"damageType": ["radiant", "necrotic"],
						"instantaneous": 1,
						"dieType": 6,
						"dieCount": 5
					}
				]
			},
			{
				"name": "Animal Friendship",
				"description": """This spell lets you convince a beast that you mean it no harm. Choose a beast that you can see within range. It must see and hear you. If the beast’s Intelligence is 4 or higher, the spell fails. Otherwise, the beast must succeed on a Wisdom saving throw or be charmed by you for the spell’s duration. If you or one of your companions harms the target, the spells ends.
At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, you can affect one additional beast for each slot level above 1st.""",
				"level": 1,
				"range": 30,
				"school": "enchantment",
				"v": 1,
				"s": 1,
				"m": 1,
				"materials": {
					"description": "a morsel of food"
				},
				"cost": {
					"action": 1
				},
				"duration": {
					"minutes": 1440
				}
			},
			{
				"name": "Vicious Mockery",
				"description": """You unleash a string of insults laced with subtle enchantments at a creature you can see within range. If the target can hear you (though it need not understand you), it must succeed on a Wisdom saving throw or take 1d4 psychic damage and have disadvantage on the next attack roll it makes before the end of its next turn.
This spell’s damage increases by 1d4 when you reach 5th level (2d4), 11th level (3d4), and 17th level (4d4).""",
				"level": 0,
				"range": 60,
				"school": "enchantment",
				"v": 1,
				"cost": {
					"action": 1
				},
				"damage": [
					{
						"damageType": ["psychic"],
						"instantaneous": 1,
						"dieType": 4,
						"dieCount": 1
					}
				]
			},
			{
				"name": "Stoneskin",
				"description": """This spell turns the flesh of a willing creature you touch as hard as stone. Until the spell ends, the target has resistance to nonmagical bludgeoning, piercing, and slashing damage""",
				"level": 4,
				"range": 0,
				"school": "abjuration",
				"v": 1,
				"s": 1,
				"m": 1,
				"materials": {
					"description": "diamond dust",
					"cost": 10000,
					"consumed": 1
				},
				"cost": {
					"actionsMajor": 1
				},
				"duration": {
					"minutes": 60,
					"concentration": 1
				}
			},
			{
				"name": "Healing Word",
				"description": """A creature of your choice that you can see within range regains hit points equal to 1d4 + your spellcasting ability modifier. This spell has no effect on undead or constructs.
At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, the healing increases by 1d4 for each slot level above 1st.""",
				"level": 1,
				"range": 60,
				"school": "evocation",
				"v": 1,
				"cost": {
					"actionsBonus": 1
				},
				"damage": [
					{
						"instantaneous": 1,
						"dieType": 4,
						"dieCount": -1
					}
				]
			},
			{
				"name": "Hellish Rebuke",
				"description": """You point your finger, and the creature that damaged you is momentarily surrounded by hellish flames. The creature must make a Dexterity saving throw. It takes 2d10 fire damage on a failed save, or half as much damage on a successful one.
At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d10 for each slot level above 1st.""",
				"level": 1,
				"range": 60,
				"school": "evocation",
				"v": 1,
				"s": 1,
				"cost": {
					"reactions": 1,
					"extraText": "1 reaction, which you take in response to being damaged by a creature within 60 feet of you that you can see"
				},
				"damage": [
					{
						"damageType": ["fire"],
						"instantaneous": 1,
						"dieType": 10,
						"dieCount": 2
					}
				]
			},
			{
				"name": "Guidance",
				"description": """You touch one willing creature. Once before the spell ends, the target can roll a d4 and add the number rolled to one ability check of its choice. It can roll the die before or after making the ability check. The spell then ends.""",
				"level": 0,
				"range": 0,
				"school": "divination",
				"v": 1,
				"s": 1,
				"cost": {
					"actionsMajor": 1
				},
				"duration": {
					"minutes": 1,
					"concentration": 1
				}
			},
			{
				"name": "Passwall",
				"description": """A passage appears at a point of your choice that you can see on a wooden, plaster, or stone surface (such as a wall, a ceiling, or a floor) within range, and lasts for the duration. You choose the opening’s dimensions: up to 5 feet wide, 8 feet tall, and 20 feet deep. The passage creates no instability in a structure surrounding it. When the opening disappears, any creatures or objects still in the passage created by the spell are safely ejected to an unoccupied space nearest to the surface on which you cast the spell.""",
				"level": 5,
				"range": 30,
				"school": "transmutation",
				"v": 1,
				"s": 1,
				"m": 1,
				"materials": {
					"description": "a pinch of sesame seeds"
				},
				"cost": {
					"actionsMajor": 1
				},
				"duration": {
					"minutes": 60
				}
			},
			{
				"name": "Programmed Illusion",
				"description": """You create an illusion of an object, a creature, or some other visible phenomenon within range that activates when a specific condition occurs. The illusion is imperceptible until then. It must be no larger than a 30-foot cube, and you decide when you cast the spell how the illusion behaves and what sounds it makes. This scripted performance can last up to 5 minutes.
When the condition you specify occurs, the illusion springs into existence and performs in the manner you described. Once the illusion finishes performing, it disappears and remains dormant for 10 minutes. After this time, the illusion can be activated again.
The triggering condition can be as general or as detailed as you like, though it must be based on visual or audible conditions that occur within 30 feet of the area. For example, you could create an illusion of yourself to appear and warn off others who attempt to open a trapped door, or you could set the illusion to trigger only when a creature says the correct word or phrase.
Physical interaction with the image reveals it to be an illusion, because things can pass through it. A creature that uses its action to examine the image can determine that it is an illusion with a successful Intelligence (Investigation) check against your spell save DC. If a creature discerns the illusion for what it is, the creature can see through the image, and any noise it makes sounds hollow to the creature.""",
				"level": 6,
				"range": 120,
				"school": "illusion",
				"v": 1,
				"s": 1,
				"m": 1,
				"materials": {
					"description": "a bit of fleece and jade dust worth at least 25 gp",
					"cost": 2500
				},
				"cost": {
					"actionsMajor": 1
				},
				"duration": {
					"minutes": -1
				}
			},
			{
				"name": "Project Image",
				"description": """You create an illusory copy of yourself that lasts for the duration. The copy can appear at any location within range that you have seen before, regardless of intervening obstacles. The illusion looks and sounds like you but is intangible. If the illusion takes any damage, it disappears, and the spell ends.
You can use your action to move this illusion up to twice your speed, and make it gesture, speak, and behave in whatever way you choose. It mimics your mannerisms perfectly.
You can see through its eyes and hear through its ears as if you were in its space. On your turn as a bonus action, you can switch from using its senses to using your own, or back again. While you are using its senses, you are blinded and deafened in regard to your own surroundings.
Physical interaction with the image reveals it to be an illusion, because things can pass through it. A creature that uses its action to examine the image can determine that it is an illusion with a successful Intelligence (Investigation) check against your spell save DC. If a creature discerns the illusion for what it is, the creature can see through the image, and any noise it makes sounds hollow to the creature.""",
				"level": 7,
				"range": 2640000,
				"school": "illusion",
				"v": 1,
				"s": 1,
				"m": 1,
				"materials": {
					"description": "a small replica of you made from materials worth at least 5 gp",
					"cost": 500
				},
				"cost": {
					"actionsMajor": 1
				},
				"duration": {
					"minutes": 1440,
					"concentration": 1
				}
			},
			{
				"name": "Ray of Enfeeblement",
				"description": """A black beam of enervating energy springs from your finger toward a creature within range. Make a ranged spell attack against the target. On a hit, the target deals only half damage with weapon attacks that use Strength until the spell ends.
At the end of each of the target’s turns, it can make a Constitution saving throw against the spell. On a success, the spell ends.""",
				"level": 2,
				"range": 60,
				"school": "necromancy",
				"v": 1,
				"s": 1,
				"cost": {
					"actionsMajor": 1
				},
				"duration": {
					"minutes": 1,
					"concentration": 1
				}
			},
			{
				"name": "Create Food and Water",
				"description": """You create 45 pounds of food and 30 gallons of water on the ground or in containers within range, enough to sustain up to fifteen humanoids or five steeds for 24 hours. The food is bland but nourishing, and spoils if uneaten after 24 hours. The water is clean and
doesn’t go bad.""",
				"level": 3,
				"range": 30,
				"school": "conjuration",
				"v": 1,
				"s": 1,
				"cost": {
					"actionsMajor": 1
				}
			},
			{
				"name": "Conjure Volley",
				"description": """You fire a piece of nonmagical ammunition from a ranged weapon or throw a nonmagical weapon into the air and choose a point within range. Hundreds of duplicates of the ammunition or weapon fall in a volley from above and then disappear. Each creature in a 40-foot-radius. 20-foot-high cylinder centered on that point must make a Dexterity saving throw. A creature takes 8d8 damage on a failed save, or half as much damage on a successful one. The damage type is the same as that of the ammunition or weapon.""",
				"level": 5,
				"range": 150,
				"school": "conjuration",
				"v": 1,
				"s": 1,
				"m": 1,
				"materials": {
					"description": "one piece of ammunition or one thrown weapon"
				},
				"cost": {
					"actionsMajor": 1
				},
				"damage": [
					{
						"instantaneous": 1,
						"dieType": 8,
						"dieCount": 8
					}
				]
			},
			{
				"name": "Chill Touch",
				"description": """You create a ghostly, skeletal hand in the space of a creature within range. Make a ranged spell attack against the creature to assail it with the chill of the grave. On a hit, the target takes 1d8 necrotic damage, and it can’t regain hit points until the start of your next turn. Until then, the hand clings to the target.
If you hit an undead target, it also has disadvantage on attack rolls against you until the end of your next turn.
This spell’s damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8).""",
				"level": 0,
				"range": 120,
				"school": "necromancy",
				"v": 1,
				"s": 1,
				"cost": {
					"actionsMajor": 1
				},
				"duration": {
					"rounds": 1
				},
				"damage": [
					{
						"damageType": ["necrotic"],
						"instantaneous": 1,
						"dieType": 8,
						"dieCount": 1
					}
				]
			},
			{
				"name": "Chromatic Orb",
				"description": """You hurl a 4-inch-diameter sphere of energy at a creature that you can see within range. You choose acid, cold, fire, lightning, poison, or thunder for the type of orb you create, and then make a ranged spell attack against the target. If the attack hits, the creature takes 3d8 damage of the type you chose.
At Higher Levels. When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d8 for each slot level above 1st.""",
				"level": 1,
				"range": 90,
				"school": "evocation",
				"v": 1,
				"s": 1,
				"m": 1,
				"materials": {
					"description": "a diamond worth at least 50 gp"
				},
				"cost": {
					"actionsMajor": 1
				},
				"damage": [
					{
						"damageType": ["acid", "cold", "fire", "lightning", "poison", "thunder"],
						"instantaneous": 1,
						"dieType": 8,
						"dieCount": 3
					}
				]
			},
			{
				"name": "Evard's Black Tentacles",
				"description": """Squirming, ebony tentacles fill a 20-foot square on ground that you can see within range. For the duration, these tentacles turn the ground in the area into difficult terrain.
When a creature enters the affected area for the first time on a turn or starts its turn there, the creature must succeed on a Dexterity saving throw or take 3d6
bludgeoning damage and be restrained by the tentacles until the spell ends. A creature that starts its turn in the area and is already restrained by the tentacles takes 3d6 bludgeoning damage.
A creature restrained by the tentacles can use its action to make a Strength or Dexterity check (its choice) against your spell save DC. On a success, it frees itself.""",
				"level": 4,
				"range": 90,
				"school": "conjuration",
				"v": 1,
				"s": 1,
				"m": 1,
				"materials": {
					"description": "a piece of tentacle from a giant octopus or a giant squid"
				},
				"cost": {
					"actionsMajor": 1
				},
				"duration": {
					"minutes": 1,
					"concentration": 1
				},
				"damage": [
					{
						"damageType": ["bludgeoning"],
						"instantaneous": 1,
						"dieType": 6,
						"dieCount": 3
					}
				]
			},
			{
				"name": "Spiritual Weapon",
				"description": """You create a floating, spectral weapon within range that lasts for the duration or until you cast this spell again. When you cast the spell, you can make a melee spell attack against a creature within 5 feet of the weapon. On a hit, the target takes force damage equal to 1d8 + your spellcasting ability modifier.
As a bonus action on your turn, you can move the weapon up to 20 feet and repeat the attack against a creature within 5 feet of it.
The weapon can take whatever form you choose. Clerics of deities who are associated with a particular weapon (as St. Cuthbert is known for his mace and Thor for his hammer) make this spell’s effect resemble that weapon.
At Higher Levels. When you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d8 for every two slot levels above the 2nd.""",
				"level": 2,
				"range": 60,
				"school": "evocation",
				"v": 1,
				"s": 1,
				"cost": {
					"actionsBonus": 1
				},
				"duration": {
					"minutes": 1
				},
				"damage": [
					{
						"damageType": ["force"],
						"instantaneous": 1,
						"dieType": 8,
						"dieCount": 1
					}
				]
			},
			{
				"name": "Thorn Whip",
				"description": """You create a long, vine-like whip covered in thorns that lashes out at your command toward a creature in range. Make a melee spell attack against the target. If the attack hits, the creature takes 1d6 piercing damage, and if the creature is Large or smaller, you pull the creature up to 10 feet closer to you.
This spell’s damage increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and 17th level (4d6).""",
				"level": 0,
				"range": 30,
				"school": "transmutation",
				"v": 1,
				"s": 1,
				"m": 1,
				"materials": {
					"description": "the stem of a plant with thorns"
				},
				"cost": {
					"actionsMajor": 1
				},
				"damage": [
					{
						"damageType": ["piercing"],
						"instantaneous": 1,
						"dieType": 6,
						"dieCount": 1
					}
				]
			},
			{
				"name": "Cloud of Daggers",
				"description": """You fill the air with spinning daggers in a cube 5 feet on each side, centered on a point you choose within range. A creature takes 4d4 slashing damage when it enters the spell’s area for the first time on a turn or starts its turn there.
At Higher Levels. When you cast this spell using a spell slot of 3rd level or higher, the damage increases by 2d4 for each slot level above 2nd.""",
				"level": 2,
				"range": 60,
				"school": "conjuration",
				"v": 1,
				"s": 1,
				"m": 1,
				"materials": {
					"description": "a sliver of glass"
				},
				"cost": {
					"actionsMajor": 1
				},
				"duration": {
					"minutes": 1,
					"concentration": 1
				},
				"damage": [
					{
						"damageType": ["slashing"],
						"instantaneous": 1,
						"dieType": 4,
						"dieCount": 4
					}
				]
			},
			{
				"name": "Beast Sense",
				"description": """You touch a willing beast. For the duration of the spell, you can use your action to see through the beast’s eyes and hear what it hears, and continue to do so until you use your action to return to your normal senses. While perceiving through the beast’s senses, you gain the benefits of any special senses possessed by that creature, though you are blinded and deafened to your own surroundings.""",
				"level": 2,
				"range": 0,
				"school": "divination",
				"s": 1,
				"cost": {
					"actionsMajor": 1,
					"ritual": 1
				},
				"duration": {
					"minutes": 60,
					"concentration": 1
				}
			},
			{
				"name": "Counterspell",
				"description": """You attempt to interrupt a creature in the process of casting a spell. If the creature is casting a spell of 3rd level or lower, its spell fails and has no effect. If it is casting a spell of 4th level or higher, make an ability check using your spellcasting ability. The DC equals 10 + the spell’s level. On a success, the creature’s spell fails and has no effect.
At Higher Levels. When you cast this spell using a spell slot of 4th level or higher, the interrupted spell has no effect if its level is less than or equal to the level of the spell slot you used.""",
				"level": 3,
				"range": 60,
				"school": "abjuration",
				"s": 1,
				"cost": {
					"reactions": 1,
					"extraText": "1 reaction, which you take when you see a creature within 60 feet of you casting a spell"
				}
			},
			{
				"name": "Friends",
				"description": """For the duration, you have advantage on all Charisma checks directed at one creature of your choice that isn’t hostile toward you. When the spell ends, the creature realizes that you used magic to influence its mood and becomes hostile toward you. A creature prone to violence might attack you. Another creature might seek retribution in other ways (at the DM’s discretion), depending on the nature of your interaction with it.""",
				"level": 0,
				"range": -1,
				"school": "enchantment",
				"s": 1,
				"m": 1,
				"materials": {
					"description": "a small amount of makeup applied to the face as this spell is cast"
				},
				"cost": {
					"actionsMajor": 1
				},
				"duration": {
					"minutes": 1,
					"concentration": 1
				}
			},
			{
				"name": "",
				"description": """""",
				"level": 0,
				"range": 0,
				"school": "",
				"v": 1,
				"s": 1,
				"m": 1,
				"materials": {
					"description": "",
					"cost": 0,
					"consumed": 1
				},
				"cost": {
					"actionsMajor": 0,
					"actionsBonus": 0,
					"reactions": 0,
					"minutes": 0,
					"ritual": 1
				},
				"duration": {
					"minutes": 0,
					"rounds": 0,
					"concentration": 1
				},
				"damage": [
					{
						"damageType": [""],
						"instantaneous": 1,
						"dieType": 0,
						"dieCount": 0
					}
				]
			},
			{
				"name": "",
				"description": """""",
				"level": 0,
				"range": 0,
				"school": "",
				"v": 1,
				"s": 1,
				"m": 1,
				"materials": {
					"description": "",
					"cost": 0,
					"consumed": 1
				},
				"cost": {
					"actionsMajor": 0,
					"actionsBonus": 0,
					"reactions": 0,
					"minutes": 0,
					"ritual": 1
				},
				"duration": {
					"minutes": 0,
					"rounds": 0,
					"concentration": 1
				},
				"damage": [
					{
						"damageType": [""],
						"instantaneous": 1,
						"dieType": 0,
						"dieCount": 0
					}
				]
			}
		]