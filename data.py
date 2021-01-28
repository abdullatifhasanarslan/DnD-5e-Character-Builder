deneme = "('deneme','deneme')"

#shows possible selections
selections = """
	("Tiefling", "Race"),
 	("Dragonborn", "Race"),
	("Dwarf", "Race"),
	("Elf", "Race"),
	("Gnome", "Race"),
	("Half-Elf", "Race"),
	("Half-Orc", "Race"),
	("Halfling", "Race"),
	("Human", "Race"),
	("Githyanki", "Race"),

	("Barbarian 1","Level"),
	("Bard 1","Level"),
	("Cleric 1","Level"),
	("Druid 1","Level"),
	("Fighter 1","Level"),
	("Monk 1","Level"),
	("Paladin 1","Level"),
	("Ranger 1","Level"),
	("Rogue 1","Level"),
	("Rogue 2","Level"),
	("Rogue 3","Level"),
	("Rogue 4","Level"),
	("Rogue 5","Level"),
	("Rogue 6","Level"),
	("Rogue 7","Level"),
	("Rogue 8","Level"),
	("Revived","Subclass"),
	("Assasin","Subclass"),
	("Sorcerer 1","Level"),
	("Warlock 1","Level"),
	("Wizard 1","Level"),

	("Animal Handler","Feat"),
	("Alert","Feat"),
	("Athlete","Feat"),
	("Charger","Feat"),
	("Crossbow Expert","Feat"),
	("Defensive Duelist","Feat"),
	("Dual Wielder","Feat"),
	("Shield Training","Feat"),
	("Mobile","Feat")
	
"""

#shows class and subclass relations
classsubclass="""
	("Barbarian","Barbarian 1"),
	("Bard","Bard 1"),
	("Cleric","Cleric 1"),
	("Druid","Druid 1"),
	("Fighter","Fighter 1"),
	("Monk","Monk 1"),
	("Paladin","Paladin 1"),
	("Ranger","Ranger 1"),
	("Rogue","Rogue 1"),
	("Rogue","Rogue 2"),
	("Rogue","Rogue 3"),
	("Rogue","Rogue 4"),
	("Rogue","Rogue 5"),
	("Rogue","Rogue 6"),
	("Rogue","Rogue 7"),
	("Rogue","Rogue 8"),
	("Rogue","Revived"),
	("Rogue","Assasin"),
	("Sorcerer","Sorcerer 1"),
	("Warlock","Warlock 1"),
	("Wizard","Wizard 1")
"""

