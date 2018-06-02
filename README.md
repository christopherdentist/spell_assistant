# Chris' Spell Assistant
Originally designed during a 24-hour coding competition, this project involves the creation of a MySQL database, populating it with D&amp;D 5th edition spells through Python scripts, and the retrieval of the data using a remote program. As of the end of the competition, the first of these three steps was completed, but not way to retrieve the data was completed.

## Purpose
Managing spells can be messy. In a role-playing game, your goal is to maintain the deception of being someone you're not, while fluidly functioning in a fictional world. For some players, this is easier than others. Barbarians, for example, need only think about when to go berserk, and when to not hit things. In contrast, mages have to constantly be aware of their magical arsenal for any situation, both in the heat of battle and in the quiet confines of a basic puzzle. Waiting for a mage to peruse their spellbook to find (or not find) an acceptable spell, announce their plan to use it, and then again waiting for the dungeon master to lookup the spell on their own to see how it would apply to the situation... it's an unacceptably long and tedious process. This program aims to streamline the process significantly.

## How
A MySQL database is set up to contain a number of useful tables. Through manual input of spell data, the database is updated to contain a variety of useful information. From spell name and level to damage type and material cost, the database allows for easy selection of a wide variety of components.

![Database design](https://github.com/christopherdentist/spell_assistant/blob/master/layout.png)

Through MySQL connectors, data can be easily entered and retrieved from any common coding language, allowing for a wide variety of front-end applications.

## Where Next
The front-end side! With the back-end (and data entry) largely completed, future progress will be diverted primarily towards a tool (or multiple tools) allowing for accessing the data. Look forward to it!
