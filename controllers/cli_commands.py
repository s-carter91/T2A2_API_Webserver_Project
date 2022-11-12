from flask import Blueprint
from init import db, bcrypt
from models.users import User
# from models.traits import Trait
# from models.champions import Champion
# from models.items import Item
from models.teamboards_champions import Teamboard, Champion, Trait, Item
from models.origins import Origin

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
            username = 'admin',
            email = 'admin@tft.com',
            password = bcrypt.generate_password_hash('tft').decode('utf-8'),
            is_admin = True
        ),
        User(
            username = 'Cheese_Steiner',
            email = 'cheeseman@generic.com',
            password = bcrypt.generate_password_hash('cheese').decode('utf-8'),
        ),
    ]

    origins = [
        # Origins
        Origin(
            name = "Astral",
            description = "After each player combat, gain an Astral Orb. The combined star level of your Astral champions increases the quality of the orb. Astral champions gain Ability Power",
            breakpoints = "3 / 5 / 8"
        ),
        Origin(
            name = "Darkflight",
            description = "The unit in the Darkflight hex is sacrificed, granting a copy of an item they have to each Darkflight champion, and bonus health to each.",
            breakpoints = "2 / 4 / 6 / 8"
        ),
        Origin(
            name = "Dragon",
            description = "Dragons require 2 team slots, provide +3 to their marked trait and gain additional bonuses based on how many Dragons are on your team.",
            breakpoints = "1 / 2 / 3 / 4 / 5 / 6"
        ),
        Origin(
            name = "Guild",
            description = "Grant a unique bonus to your team depending of which guilds are played",
            breakpoints = "1 / 2 / 3 / 4 / 5 / 6 / 7 / 8"
        ),
        Origin(
            name = "Jade",
            description = "Summon movable Jade Statues that grow in power. Allies adjacent to a statue gain Attack Speed healing.",
            breakpoints = "3 / 6 / 9 / 12"
        ),
        Origin(
            name = "Lagoon",
            description = "Lagoon units gain bonus Ability Power and Attack Speed. A Seastone appears on the board that grants loot as Lagoon units cast Abilities over time.",
            breakpoints = "3 / 6 / 9 / 12"
        ),
        Origin(
            name = "Mirage",
            description = "Mirage champions gain a different bonus from game to game. Variations: Electric Overload, Warlord, Pirate, Dawnbringer, Executioner, Spellsword, Duelist.",
            breakpoints = "2 / 4 / 6 / 8"
        ),
        Origin(
            name = "Ragewing",
            description = "Innate: Convert Mana to Rage; Attacks generate 15 Rage. After casting an Ability, enrage for 4 seconds: +30% Attack Speed but can't gain Rage. Gain bonus stats when enraged.",
            breakpoints = "2 / 4 / 6 / 8"
        ),
        Origin(
            name = "Scalescorn",
            description = "Deal extra magic damage. Bonus damage to higher health enemies.",
            breakpoints = "2 / 4 / 6 / 8"
        ),
        Origin(
            name = "Shimmerscale",
            description = "Grants exclusive random Shimmerscale items.",
            breakpoints = "3 / 5 / 7 / 9"
        ),
        Origin(
            name = "Tempest",
            description = "Stuns enemy team and Tempest units get extra damage.",
            breakpoints = "2 / 4 / 6 / 8"
        ),
        Origin(
            name = "Whispers",
            description = "Whispers damage reduces Armor and Magic Resist of enemies.",
            breakpoints = "2 / 4 / 6"
        )
    ]
        # Classes
    traits = [
        Trait(
            name = "Assassin",
            description = "Assassins' gain bonus Critical Strike Chance and Damage and their abilities can critally strike.",
            breakpoints = "2 / 4 / 6"
        ),
        Trait(
            name = "Bard",
            description = "Allies that survive combat have a chance to create a Doot. Bard always creates a Doot when dancing.",
            breakpoints = "1"
        ),
        Trait(
            name = "Bruiser",
            description = "Your team gains bonus maximum Health. Bruisers gain double this bonus.",
            breakpoints = '2 / 4 / 6 / 8'
        ),
        Trait(
            name = "Cannoneer",
            description = "Every 5th attack deals damage around the target.",
            breakpoints = "2 / 4 / 6"
        ),
        Trait(
            name = "Cavalier",
            description = "Cavaliers gain Armor and Magic Resist.",
            breakpoints = "2 / 3 / 4 / 5 / 6"
        ),
        Trait(
            name = "Dragonmancer",
            description = "Select a Dragonmancer Hero. The Hero gains increased Health and Ability Power.",
            breakpoints = "2 / 4 / 6 / 8"
        ),
        Trait(
            name = "Evoker",
            description = "Gain Mana whenever an ally or enemy casts an Ability.",
            breakpoints = "2 / 3 / 4"
        ),
        Trait(
            name = "Guardian",
            description = "Once per combat at 50% Health, Guardians shield themselves and their closest ally. Shields stack!",
            breakpoints = "2 / 4 / 6 / 8"
        ),
        Trait(
            name = "Mage",
            description = "Mages cast abilities twice and have modified total Ability Power.",
            breakpoints = "3 / 5 / 7 / 9"
        ),
        Trait(
            name = "Monolith",
            description = "Terra create 3 hexes on the battlefield. Units standing in the hex gain damage reduction.",
            breakpoints = "1"
        ),
        Trait(
            name = "Mystic",
            description = "Your team gains Magic Resist.",
            breakpoints = "2 / 3 / 4 / 5"
        ),
        Trait(
            name = "Shapeshifter",
            description = "Transforming grants bonus maximum Health, and heals for that amount.",
            breakpoints = "2 / 4"
        ),
        Trait(
            name = "Spellthief",
            description = "Zoe nabs a new Ability after each cast and at the start of every round.",
            breakpoints = '1'
        ),
        Trait(
            name = "Starcaller",
            description = "The first time Soraka casts her Ability heals you for 2 / 3 / 75, depending on their star level.",
            breakpoints = '1'
        ),
        Trait(
            name = "Swiftshot",
            description = "Gain Attack Range and Attack Speed.",
            breakpoints = "2 / 3 / 4 / 5"
        ) ,
        Trait(
            name = "Warrior",
            description = "Warrior attacks have a chance to increase the damage of their next attack.",
            breakpoints = "2 / 4 / 6"
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
            item_bonus = "Grant 15 / 30 / 45 (based on champion level) bonus Attack Damage",
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


    db.session.add_all(origins)
    db.session.add_all(traits)
    db.session.add_all(users)
    db.session.commit()

    champs = [
        Champion(
            name = "Ao Shin",
            cost = "8",
            ability = "Fires a barrage of lightning strikes at random enemies",
            origin_id = "Tempest",
            suggested_items = "Spear of Shojin, Archangel's Staff, Hextech Gunblade"
        ),
        Champion(
            name = "Aphelios",
            cost = "2",
            ability = "Uses his Infernum cannon to blast bolts in a cone towards his target.",
            origin_id = "Darkflight",
            suggested_items = "Zeke's Herald, Last Whisper, Infinity Edge"
        ),
        Champion(
            name = "Aurelion Sol",
            cost = "8",
            ability = "Summons an unstable black hole underneath a random enemy.",
            origin_id = "Astral",
            suggested_items = "Hextech Gunblade, Archangel's Staff, Jeweled Gauntlet"
        ),
        Champion(
            name = "Bard",
            cost = "5",
            ability = "Sends magical energy toward the largest group of enemies, stunning them and causing them to take increased damage while stunned",
            origin_id = "Guild",
            suggested_items = "Spear of Shojin, Shroud of Stillness, Zeke's Herald"
        ),
        Champion(
            name = "Braum",
            cost = "2",
            ability = "Puts up his shield towards the largest group of enemies for 4 seconds",
            origin_id = "Scalescorn",
            suggested_items = "Sunfire Cape, Warmog's Armor, Bramble Vest"
        ),
        Champion(
            name = "Deeja",
            cost = "7",
            ability = "Sends a wind blast toward the largest group of enemies.",
            origin_id = "Mirage",
            suggested_items = "Guinsoo's Rageblade, Giant Slayer, Archangel's Staff"
        ),
        Champion(
            name = "Diana",
            cost = "3",
            ability = "Shields herself and summons damaging orbs around her. ",
            origin_id = "Scalescorn",
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
            origin_id = "Tempest",
            suggested_items = "Blue Buff, Infinity Edge, Jeweled Gauntlet"
        ),
        Champion(
            name = "Gnar",
            cost = "2",
            ability = "Transforms into Mega Form, knocking up nearby enemies.",
            origin_id = "Jade",
            suggested_items = "Sunfire Cape, Protector's Vow, Redemption"
        ),
        Champion(
            name = "Graves",
            cost = "4",
            ability = "Dashes towards his target, quickly fires two attacks.",
            origin_id = "Tempest",
            suggested_items = "Edge of Night, Titan's Resolve, Bloodthirster"
        ),
        Champion(
            name = "Hecarim",
            cost = "4",
            ability = "Summons spectral riders that charge through his target",
            origin_id = "Ragewing",
            suggested_items = "Morellonomicon, Protector's Vow, Zz'Rot Portal"
        ),
        Champion(
            name = "Idas",
            cost = "7",
            ability = "Hardens her scales for 2 seconds, reducing incoming damage.",
            origin_id = "Shimmerscale",
            suggested_items = "Gargoyle Stoneplate"
        ),
        Champion(
            name = "Jax",
            cost = "2",
            ability = "Dodges all incoming attacks for 2 seconds.",
            origin_id = "Jade",
            suggested_items = "Sunfire Cape, Gargoyle Stoneplate, Warmog's Armor"
        ),
        Champion(
            name = "Jayce",
            cost = "4",
            ability = "Transforms to his melee form, then slams the ground around his target.",
            origin_id = "Guild",
            suggested_items = "Ionic Spark, Protector's Vow, Warmog's Armor"
        ),
        Champion(
            name = "Kai'Sa",
            cost = "2",
            ability = "Fires 4 missiles split between her target and up to 2 other targets.",
            origin_id = "Lagoon",
            suggested_items = "Blue Buff, Archangel's Staff, Giant Slayer"
        ),
        Champion(
            name = "Karma",
            cost = "1",
            ability = "Fires a burst of energy towards her target.",
            origin_id = "Jade",
            suggested_items = "Blue Buff, Jeweled Gauntlet, Infinity Edge"
        ),
        Champion(
            name = "Lee Sin",
            cost = "3",
            ability = "Kicks his target, stunning and knocking them back.",
            origin_id = "Tempest",
            suggested_items = "Hand of Justice, Infinity Edge, Jeweled Gauntlet"
        ),
        Champion(
            name = "Leona",
            cost = "1",
            ability = "Creates a barrier around herself, reducing all incoming damage.",
            origin_id = "Mirage",
            suggested_items = "Warmog's Armor, Sunfire Cape, Dragon's Claw"
        ),
        Champion(
            name = "Lillia",
            cost = "2",
            ability = "Strikes a small area around her target's current location.",
            origin_id = "Scalescorn",
            suggested_items = "Ionic Spark, Bloodthirster, Archangel's Staff"
        ),
        Champion(
            name = "Lux",
            cost = "2",
            ability = "Fires a star towards the farthest enemy.",
            origin_id = "Astral",
            suggested_items = "Spear of Shojin, Jeweled Gauntlet, Infinity Edge"
        ),
        Champion(
            name = "Malphite",
            cost = "1",
            ability = "Shields himself for 5 seconds.",
            origin_id = "Lagoon",
            suggested_items = "Zz'Rot Portal, Sunfire Cape, Gargoyle Stoneplate"
        ),
        Champion(
            name = "Nasus",
            cost = "1",
            ability = "Surrounds himself in light gaining health and dealing damage.",
            origin_id = "Shimmerscale",
            suggested_items = "Warmog's Armor, Titan's Resolve, Morellonomicon"
        ),
        Champion(
            name = "Nidalee",
            cost = "1",
            ability = "Transforms into Cougar Form for the rest of combat, gaining bonus stats.",
            origin_id = "Astral",
            suggested_items = "Fuinsoo's Rageblade, Deathblade, Runaan's Hurricane"
        ),
        Champion(
            name = "Nilah",
            cost = "4",
            ability = "Cracks her whip-blade at her target, dashing through them.",
            origin_id = "Lagoon",
            suggested_items = "Infinity Edge, Hand of Justice, Bloodthirster"
        ),
        Champion(
            name = "Nunu",
            cost = "3",
            ability = "Bites his target, dealing magic damage.",
            origin_id = "Mirage",
            suggested_items = "Warmog's Armor, Sunfire Cape, Redemption"
        ),
        Champion(
            name = "Olaf",
            cost = "3",
            ability = "Strikes his target, gaining bonus attack speed.",
            origin_id = "Scalescorn",
            suggested_items = "Infinity Edge, Bloodthirster, Rapid Firecannon"
        ),
        Champion(
            name = "Pantheon",
            cost = "4",
            ability = "Braces his shield, dealing damage in front of him.",
            origin_id = "Whispers",
            suggested_items = "Bloodthirster, Titan's Resolve, Edge of Night"
        ),
        Champion(
            name = "Qiyana",
            cost = "2",
            ability = "Dashes to the best position to strike enemies with her blade.",
            origin_id = "Tempest",
            suggested_items = "Shroud of Stillness, Banshee's Claw, Zephyr"
        ),
        Champion(
            name = "Rakan",
            cost = "3",
            ability = "Dashes to the farthest enemy, disarming units he travels through.",
            origin_id = "Ragewing",
            suggested_items = "Sunfire Cape, Protector's Vow, Zz'Rot Portal"
        ),
        Champion(
            name = "Rell",
            cost = "2",
            ability = "Tethers to an ally which protects her ally and deals damage to enemies.",
            origin_id = "Darkflight",
            suggested_items = "Protector's Vow, Sunfire Cape, Zeke's Herald"
        ),
        Champion(
            name = "Rengar",
            cost = "3",
            ability = "Leaps to the lowest armor enemy, dealing damage.",
            origin_id = "Darkflight",
            suggested_items = "Infinity Edge, Bloodthirster, Runaan's Huricane"
        ),
        Champion(
            name = "Sejuani",
            cost = "1",
            ability = "Swings her mace wide, hitting all enemies in a cone dealing damage.",
            origin_id = "Guild",
            suggested_items = "Sunfire Cape, Zz'Rot Portal, Chalice of Power"
        ),
        Champion(
            name = "Senna",
            cost = "1",
            ability = "Launches black mist toward the farthest enemy dealing damage.",
            origin_id = "Ragewing",
            suggested_items = "Thief's Gloves, Guinsoo's Rageblade, Last Whisper"
        ),
        Champion(
            name = "Seraphine",
            cost = "3",
            ability = "Grants a shield and bonus damage to allies",
            origin_id = "Lagoon",
            suggested_items = "Morellonomicon, Spear of Shojin, Rabadon's Deathcap"
        ),
        Champion(
            name = "Sett",
            cost = "1",
            ability = "Gains Armor and Magic Resist.",
            origin_id = "Ragewing",
            suggested_items = "Guinsoo's Rageblade, Quicksilver, Giant Slayer"
        ),
        Champion(
            name = "Shi Oh Yu",
            cost = "7",
            ability = "Gains damage reduction, immunity to cc, and empowering her next 3 attacks",
            origin_id = "Jade",
            suggested_items = "Bloodthirster, Titan's Resolve, Edge of Night"
        ),
        Champion(
            name = "Shyvana",
            cost = "8",
            ability = "Transforms into Dragon Form for the rest of combat.",
            origin_id = "Ragewing",
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
            origin_id = "Lagoon",
            suggested_items = "Blue Buff, Morellonomicon, Jeweled Gauntlet"
        ),
        Champion(
            name = "Soraka",
            cost = "5",
            ability = "Calls down a shower of stars that heals allies.",
            origin_id = "Jade",
            suggested_items = "Spear of Shojin, Chalice of Power, Statikk Shiv"
        ),
        Champion(
            name = "Syfen",
            cost = "7",
            ability = "Charges forward, dealing damage and knocking up enemies.",
            origin_id = "Whispers",
            suggested_items = "Bloodthirster, Titan's Resolve, Quicksilver"
        ),
        Champion(
            name = "Sylas",
            cost = "7",
            ability = "Whirls his chains, dealing damage and applying Mana-Reave.",
            origin_id = "Whispers",
            suggested_items = "Gargoyle Stoneplate, Sunfire Cape, Zz'Rot Portal"
        ),
        Champion(
            name = "Taliyah",
            cost = "1",
            ability = "Deals damage by throwing 3 seastones at her target.",
            origin_id = "Lagoon",
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
            origin_id = "Guild",
            suggested_items = "Infinity Edge, Last Whisper, Runaan's Hurricane"
        ),
        Champion(
            name = "Varus",
            cost = "3",
            ability = "Sends out a cosmic tendril that strikes the first enemy hit.",
            origin_id = "Astral",
            suggested_items = "Guinsoo's Rageblade, Giant Slayer, Runaan's Hurricane"
        ),
        Champion(
            name = "Vladimir",
            cost = "1",
            ability = "Deals damage to the target and heals himself.",
            origin_id = "Astral",
            suggested_items = "Warmog's Armor, Titan's Resolve, Redemption"
        ),
        Champion(
            name = "Volibear",
            cost = "3",
            ability = "Rages, gaining bonus Health. Every 3rd attack hits surrounding enemies",
            origin_id = "Shimmerscale",
            suggested_items = "Guinsoo's Rageblade, Bloodthirster, Quicksilver"
        ),
        Champion(
            name = "Wukong",
            cost = "1",
            ability = "Slams his target with his staff, dealing extra damage and stunning.",
            origin_id = "Jade",
            suggested_items = "Rapid Firecannon, Deathblade, Infinity Edge"
        ),
        Champion(
            name = "Xayah",
            cost = "4",
            ability = "Attacks also fire a feather which are recalled and deal damage.",
            origin_id = "Ragewing",
            suggested_items = "Guinsoo's Rageblade, Giant Slayer, Last Whisper"
        ),
        Champion(
            name = "Yasuo",
            cost = "5",
            ability = "Shields himself and dashes through his target, dealing damage.",
            origin_id = "Mirage",
            suggested_items = "Blue Buff, Bloodthirster, Titan's Resolve"
        ),
        Champion(
            name = "Yone",
            cost = "2",
            ability = "Basic attacks deal bonus damage.",
            origin_id = "Mirage",
            suggested_items = "Guinsoo's Rageblade, Quicksilver, Bloodthirster"
        ),
        Champion(
            name = "Zac",
            cost = "2",
            ability = "Explodes outward, dealing damage to enemies and healing himself.",
            origin_id = "Lagoon",
            suggested_items = "Bramble Vest, Dragon's Claw, Warmog's Armor"
        ),
        Champion(
            name = "Zeri",
            cost = "3",
            ability = "Fires a water pulse at the closest enemy, damaging all in a line.",
            origin_id = "Lagoon",
            suggested_items = "Bramble Vest, Dragon's Claw, Warmog's Armor"
        ),
        Champion(
            name = "Zippy",
            cost = "6",
            ability = "shields himself and somersaults an enemy, dealing physical damage.",
            origin_id = "Guild",
            suggested_items = "Bramble Vest, Dragon's Claw, Warmog's Armor"
        ),
        Champion(
            name = "Zoe",
            cost = "5",
            ability = "Borrows spells from other dimensions during combat and cast them as if they were her own.",
            origin_id = "Shimmerscale",
            suggested_items = ""
        ),
        Champion(
            name = "Zyra",
            cost = "2",
            ability = "Summons vines, dealing magic damage and stunning enemies.",
            suggested_items = "Bramble Vest, Dragon's Claw, Warmog's Armor"
        )
    ]



    db.session.add_all(champs)
    db.session.add_all(items)
    db.session.commit()

    tbs = [
        Teamboard(
            title = "Lagoon",
            description = "Lagoon Team",
    
            user_id = "admin"
        )
    ]
    db.session.add_all(tbs)

    tb = tbs[0]
    tb.champions.append(champs[0])
    tb.champions.append(champs[1])
    # tb.champions.append(champs[46])
    # tb.champions.append(champs[56])
    # tb.champions.append(champs[37])

    assassin = traits[0]
    assassin.champions.append(champs[6])
    assassin.champions.append(champs[24])
    assassin.champions.append(champs[28])
    assassin.champions.append(champs[31])

    bard = traits[1]
    bard.champions.append(champs[3])

    bruiser = traits[2]
    bruiser.champions.append(champs[13])
    bruiser.champions.append(champs[21])
    bruiser.champions.append(champs[26])
    bruiser.champions.append(champs[38])
    bruiser.champions.append(champs[41])
    bruiser.champions.append(champs[42])

    cannoneer = traits[3]
    cannoneer.champions.append(champs[1])
    cannoneer.champions.append(champs[10])
    cannoneer.champions.append(champs[33])
    cannoneer.champions.append(champs[54])

    cavalier = traits[4]
    cavalier.champions.append(champs[11])
    cavalier.champions.append(champs[19])
    cavalier.champions.append(champs[25])
    cavalier.champions.append(champs[30])
    cavalier.champions.append(champs[32])

    dragonmancer = traits[5]
    dragonmancer.champions.append(champs[15])
    dragonmancer.champions.append(champs[16])
    dragonmancer.champions.append(champs[17])
    dragonmancer.champions.append(champs[35])
    dragonmancer.champions.append(champs[48])
    dragonmancer.champions.append(champs[51])

    evoker = traits[6]
    evoker.champions.append(champs[2])
    evoker.champions.append(champs[34])
    evoker.champions.append(champs[57])

    guardian = traits[7]
    guardian.champions.append(champs[4])
    guardian.champions.append(champs[12])
    guardian.champions.append(champs[18])
    guardian.champions.append(champs[22])
    guardian.champions.append(champs[29])
    guardian.champions.append(champs[53])

    mage = traits[8]
    mage.champions.append(champs[19])
    mage.champions.append(champs[20])
    mage.champions.append(champs[39])
    mage.champions.append(champs[42])
    mage.champions.append(champs[43])
    mage.champions.append(champs[47])
    mage.champions.append(champs[56])

    monolith = traits[9]
    monolith.champions.append(champs[44])

    mystic = traits[10]
    mystic.champions.append(champs[3])
    mystic.champions.append(champs[29])
    mystic.champions.append(champs[34])
    mystic.champions.append(champs[36])

    shapeshifter = traits[11]
    shapeshifter.champions.append(champs[9])
    shapeshifter.champions.append(champs[14])
    shapeshifter.champions.append(champs[23])
    shapeshifter.champions.append(champs[37])

    spellthief = traits[12]
    spellthief.champions.append(champs[56])

    starcaller = traits[13]
    starcaller.champions.append(champs[40])

    swiftshot = traits[14]
    swiftshot.champions.append(champs[8])
    swiftshot.champions.append(champs[45])
    swiftshot.champions.append(champs[46])
    swiftshot.champions.append(champs[50])

    warrior = traits[15]
    warrior.champions.append(champs[26])
    warrior.champions.append(champs[27])
    warrior.champions.append(champs[49])
    warrior.champions.append(champs[51])
    warrior.champions.append(champs[52])


    archa = items[0]
    archa.champions.append(champs[5])
    archa.champions.append(champs[56])
    archa.champions.append(champs[57])

    Ao_shin = champs[0]
    Ao_shin.items.append(items[0])
    Ao_shin.items.append(items[-9])


    Braum = champs[4]
    Braum.items.append(items[4])
    Braum.items.append(items[-7])

    Aphelios = champs[1]
    Aphelios.items.append(items[-3])
    db.session.commit()
    print('Tables Seeded')

# @db_commands.cli.command('team')
# def seed_tb():
#     tbs = [
#         Teamboard(
#             title = "Lagoon",
#             description = "Lagoon Team",
    
#             user_id = "admin"
#         )
#     ]
#     db.session.add_all(tbs)
#     db.session.commit()
#     print('tb Seeded')


# @db.commands.cli.command('boards')
# def seed_boardchamps():
#     tbc = [
        
#     ]