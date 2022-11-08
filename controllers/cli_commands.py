from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.traits import Trait
from models.champs import Champion
from models.items import Item

db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")

# Creating generic user accounts for testing and admin purposes
@db_commands.cli.command('seed')
def seed_db():
    users = [
        User(
            email = 'admin@tft.com',
            password = bcrypt.generate_password_hash('eggs').decode('utf-8'),
            is_admin = True
        ),
        User(
            name = 'Cheese Steiner',
            email = 'cheeseman@generic.com',
            password = bcrypt.generate_password_hash('12345').decode('utf-8'),
        ),
    ]

    traits = [
        # Origins
        Trait(
            name = "Astral",
            description = "After each player combat, gain an Astral Orb. The combined star level of your Astral champions increases the quality of the orb. Astral champions gain Ability Power",
            Breakpoints = "3/5/8"
        ),
        Trait(
            name = "Darkflight",
            description = "The unit in the Darkflight hex is sacrificed, granting a copy of an item they have to each Darkflight champion, and bonus health to each.",
            Breakpoints = "2/4/6/8"
        ),
        Trait(
            name = "Dragon",
            description = "Dragons require 2 team slots, provide +3 to their marked trait and gain additional bonuses based on how many Dragons are on your team.",
            Breakpoints = "1/2/3/4/5/6"
        ),
        Trait(
            name = "Guild",
            description = "Grant a unique bonus to your team; Guild allies gain double the amount. Increases for each Guild member in play! Sejuani: +130 Health Twitch: +11% Attack Speed Zippy: +8 Armor and Magic Resist Jayce: +5 Attack Damage and Ability Power Bard: +2 Mana per attack Emblem: +3% Omnivamp"
        ),
        Trait(
            name = "Jade",
            description = "Summon movable Jade Statues that grow in power. Allies adjacent to a statue gain Attack Speed and maximum Health healing every 2 seconds. When a statue is destroyed, it deals 33% of its Health as magic damage to nearby enemies."
        ),
        Trait(
            name = "Lagoon",
            description = "Lagoon units gain bonus Ability Power and Attack Speed. A Seastone appears on the board that grants loot as Lagoon units cast Abilities over time.",
            breakpoints = "3/6/9/12"
        ),
        Trait(
            name = "Mirage",
            description = "Mirage champions gain a different Trait bonus from game to game. Variations: Electric Overload, Warlord, Pirate, Dawnbringer, Executioner, Spellsword, Duelist.",
            breakpoints = "2"
        ),
        Trait(
            name = "Scalescorn",
            description = "Innate: Convert Mana to Rage; Attacks generate 15 Rage. After casting an Ability, enrage for 4 seconds: +30% Attack Speed but can't gain Rage. Gain bonus stats when enraged.",
            breakpoints = "2/4/6/8"
        ),
        Trait(
            name = "Ragewing",
            description = "Innate: Convert Mana to Rage; Attacks generate 15 Rage. After casting an Ability, enrage for 4 seconds: +30% Attack Speed but can't gain Rage. Gain bonus stats when enraged.",
            breakpoints = "2/4/6/8"
        ),
        Trait(
            name = "Shimmerscale",
            description = "Grants exclusive random Shimmerscale items.",
            breakpoints = "3/5/7/9"
        ),
        Trait(
            name = "Bruiser",
            description = "Your team gains bonus maximum Health. Bruisers gain double this bonus."
        ),
        # Classes
        Trait(
            name = "Assassin",
            description = "Innate: Leap to the enemy backline. Assassins' gain bonus Critical Strike Chance and Damage and their abilities can critally strike.",
            breakpoints = "2/4/6"
        ),
        Trait(
            name = "Bard",
            description = "Innate: Leap to the enemy backline. Assassins' gain bonus Critical Strike Chance and Damage and their abilities can critally strike.",
            breakpoints = "2/4/6"
        ),
        Trait(
            name = "Bruiser",
            description = "Your team gains bonus maximum Health. Bruisers gain double this bonus."
        ),
        Trait(
            name = "Cavalier",
            description = "Innate: Charge quickly towards their target whenever they move. Cavaliers gain Armor and Magic Resist. At the start of combat and after each charge, gain 200% the amount for 4 seconds.",
            breakpoints = "2 - "
        ),
        Trait(
            name = "Shapeshifter",
            description = "Transforming grants bonus maximum Health, and heals for that amount."
        ),
        Trait(
            name = "Guardian",
            description = "Once per combat at 50% Health, Guardians shield themselves and their closest ally. Shields stack!"
        ),  
        Trait(
            name = "Warrior",
            description = "Warrior attacks have a 50% chance to increase the damage of their next attack.",
            breakpoint = "2 - 75% damage. 4 - 150% damage. 6 - 275% damage"
        )     
    ]

    items = [
        Item(
            name = "Archangel's Staff",
            item_bonus = "Grant 10 bonus Ability Power. Gain 20 Ability Power every 5 seconds.",
            stats = "10 Mana, 15 Ability Power"
        ),
        Item(
            name = "Banshee's Claw",
            item_bonus = "Grant a shield to the holder and allies within 1 hex in the same row that blocks the first enemy Ability",
            stats = "150 Health, 15% Dodge Chance"
        ),
        Item(
            name = "Bloodthirster",
            item_bonus = "At 40% Health, gain a 25% maximum Health shield.",
            stats = "10 Attack Damage, 20 Magic Resistance"
        ),
        Item(
            name = "Blue Buff",
            item_bonus = "Grant 20 bonus starting Mana. After casting an Ability, set Mana to 20.",
            stats = "30 Mana"
        ),
        Item(
            name = "Bramble Vest",
            item_bonus = "Grant 40 bonus Armor. Resists damage from critical strikes. When struck by an attack, damage all nearby enemies.",
            stats = "40 Armor"
        ),
        Item(
            name = "Chalice of Power",
            item_bonus = "Grant 30 Ability Power to the holder and allies within 1 hex in the same row.",
            stats = "20 Magic Resistance, 15 Mana"
        ),
        Item(
            name = "Death Blade",
            item_bonus = "Grant 15/30/45 (based on champion level) bonus Attack Damage",
            stats = "20 Attack Damage"
        ),
        Item(
            name = "Dragon's Claw",
            item_bonus = "Grant 80 bonus Magic Resist. Every 2 seconds, regenerate 1.2% maximum Health.",
            stats = "40 Magic Resistance"
        ),
        Item(
            name = "Edge of Night",
            item_bonus = "At 60% Health, briefly become untargetable. Then, grant bonus Attack Speed.",
            stats = "10 Attack Damage, 20 Armor"
        ),
        Item(
            name = "Gargoyle Stoneplate",
            item_bonus = "Grants 16 Armor and 16 Magic Resist for each enemy targeting the holder.",
            stats = "20 Magic Resistance, 20 Armor"
        ),
        Item(
            name = "Giant Slayer",
            item_bonus = "Deal 20% bonus damage. boosted to 45% if the target has 2200+ Health.",
            stats = "10 Attack Damage, 10% Attack Speed"
        ),
        Item(
            name = "Guinsoo's Rageblade",
            item_bonus = "Attacks grant 6% bonus Attack Speed. This effect stacks.",
            stats = "10 Ability Power, 10% Attack Speed"
        ),
        Item(
            name = "Hand of Justice",
            item_bonus = "Grants 15 Attack Damage, Ability Power and Omnivamp.",
            stats = "10 Mana, 15% Critical Strike Chance"
        ),
        Item(
            name = "Hextech Gunblade",
            item_bonus = "Grant 25% Omnivamp. The lowest health ally is also healed.",
            stats = "10 Attack Damage, 10 Ability Power"
        ),
        Item(
            name = "Infinity Edge",
            item_bonus = "Grants 60% Critical Strike Chance and 10% Critical Strike Damage.",
            stats = "10 Attack Damage"
        ),
        Item(
            name = "Ionic Spark",
            item_bonus = "Enemies within 2 hexes have their Magic Resist reduced by 50%.",
            stats = "10 Ability Power, 20 Magic Resistance"
        ),
        Item(
            name = "Jeweled Gauntlet",
            item_bonus = "Grant 10% Critical Strike Damage and 30 bonus Ability Power. Abilities can Crit",
            stats = "10 Ability Power, 15% Critical Strike Chance"
        ),
        Item(
            name = "Last Whisper",
            item_bonus = "Grant 10% Attack Speed. Dealing physical damage reduces the target's Armor by 50%",
            stats = "10% Attack Speed, 15% Critical Strike Chance"
        ),
        Item(
            name = "Locket of the Iron Salari",
            item_bonus = "Shields the holder and allies within 2 hexes in the same row.",
            stats = "10 Ability Power, 20 Armor"
        ),
        Item(
            name = "Morellonomicon",
            item_bonus = "Grant 20 Ability Power. Ability damage burns the target and reduces healing.",
            stats = "10 Ability Power, 150 Health"
        ),
        Item(
            name = "Protectors Vow",
            item_bonus = "Grant 15 bonus starting Mana. At 50% Health, allies within 3 hexes gain a shield and defensive stats.",
            stats = "20 Armor, 15 Mana"
        ),
        Item(
            name = "Quicksilver",
            item_bonus = "Grant 20% Attack Speed. Grant immunity to crowd control.",
            stats = "20 Magic Resistance, 15% Dodge Chance"
        ),
        Item(
            name = "Rabadon's Deathcap",
            item_bonus = "Grant 55 bonus Ability Power.",
            stats = "20 Ability Power"
        ),
        Item(
            name = "Rapid Firecannon",
            item_bonus = "Grant 30% Attack Speed, 1 bonus Attack Range and attacks cannot miss.",
            stats = "40% Attack Speed"
        ),
        Item(
            name = "Redemption",
            item_bonus = "Heal and reduce damage to allies within 1 hex every 5 seconds.",
            stats = "150 Health, 15 Mana"
        ),
        Item(
            name = "Runaan's Hurricane",
            item_bonus = "Grant 10 Attack Damage. Attacks fire a bolt at a nearby enemy, dealing reduced physical damage.",
            stats = "20 Magic Resistance, 10% Attack Speed"
        ),
        Item(
            name = "Shroud of Stillness",
            item_bonus = "Shoot a beam that increases the spell cost of affected enemies.",
            stats = "20 Armor, 15% Dodge Chance"
        ),
        Item(
            name = "Spear of Shojin",
            item_bonus = "Grant 20 Ability Power. Attacks restore 5 additional Mana.",
            stats = "10 Attack Damage, 15 Mana"
        ),
        Item(
            name = "Statikk Shiv",
            item_bonus = "Grant 10% Attack Speed. Every 3rd attack bounces to 4 extra enemies dealing magic damage.",
            stats = "10% Attack Speed, 15 Mana"
        ),
        Item(
            name = "Sunfire Cape",
            item_bonus = "Grant 150 Health. Every 2 seconds, burn a nearby enemy dealing true damage and reducing healing.",
            stats = "150 Health, 20 Armor"
        ),
        Item(
            name = "Theive's Gloves",
            item_bonus = "Equip 2 random items. (Can't equip other items)",
            stats = "15% Critical Strike Chance, 15% Dodge Chance"
        ),
        Item(
            name = "Titan's Resolve",
            item_bonus = "Grants 2 Attack Damage and 2 Ability Power when attacking or taking damage, stacking up to 25 times. Grants 25 Armor and Magic Resistance at 25 stacks.",
            stats = "10% Attack Speed, 20 Armor"
        ),
        Item(
            name = "Warmog's Armor",
            item_bonus = "Grant 700 Health.",
            stats = "300 Health"
        ),
        Item(
            name = "Zeke's Herald",
            item_bonus = "Grant 30% Attack Speed to the holder and allies within 1 hex in the same row.",
            stats = "10 Attack Damage, 150 Health"
        ),
        Item(
            name = "Zephyr",
            item_bonus = "Summon a whirlwind on the opposite side of the arena that removes an enemy from combat for 5 seconds.",
            stats = "20 Magic Resistance, 150 Health"
        ),
        Item(
            name = "Zz'Rot Portal",
            item_bonus = "Taunt enemies On death, a Voidspawn arises, taunting nearby enemies.",
            stats = "150 Health, 10% Attack Speed"
        )


    ]
    # CAN YOU MAKE THE BREAKPOINT A LIST


    # Unsure if both traits and users can be included in the one add parameter
    db.session.add_all(traits, users)
    db.session.commit()

    champs = [
        Champion(
            name = "Ao Shin",
            cost = "8",
            ability = "Fires a barrage of lightning strikes at random enemies",
            suggested_items = "Spear of Shojin, Archangel's Staff, Hextech Gunblade"
        ),
            Champion(
            name = "Aphelios",
            cost = "2",
            ability = "Uses his Infernum cannon to blast bolts in a cone towards his target.",
            suggested_items = "Zeke's Herald, Last Whisper, Infinity Edge"
        ),
        Champion(
            name = "Aurelion Sol",
            cost = "8",
            ability = "Summons an unstable black hole underneath a random enemy.",
            suggested_items = "Hextech Gunblade, Archangel's Staff, Jeweled Gauntlet"
        ),
        Champion(
            name = "Bard",
            cost = "5",
            ability = "Sends magical energy toward the largest group of enemies, stunning them and causing them to take increased damage while stunned",
            suggested_items = "Spear of Shojin, Shroud of Stillness, Zeke's Herald"
        ),
        Champion(
            name = "Braum",
            cost = "2",
            ability = "Puts up his shield towards the largest group of enemies for 4 seconds",
            suggested_items = "Sunfire Cape, Warmog's Armor, Bramble Vest"
        ),
        Champion(
            name = "Deeja",
            cost = "7",
            ability = "Sends a wind blast toward the largest group of enemies.",
            suggested_items = "Guinsoo's Rageblade, Giant Slayer, Archangel's Staff"
        ),
        Champion(
            name = "Diana",
            cost = "3",
            ability = "Shields herself and summons damaging orbs around her. ",
            suggested_items = "Ionic Spark, Hand of Justice, Sunfire Cape"
        ),
        Champion(
            name = "Dragon Tyrant Swain",
            cost = "7",
            ability = "Launches 8 dragonlings toward enemies that deal damage and heal Swain",
            suggested_items = "Morellonomicon, Titan's Resolve, Archangel's Staff"
        ),
        Champion(
            name = "Ezreal",
            cost = "1",
            ability = "Fires an energy bolt towards his target",
            suggested_items = "Blue Buff, Infinity Edge, Jeweled Gauntlet"
        ),
        Champion(
            name = "Gnar",
            cost = "2",
            ability = "Transforms into Mega Form, knocking up nearby enemies.",
            suggested_items = "Sunfire Cape, Protector's Vow, Redemption"
        ),
        Champion(
            name = "Graves",
            cost = "4",
            ability = "Dashes towards his target, quickly fires two attacks.",
            suggested_items = "Edge of Night, Titan's Resolve, Bloodthirster"
        ),
        Champion(
            name = "Hecarim",
            cost = "4",
            ability = "Summons spectral riders that charge through his target",
            suggested_items = "Morellonomicon, Protector's Vow, Zz'Rot Portal"
        ),
        Champion(
            name = "Idas",
            cost = "7",
            ability = "Hardens her scales for 2 seconds, reducing incoming damage.",
            suggested_items = "Gargoyle Stoneplate"
        ),
        Champion(
            name = "Jax",
            cost = "2",
            ability = "Dodges all incoming attacks for 2 seconds.",
            suggested_items = "Sunfire Cape, Gargoyle Stoneplate, Warmog's Armor"
        ),
        Champion(
            name = "Jayce",
            cost = "4",
            ability = "Transforms to his melee form, then slams the ground around his target.",
            suggested_items = "Ionic Spark, Protector's Vow, Warmog's Armor"
        ),
        Champion(
            name = "Kai'Sa",
            cost = "2",
            ability = "Fires 4 missiles split between her target and up to 2 other targets.",
            suggested_items = "Blue Buff, Archangel's Staff, Giant Slayer"
        ),
        Champion(
            name = "Karma",
            cost = "1",
            ability = "Fires a burst of energy towards her target.",
            suggested_items = "Blue Buff, Jeweled Gauntlet, Infinity Edge"
        ),
        Champion(
            name = "Lee Sin",
            cost = "3",
            ability = "Kicks his target, stunning and knocking them back.",
            suggested_items = "Hand of Justice, Infinity Edge, Jeweled Gauntlet"
        ),
        Champion(
            name = "Leona",
            cost = "1",
            ability = "Creates a barrier around herself, reducing all incoming damage.",
            suggested_items = "Warmog's Armor, Sunfire Cape, Dragon's Claw"
        ),
        Champion(
            name = "Lillia",
            cost = "2",
            ability = "Strikes a small area around her target's current location.",
            suggested_items = "Ionic Spark, Bloodthirster, Archangel's Staff"
        ),
        Champion(
            name = "Lux",
            cost = "2",
            ability = "Fires a star towards the farthest enemy.",
            suggested_items = "Spear of Shojin, Jeweled Gauntlet, Infinity Edge"
        ),
        Champion(
            name = "Malphite",
            cost = "1",
            ability = "Shields himself for 5 seconds.",
            suggested_items = "Zz'Rot Portal, Sunfire Cape, Gargoyle Stoneplate"
        ),
        Champion(
            name = "Nasus",
            cost = "1",
            ability = "Surrounds himself in light gaining health and dealing damage.",
            suggested_items = "Warmog's Armor, Titan's Resolve, Morellonomicon"
        ),
        Champion(
            name = "Nidalee",
            cost = "1",
            ability = "Transforms into Cougar Form for the rest of combat, gaining bonus stats.",
            suggested_items = "Fuinsoo's Rageblade, Deathblade, Runaan's Hurricane"
        ),
        Champion(
            name = "Nilah",
            cost = "4",
            ability = "Cracks her whip-blade at her target, dashing through them.",
            suggested_items = "Infinity Edge, Hand of Justice, Bloodthirster"
        ),
        Champion(
            name = "Nomsy (Mage)",
            cost = "6",
            ability = "Lobs a massive fireball towards 2 random targets.",
            suggested_items = "Spear of Shojin, Jewelled Gauntlet, Infinity Edge"
        ),
        Champion(
            name = "Nomsy (Evoker)",
            cost = "6",
            ability = "Lobs a massive fireball towards 2 random targets.",
            suggested_items = "Spear of Shojin, Jewelled Gauntlet, Infinity Edge"
        ),
        Champion(
            name = "Nomsy (Cannoneer)",
            cost = "6",
            ability = "Lobs a massive fireball towards 2 random targets.",
            suggested_items = "Spear of Shojin, Jewelled Gauntlet, Infinity Edge"
        ),
        Champion(
            name = "Nunu",
            cost = "3",
            ability = "Bites his target, dealing magic damage.",
            suggested_items = "Warmog's Armor, Sunfire Cape, Redemption"
        ),
        Champion(
            name = "Olaf",
            cost = "3",
            ability = "Strikes his target, gaining bonus attack speed.",
            suggested_items = "Infinity Edge, Bloodthirster, Rapid Firecannon"
        ),
        Champion(
            name = "Pantheon",
            cost = "4",
            ability = "Braces his shield, dealing damage in front of him.",
            suggested_items = "Bloodthirster, Titan's Resolve, Edge of Night"
        ),
        Champion(
            name = "Qiyana",
            cost = "2",
            ability = "Dashes to the best position to strike enemies with her blade.",
            suggested_items = "Shroud of Stillness, Banshee's Claw, Zephyr"
        ),
        Champion(
            name = "Rakan",
            cost = "3",
            ability = "Dashes to the farthest enemy, disarming units he travels through.",
            suggested_items = "Sunfire Cape, Protector's Vow, Zz'Rot Portal"
        ),
        Champion(
            name = "Rell",
            cost = "2",
            ability = "Tethers to an ally which protects her ally and deals damage to enemies.",
            suggested_items = "Protector's Vow, Sunfire Cape, Zeke's Herald"
        ),
        Champion(
            name = "Rengar",
            cost = "3",
            ability = "Leaps to the lowest armor enemy, dealing damage.",
            suggested_items = "Infinity Edge, Bloodthirster, Runaan's Huricane"
        ),
        Champion(
            name = "Sejuani",
            cost = "1",
            ability = "Swings her mace wide, hitting all enemies in a cone dealing damage.",
            suggested_items = "Sunfire Cape, Zz'Rot Portal, Chalice of Power"
        ),
        Champion(
            name = "Senna",
            cost = "1",
            ability = "Launches black mist toward the farthest enemy dealing damage.",
            suggested_items = "Thief's Gloves, Guinsoo's Rageblade, Last Whisper"
        ),
        Champion(
            name = "Seraphine",
            cost = "3",
            ability = "Grants a shield and bonus damage to allies",
            suggested_items = "Morellonomicon, Spear of Shojin, Rabadon's Deathcap"
        ),
        Champion(
            name = "Sett",
            cost = "1",
            ability = "Gains Armor and Magic Resist.",
            suggested_items = "Guinsoo's Rageblade, Quicksilver, Giant Slayer"
        ),
        Champion(
            name = "Shi Oh Yu",
            cost = "7",
            ability = "Gains damage reduction, immunity to cc, and empowering her next 3 attacks",
            suggested_items = "Bloodthirster, Titan's Resolve, Edge of Night"
        ),
        Champion(
            name = "Shyvana",
            cost = "8",
            ability = "Transforms into Dragon Form for the rest of combat.",
            suggested_items = "Morellonomicon, Ionic Spark, Archangel's Staff"
        ),
        Champion(
            name = "Skarner",
            cost = "1",
            ability = "Shields himself for 8 seconds and gains Attack Speed.",
            suggested_items = "Sunfire Cape, Zz'Rot Portal, Redemption"
        ),
        Champion(
            name = "Sohm",
            cost = "7",
            ability = "Sends out a tide dealing damage.",
            suggested_items = "Blue Buff, Morellonomicon, Jeweled Gauntlet"
        ),
        Champion(
            name = "Soraka",
            cost = "5",
            ability = "Calls down a shower of stars that heals allies.",
            suggested_items = "Spear of Shojin, Chalice of Power, Statikk Shiv"
        ),
        Champion(
            name = "Syfen",
            cost = "7",
            ability = "Charges forward, dealing damage and knocking up enemies.",
            suggested_items = "Bloodthirster, Titan's Resolve, Quicksilver"
        ),
        Champion(
            name = "Sylas",
            cost = "7",
            ability = "Whirls his chains, dealing damage and applying Mana-Reave.",
            suggested_items = "Gargoyle Stoneplate, Sunfire Cape, Zz'Rot Portal"
        ),
        Champion(
            name = "Taliyah",
            cost = "1",
            ability = "Deals damage by throwing 3 seastones at her target.",
            suggested_items = "Spear of Shojin, Rabadon's Deathcap, Statikk Shiv"
        ),
        Champion(
            name = "Terra",
            cost = "8",
            ability = "Stomps three times causing an earthquake around them, dealing damage.",
            suggested_items = "Gargoyle Stoneplate, Bramble Vest, Dragon's Claw"
        ),
        Champion(
            name = "Twitch",
            cost = "2",
            ability = "Hurls an exploding flask, dealing physical damage and reducing Armor.",
            suggested_items = "Infinity Edge, Last Whisper, Runaan's Hurricane"
        ),
        Champion(
            name = "Varus",
            cost = "3",
            ability = "Sends out a cosmic tendril that strikes the first enemy hit.",
            suggested_items = "Guinsoo's Rageblade, Giant Slayer, Runaan's Hurricane"
        ),
        Champion(
            name = "Vladimir",
            cost = "1",
            ability = "Deals damage to the target and heals himself.",
            suggested_items = "Warmog's Armor, Titan's Resolve, Redemption"
        ),
        Champion(
            name = "Volibear",
            cost = "3",
            ability = "Rages, gaining bonus Health. Every 3rd attack hits surrounding enemies",
            suggested_items = "Guinsoo's Rageblade, Bloodthirster, Quicksilver"
        ),
        Champion(
            name = "Wukong",
            cost = "1",
            ability = "Slams his target with his staff, dealing extra damage and stunning.",
            suggested_items = "Rapid Firecannon, Deathblade, Infinity Edge"
        ),
        Champion(
            name = "Xayah",
            cost = "4",
            ability = "Attacks also fire a feather which are recalled and deal damage.",
            suggested_items = "Guinsoo's Rageblade, Giant Slayer, Last Whisper"
        ),
        Champion(
            name = "Yasuo",
            cost = "5",
            ability = "Shields himself and dashes through his target, dealing damag.e",
            suggested_items = "Blue Buff, Bloodthirster, Titan's Resolve"
        ),
        Champion(
            name = "Yone",
            cost = "2",
            ability = "Basic attacks deal bonus damage.",
            suggested_items = "Guinsoo's Rageblade, Quicksilver, Bloodthirster"
        ),
        Champion(
            name = "Zac",
            cost = "2",
            ability = "Explodes outward, dealing damage to enemies and healing himself.",
            suggested_items = "Bramble Vest, Dragon's Claw, Warmog's Armor"
        )
    ]