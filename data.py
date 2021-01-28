deneme = "('deneme','deneme')"

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

	("Barbarian 1","Subclass"),
	("Bard 1","Subclass"),
	("Cleric 1","Subclass"),
	("Druid 1","Subclass"),
	("Fighter 1","Subclass"),
	("Monk 1","Subclass"),
	("Paladin 1","Subclass"),
	("Ranger 1","Subclass"),
	("Rogue 1","Subclass"),
	("Rogue 2","Subclass"),
	("Sorcerer 1","Subclass"),
	("Warlock 1","Subclass"),
	("Wizard 1","Subclass"),

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
	("Sorcerer","Sorcerer 1"),
	("Warlock","Warlock 1"),
	("Wizard","Wizard 1")
"""

features = """
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

preqresuites = """

	("Animal Handler","Animal Handler"),
	("Alert","Alert"),
	("Athlete","Athlete"),
	("Charger","Charger"),
	("Crossbow Expert","Crossbow Expert"),
	("Defensive Duelist","Defensive Duelist"),
	("Dual Wielder","Dual Wielder"),
	("Mobile","Mobile"),
	("Shield Training","Shield Training"),

	("Barbarian 1","Rage"),
	("Bard 1","Bardic Inspiration"),
	("Cleric 1","Divine Domain"),
	("Druid 1","Druidic"),
	("Fighter 1","Second Wind"),
	("Monk 1","Martial Arts"),
	("Paladin 1","Fighting Style"),
	("Ranger 1","Fighting Style"),
	("Rogue 1","Expertise"),
	("Rogue 1","Sneak Attack"),
	("Rogue 1","Thieves' Cant"),
	("Rogue 2","Cunning Action"),
	("Sorcerer 1","Sorcerous Origin"),
	("Warlock 1","Otherworldly Patron"),
	("Wizard 1","Spellbook"),


	("Githyanki","Githyanki"),
	("Githyanki","Decadent Mastery"),
	("Githyanki","Martial Prodigy"),
	("Githyanki","Githyanki Psionics"),
	("Dwarf","Dwarf"),
	("Dragonborn","Dragonborn"),
	("Elf","Elf"),
	("Gnome","Gnome"),
	("Half-Elf","Half-Elf"),
	("Half-Orc","Half-Orc"),
	("Halfling","Halfling"),
	("Human","Human"),
	("Tiefling","Tiefling")
	
"""



characterselection = """
	("deneme","Mobile"),
	("deneme","Shield Training"),
	("deneme","Githyanki"),
	("deneme","Rogue 1")
"""