#shows feature names and explanatşon
features = """
	("Attack Action","The most Common action to take in combat is the Attack action, whether you are swinging a sword, firing an arrow from a bow, or brawling with your fists.
With this action, you make one melee or ranged Attack. See the “Making an Attack” section for the rules that govern attacks.

Certain features, such as the Extra Attack feature of the Fighter, allow you to make more than one Attack with this action."),

	("Two-Weapon Fighting","When you take the Attack action and Attack with a light melee weapon that you’re holding in one hand, you can use a Bonus Action to Attack with a different light melee weapon that you’re holding in the other hand. You don’t add your ability modifier to the damage of the bonus Attack, unless that modifier is negative.

If either weapon has the Thrown property, you can throw the weapon, instead of making a melee Attack with it."),

	("Opportunity Attack","In a fight, everyone is constantly watching for a chance to strike an enemy who is fleeing or passing by. Such a strike is called an opportunity Attack.
You can make an opportunity Attack when a Hostile creature that you can see moves out of your reach. To make the opportunity Attack, you use your Reaction to make one melee Attack against the provoking creature. The Attack occurs right before the creature leaves your reach.

You can avoid provoking an opportunity Attack by taking the Disengage action. You also don’t provoke an opportunity Attack when you Teleport or when someone or something moves you without using your Movement, action, or Reaction. For example, you don’t provoke an opportunity Attack if an explosion hurls you out of a foe’s reach or if gravity causes you to fall past an enemy."),
	("Animal Handler","Source: Unearthed Arcana 38 - Feats for Skills

You master the techniques needed to train and handle animals. You gain the following benefits:

    Increase your Wisdom score by 1, to a maximum of 20.

    You gain proficiency in the Animal Handling skill. If you are already proficient in the skill, you add double your proficiency bonus to checks you make with it.

    You can use a bonus action on your turn to command one friendly beast within 60 feet of you that can hear you and that isn’t currently following the command of someone else. You decide now what action the beast will take and where it will move during its next turn, or you issue a general command that lasts for 1 minute, such as to guard a particular area."),
	("Alert","Source: Player's Handbook

Always on the lookout for danger, you gain the following benefits:

    You can’t be surprised while you are conscious.

    You gain a +5 bonus to initiative.

    Other creatures don’t gain advantage on attack rolls against you as a result of being hidden from you."),
	("Athlete","Source: Player's Handbook

You have undergone extensive physical training to gain the following benefits:

    Increase your Strength or Dexterity score by 1, to a maximum of 20.

    When you are prone, standing up uses only 5 feet of your movement.

    Climbing doesn’t cost you extra movement.

    You can make a running long jump or a running high jump after moving only 5 feet on foot, rather than 10 feet."),
	("Charger","Source: Player's Handbook

When you use your action to Dash, you can use a bonus action to make one melee weapon attack or to shove a creature. If you move at least 10 feet in a straight line immediately before taking this bonus action, you either gain a +5 bonus to the attack’s damage roll (if you chose to make a melee attack and hit) or push the target up to 10 feet away from you (if you chose to shove and you succeed)."),
	("Crossbow Expert","Source: Player's Handbook

Thanks to extensive practice with the crossbow, you gain the following benefits:

    You ignore the loading quality of crossbows with which you are proficient.

    Being within 5 feet of a hostile creature doesn’t impose disadvantage on your ranged attack rolls.

    When you use the Attack action and attack with a one handed weapon, you can use a bonus action to attack with a hand crossbow you are holding."),
	("Defensive Duelist","Source: Player's Handbook

Prerequisite: Dexterity 13 or higher

When you are wielding a finesse weapon with which you are proficient and another creature hits you with a melee attack, you can use your reaction to add your proficiency bonus to your AC for that attack, potentially causing the attack to miss you."),
	("Dual Wielder","Source: Player's Handbook

You master fighting with two weapons, gaining the following benefits:

    You gain a +1 bonus to AC while you are wielding a separate melee weapon in each hand.

    You can use two-weapon fighting even when the one handed melee weapons you are wielding aren’t light.

    You can draw or stow two one-handed weapons when you would normally be able to draw or stow only one."),
	("Shield Training","Source: Unearthed Arcana 73 - Feats

You’ve trained in the effective use of shields. You gain the following benefits:

    Increase your Strength, Dexterity, or Constitution score by 1, to a maximum of 20.

    You gain proficiency with shields.

    In combat, you can don or doff a shield as the free object interaction on your turn.

    If you have the Spellcasting or Pact Magic feature, you can use a shield as a spellcasting focus."),
	("Mobile","Source: Player's Handbook

You are exceptionally speedy and agile. You gain the following benefits:

    Your speed increases by 10 feet.

    When you use the Dash action, difficult terrain doesn't cost you extra movement on that turn.

    When you make a melee attack against a creature, you don't provoke opportunity attacks from that creature for the rest of the turn, whether you hit or not."),
	
	("Expertise","choose two of your skill proficiencies, or one of your skill proficiencies and your proficiency with thieves' tools. Your proficiency bonus is doubled for any ability check you make that uses either of the chosen proficiencies."),

	("Sneak Attack","Beginning at 1st level, you know how to strike subtly and exploit a foe's distraction. Once per turn, you can deal an extra 1d6 damage to one creature you hit with an attack if you have advantage on the attack roll. The attack must use a finesse or a ranged weapon.

You don't need advantage on the attack roll if another enemy of the target is within 5 feet of it, that enemy isn't incapacitated, and you don't have disadvantage on the attack roll.

The amount of the extra damage increases as you gain levels in this class, as shown in the Sneak Attack column of the Rogue table."),

	("Thieves' Cant","During your rogue training you learned thieves' cant, a secret mix of dialect, jargon, and code that allows you to hide messages in seemingly normal conversation. Only another creature that knows thieves' cant understands such messages. It takes four times longer to convey such a message than it does to speak the same idea plainly,

In addition, you understand a set of secret signs and symbols used to convey short, simple messages, such as whether an area is dangerous or the territory of a thieves' guild, whether loot is nearby, or whether the people in an area are easy marks or will provide a safe house for thieves on the run."),
	("Cunning Action","Bonus Action Dash, Disengage, Hide"),
	("Tokens of Past Lives","Starting at 3rd level, you remember talents you had in your previous life. When you finish a long rest, you gain one skill or tool proficiency of your choice. You can replace this proficiency with another when you finish a long rest."),
	("Revived Nature","When you choose this archetype at 3rd level, your newfound connection to death gives you the following benefits:

    You have advantage on saving throws against disease and being poisoned, and you have resistance to poison damage.

    You don't need to eat, drink, or breathe

    You don't need to sleep. When you take a long rest, you must spend at least four hours in an inactive, motionless state, rather than sleeping. In this state, you remain semiconscious, and you can hear as normal."),

	("Bolts from the Grave","Starting at 3rd level, you have learned to unleash bolts of necrotic energy from within your revived body. Immediately after you use your Cunning Action, you can make a ranged spell attack against a creature within 30 feet of you, provided you haven't used your Sneak Attack this turn. You are proficient with it, and you add your Dexterity modifier to its attack and damage rolls. A creature hit by this attack takes necrotic damage equal to your Sneak Attack. This uses your Sneak Attack for the turn."),

	("Uncanny Dodge","Starting at 5th level, when an attacker that you can see hits you with an attack, you can use your reaction to halve the attack's damage against you."),
	("Evasion","Beginning at 7th level, you can nimbly dodge out of the way of certain area effects, such as a red dragon's fiery breath or an Ice Storm spell. When you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw, and only half damage if you fail."),

	("Rage","Resistance to damage"),
	("Bardic Inspiration","Vicious Mockery"),
	("Divine Domain","May Allah help you"),
	("Druidic","Tree Hugger"),
	("Second Wind","More dayak"),
	("Martial Arts","Kung-fu"),
	("Fighting Style","Heyoo"),
	("Sorcerous Origin","Wild Magic"),
	("Otherworldly Patron","I sold my soul to devil"),
	("Spellbook","The pursuit of knowledge"),


	
	("Dwarf","Kingdoms rich in ancient grandeur, halls carved into the roots of mountains, the echoing of picks and hammers in deep mines and blazing forges, a commitment to clan and tradition, and a burning hatred of goblins and orcs – these common threads unite all dwarves."),
	("Dragonborn","Dragonborn feature"),
	("Elf","Elf feature"),
	("Gnome","Gnome feature"),
	("Half-Elf","Half-Elf feature"),
	("Half-Orc","Half-Orc feature"),
	("Halfling","Halfling feature"),
	("Human","Human feature"),
	("Tiefling","Tiefling feature"),
	("Githyanki","Ability Score Increase. Your Intelligence score increases by 1. Your Strength score increases by 2."),
	("Decadent Mastery","You learn one language of your choice, and you are proficient with one skill or tool of your choice. In the timeless city of Tu'narath, githyanki have bountiful time to master odd bits of knowledge."),
	("Martial Prodigy", "You are proficient with light and medium armor and with shortswords, longswords, and greatswords."),
	("Githyanki Psionics","You know the Mage Hand cantrip, and the hand is invisible when you cast the cantrip with this trait.
        When you reach 3rd level, you can cast the Jump spell once with this trait, and you regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the Misty Step spell once with this trait, and you regain the ability to do so when you finish a long rest.
        Intelligence is your spellcasting ability for these spells. When you cast them with this trait, they don't require components.")
    

"""
#shows preqresuites of the features
preqresuites = """

	("Animal Handler","Animal Handler","Automatic"),
	("Alert","Alert","Automatic"),
	("Athlete","Athlete","Automatic"),
	("Charger","Charger","Automatic"),
	("Crossbow Expert","Crossbow Expert","Automatic"),
	("Defensive Duelist","Defensive Duelist","Automatic"),
	("Dual Wielder","Dual Wielder","Automatic"),
	("Mobile","Mobile","Automatic"),
	("Shield Training","Shield Training","Automatic"),

	("Barbarian 1","Rage","Automatic"),
	("Bard 1","Bardic Inspiration","Automatic"),
	("Cleric 1","Divine Domain","Selection"),
	("Druid 1","Druidic","Automatic"),
	("Fighter 1","Second Wind","Automatic"),
	("Monk 1","Martial Arts","Automatic"),
	("Paladin 1","Fighting Style","Selection"),
	("Ranger 1","Fighting Style","Selection"),
	("Rogue 1","Expertise","Selection"),
	("Rogue 1","Sneak Attack","Automatic"),
	("Rogue 1","Thieves' Cant","Automatic"),
	("Rogue 2","Cunning Action","Automatic"),	
	("Rogue 3","Roguish Archtype","Selection"),	
	("Revived","Tokens of Past Lives","Automatic"),
	("Revived","Revived Nature","Automatic"),
	("Revived","Bolts from the Grave","Automatic"),
	("Rogue 5","Uncanny Dodge","Automatic"),
	("Rogue 7","Evasion","Automatic"),

	("Sorcerer 1","Sorcerous Origin","Selection"),
	("Warlock 1","Otherworldly Patron","Selection"),
	("Wizard 1","Spellbook","Automatic"),


	("Githyanki","Githyanki","Automatic"),
	("Githyanki","Decadent Mastery","Automatic"),
	("Githyanki","Martial Prodigy","Automatic"),
	("Githyanki","Githyanki Psionics","Automatic"),
	("Dwarf","Dwarf","Automatic"),
	("Dragonborn","Dragonborn","Automatic"),
	("Elf","Elf","Automatic"),
	("Gnome","Gnome","Automatic"),
	("Half-Elf","Half-Elf","Automatic"),
	("Half-Orc","Half-Orc","Automatic"),
	("Halfling","Halfling","Automatic"),
	("Human","Human","Automatic"),
	("Tiefling","Tiefling","Automatic")
	
"""

#shows features that the character satisfies preqresuites
#might need revision
preqresuitesatisfaction = """

	("Rizzrack","Githyanki"),
	("Rizzrack","Decadent Mastery"),
	("Rizzrack","Martial Prodigy"),
	("Rizzrack","Githyanki Psionics"),

	("Rizzrack","Mobile"),
	("Rizzrack","Shield Training"),

	("Rizzrack","Expertise"),
	("Rizzrack","Sneak Attack"),
	("Rizzrack","Thieves' Cant"),
	("Rizzrack","Cunning Action"),
	("Rizzrack","Tokens of Past Lives"),
	("Rizzrack","Revived Nature"),
	("Rizzrack","Bolts from the Grave"),
	("Rizzrack","Uncanny Dodge"),
	("Rizzrack","Evasion")
"""

#shows what features character have
characterfeature = """
	("Rizzrack","Githyanki"),
	("Rizzrack","Decadent Mastery"),
	("Rizzrack","Martial Prodigy"),
	("Rizzrack","Githyanki Psionics"),

	("Rizzrack","Mobile"),
	("Rizzrack","Shield Training"),

	("Rizzrack","Expertise"),
	("Rizzrack","Sneak Attack"),
	("Rizzrack","Thieves' Cant"),
	("Rizzrack","Cunning Action"),
	("Rizzrack","Tokens of Past Lives"),
	("Rizzrack","Revived Nature"),
	("Rizzrack","Bolts from the Grave"),
	("Rizzrack","Uncanny Dodge"),
	("Rizzrack","Evasion")
"""

#SHOWS what selections character made
characterselection = """
	("Rizzrack","Mobile"),
	("Rizzrack","Shield Training"),
	("Rizzrack","Githyanki"),
	("Rizzrack","Rogue 1"),
	("Rizzrack","Rogue 2"),
	("Rizzrack","Rogue 3"),
	("Rizzrack","Rogue 4"),
	("Rizzrack","Rogue 5"),
	("Rizzrack","Rogue 6"),
	("Rizzrack","Rogue 7"),
	("Rizzrack","Rogue 8")
"""

#action bonus action vs vs
resources = """
	("Action"),
	("Bonus Action"),
	("Reaction"),
	("Free Object Interaction"),
	("Free Action"),
	("Spell Slot"),
	("Bardic Inspiration")
"""

#which feature uses which resource
resourceconsumption = """
	("Bonus Action","Cunning Action"),
	("Action","Attack Action"),
	("Bonus Action","Two-Weapon Fighting"),
	("Reaction","Opportunity Attack"),
	("Action","Githyanki Psionics"),
	("Bonus Action","Githyanki Psionics"),
	("Free Object Interaction","Shield Training")
	("Reaction","Uncanny Dodge"),
"""