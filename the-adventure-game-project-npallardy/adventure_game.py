# Designed by Nick Pallardy
# You are welcome to write and include any other Python files you want or need
# however your game must be started by calling the main function in this file.
from random import random
from random import randrange
from AdventurerModule import Adventurer
from MonsterModule import Monster
from HealthBars import HealthBars
import time



def getInputs():
    PrintOpeningTheme()
    PlayerName =input("You have been warned adventurer.  Should you wish to proceed, enter your name: ")
    PlayerClass = GetPlayerClass()
    time.sleep(2)
    return PlayerName, PlayerClass
 
 
def PrintOpeningTheme():
    print("""Far below the earth’s crust lies a hoard of wealth and powerful artifacts.
The manner of wealth that can only be attained through torture, murder, and an insatiable appetite for power.
Therein lies a most ancient and powerful artifact… the Scepter of Unsight. An artifact of immense
power that grants the possessor dominion over light itself.  Wielded in life by a tyrannical and bloodthirsty savage,
this artifact now rests in the caverns where his stronghold lay.  Some say he never truly died...
and that he haunts the stronghold to this day, eager to greet the next fool to step into his domain...

Welcome to Tieran's Folly

In this dark pit there is but one way to reach the scepter.  You must face 10 portals and the nightmares they conceal.
Be it chance, skill, or cunning...be ready...\n""")


def GetPlayerClass():
    ClassSequence = ["Rogue","Barbarian","Knight"]
    print("""\nIn this realm you have but three paths.  You may enter as the wily Rogue renown for cunning and stealth.  You might choose
the path of the Barbarian hoping strength and courage will see you through.  Lastly, you may choose the Knight and rely upon your deadly skill.""")
    while True:
        ClassReference =str(input("Enter (1) for {0}, (2) for {1}, and (3) for {2}: ".format(ClassSequence[0],ClassSequence[1],ClassSequence[2])))
        if ClassReference == '1' or ClassReference =='2' or ClassReference == '3':
            break
        print("Error - enter 1, 2, or 3.")
    PlayerClass = ClassSequence[int(ClassReference)-1]
    print("\nWelcome {0}\n".format(PlayerClass))
    return PlayerClass

def getSkillPoints(MainCharacter):
    SkillPoints = 10
    print("You have 10 Skill Points to use on your adventurer as you see fit.  Choose wisely...")
    print("You may use the points to increase your character's Vitality, Strength, or Skill")
    Vitality = int(input("Points for Vitality (increases health): "))
    if Vitality > SkillPoints:
        while Vitality > SkillPoints:
            Vitality = int(input("Error. Too many skill points used.  Enter Points for Vitality: "))
    SkillPoints = SkillPoints - Vitality
    
    if SkillPoints > 0:
        Strength = int(input("Points for Strength (increases damage): "))
        if Strength > SkillPoints:
            while Strength > SkillPoints:
                Strength = int(input("Error. Too many skill points used.  Enter Points for Strength: "))  
    SkillPoints = SkillPoints - Strength
    
    if SkillPoints > 0:
        Skill = int(input("Points for Skill (increases dodge/critical chance): "))
        if Skill > SkillPoints:
            while Skill > SkillPoints:
                Skill = int(input("Error. Too many skill points used.  Enter Points for Skill: "))
        Skill = SkillPoints
            
    # add skill points to character
    MainCharacter.AddSkillPoints(Vitality, Strength, Skill)
    
def EnterPortalChoice():
    while True:
        EnterChoice = str(input("\nThe portal outline lies before you.  An oval void outlined in flicker purple flames that dance off \n the surrounding rock.  Do you wish to enter? (y/n) : "))
        # if choice is yes then break and return yes
        if EnterChoice.casefold() == 'y'.casefold():
            EnterChoice = 'y'
            break
        
        # if choice is no then do a chicken test and if they still want to leave then return no
        elif EnterChoice.casefold() == 'n'.casefold():
            ChickenTest = input("Are you certain you wish to end your adventure? (y/n) : ")
            if ChickenTest.casefold() == 'y'.casefold():
                EnterChoice = 'n'
                break
        else:
            print("Error - enter 'y' or 'n'")
    return EnterChoice

def getPortalOutcome():
    # get a random number and use that to determine one of the three possible outcomes
    OutcomeChance = float(random())
    if OutcomeChance < .33:
        PortalDestination = "Riddle"
    elif OutcomeChance >= .33 and OutcomeChance < .66:
        PortalDestination = "Gold"
    else:
        PortalDestination = "Enemy"
    return PortalDestination

def TakePlayerToPortalOutcome(MainCharacter, PortalDestination, MonsterList):
    # take the portal outcome (riddle, gold, enemy) and direct it to the appropriate sequence.
    if PortalDestination == "Riddle":
        ExecuteRiddle(MainCharacter)     
    elif PortalDestination == "Gold":
        getRandomGoldAmt(MainCharacter)
    else:
        ExecuteFight(MainCharacter, MonsterList)

def generateMonsters():
    MonsterList = []
    MonsterList.append(Monster('Golem'))
    MonsterList.append(Monster('Wisp'))
    MonsterList.append(Monster('Skeleton'))
    MonsterList.append(Monster('Lich'))
    return MonsterList
    
def getRandomEnemy(MonsterList):
    NumberOfMonsters = len(MonsterList)
    MonsterNumberinSequence = randrange(0,NumberOfMonsters)
    RandomMonster = MonsterList[MonsterNumberinSequence]
    return RandomMonster

def getRandomGoldAmt(MainCharacter):
    GoldAmt = randrange(10,60,10)
    intro = "\nAs you exit the portal you see a pile of glittering coins reflecting the reddish orange glow of the torchlight\n"
    print(intro)
    time.sleep(1.5)
    print("Wow! You receive {0} Gold Coins!".format(GoldAmt))
    MainCharacter.addGold( GoldAmt)

def getRandomRiddle():
    RiddleNumb = randrange(1,6)
    Riddleintro = "\nAs you enter the room you see words etched upon the ground.  One word to save, one word to suffer.  Answer thy riddle wisely...\n"
    print(Riddleintro)
    Riddle, RiddleAnswer = getRiddle(RiddleNumb)
    time.sleep(3)
    print(Riddle)
    return RiddleAnswer

def getRiddle(RiddleNumb):
    if RiddleNumb == 1:
        Riddle = "What is greater than God,\nmore evil than the devil,\nthe poor have it\nthe rich need it,\nand if you eat it you will die?"
        RiddleAnswer = "nothing"
    elif RiddleNumb == 2:
        Riddle = "If you have me, you want to share me,\nif you share me, you haven't got me.\nWhat am I?"
        RiddleAnswer = "secret"
    elif RiddleNumb == 3:
        Riddle = "What can you catch but not throw?"
        RiddleAnswer = "cold"
    elif RiddleNumb == 4:
        Riddle = "This thing all things devour:\nBirds, beasts, trees, flowers;\nGnaws iron, bites steel;\nGrinds hard stones to meal;\nSlays king, ruins town,\nAnd beats high mountain down.\nWhat am I?"
        RiddleAnswer = "time"
    else:
        Riddle = "Alive without breath\nAs cold as death;\nNever thirsty, ever drinking,\nAll in mail never clinking.\nWhat am I?"
        RiddleAnswer = "fish"
    return Riddle, RiddleAnswer

def ExecuteRiddle(MainCharacter):
    RiddleAnswer = getRandomRiddle()
    PlayerAnswer = str(input("\nEnter Your One Word Answer: "))
    if RiddleAnswer.casefold() != PlayerAnswer.casefold():
        RiddleDamage = randrange(1,16)
        print("Fools shall not be suffered. Flames roar at you from all sides and you sustain {0} damage.".format(RiddleDamage))
        MainCharacter.lowerHealth(RiddleDamage)
        if MainCharacter.getHealth() < 0:
            MainCharacter.setHealth(0)
    else:
        time.sleep(1.5)
        print("Well reasoned...you may continue your quest")

def ExecuteFight(MainCharacter, MonsterList):
    RandomMonster = getRandomEnemy(MonsterList)
    RandomMonster.getIntro()
    time.sleep(7)
    Winner = FightUntilFinish(MainCharacter,RandomMonster)
    time.sleep(1)
    print("{0} has won the battle".format(Winner))
    
def FightUntilFinish(MainCharacter,RandomMonster):
    #create the health bars for the fighters
    HealthScreen = HealthBars(MainCharacter, RandomMonster)
    while True:
        # get the damage the player will deal
        PlayerDamageDealt = getPlayerAttack(MainCharacter, RandomMonster)

        time.sleep(2)
        print("\n{0} the {1} launches an attack and deals the {2} {3} damage".format(MainCharacter.getName(),MainCharacter.getClass(),RandomMonster.getName(), PlayerDamageDealt))
        # display damage taken by the opponent
        HealthScreen.displayDamage(PlayerDamageDealt, RandomMonster.getName())
        
        # if monster health is at or below 0; set health to 0, display health as 0, restore the monster to fight again, and display the fight winner
        if RandomMonster.getHealth() <= 0:
            RandomMonster.setHealth(0)
            HealthScreen.changeHealthBars(MainCharacter, RandomMonster)
            time.sleep(1)
            RandomMonster.restoreMonsterFullHealth()
            Winner = MainCharacter.getName()
            HealthScreen.displayWinner(Winner)
            time.sleep(1)
            HealthScreen.closeFightScreen()
            MainCharacter.addKill()
            
            break
        # update health bars with damage taken
        HealthScreen.changeHealthBars(MainCharacter, RandomMonster)
        EnemyDamageDealt = getEnemyAttack(MainCharacter, RandomMonster)
        
        time.sleep(2)
        print("\nThe {0} {1} and deals {2} {3} damage".format(RandomMonster.getName(),RandomMonster.getAttackMethod(),MainCharacter.getName(), EnemyDamageDealt))
        # display damage taken by the opponent
        HealthScreen.displayDamage(EnemyDamageDealt, MainCharacter.getName())
        
        # if main character healht at or below 0; set health to 0, display health as 0, display the fight winner
        if MainCharacter.getHealth() <= 0:
            MainCharacter.setHealth(0)
            HealthScreen.changeHealthBars(MainCharacter, RandomMonster)
            time.sleep(1)
            Winner = RandomMonster.getName()
            HealthScreen.displayWinner(Winner)
            time.sleep(2)
            HealthScreen.closeFightScreen()
            break
        
        # update health bars with damage taken
        HealthScreen.changeHealthBars(MainCharacter, RandomMonster)
        
    return Winner
    

def getPlayerAttack(MainCharacter, RandomMonster):
    ChanceToCrit = random()
    if RandomMonster.getDodge() == True:
        DamageDealt = 0
    else:
        DamageDealt = MainCharacter.getDamage()
        RandomMonster.lowerHealth(DamageDealt)
    return DamageDealt

def getEnemyAttack(MainCharacter, RandomMonster):
    if MainCharacter.getDodge() == True:
        DamageDealt = 0
    else:
        DamageDealt = RandomMonster.getDamage()
        MainCharacter.lowerHealth(DamageDealt)
    return DamageDealt



def getWinSequence(PlayerName, PlayerClass, GoldAmt, PlayerHealth, PlayerKills):
    print("\nUpon appearing you immediately notice that this chamber is different.")
    print("A towering pile of riches stands before complete with rubies, gold, and glittering weapons.")
    print("As your gaze moves upwards you see a pedestal and upon it lies that which you have been seeking")
    print("The Scepter of Unsight and the power that comes with it are now yours.  Wield it well.")
    time.sleep(3)
    print("\nCongratulations on conquering Tieran's Folly.")
    time.sleep(2)
    print("Below are your final statistics")
    print("Player Name: {0}, {1}".format(PlayerName, PlayerClass))
    print("Health: {0}".format(PlayerHealth))
    print("Gold: {0}".format(GoldAmt))
    print("Enemies defeated: {0}".format(PlayerKills))

def getLoseSequence(PlayerName, PlayerClass, GoldAmt, PlayerHealth, PlayerKills):
    print("\nThe scene slowly fades to black as {0}'s eyelids shut for the final time.".format(PlayerName))
    time.sleep(1)
    print("\nTieran's folly claims yet another soul.")
    time.sleep(2)
    print("\nGAME OVER.")
    time.sleep(1)
    print("Below are your final statistics")
    print("Player Name: {0}, {1}".format(PlayerName, PlayerClass))
    print("Health: {0}".format(PlayerHealth))
    print("Gold: {0}".format(GoldAmt))
    print("Enemies defeated: {0}".format(PlayerKills))    
    
def getQuitSequence(PlayerName, PlayerClass, GoldAmt, PlayerHealth, PlayerKills):
    print("\nSo your adventure ends.  Tieran's folly shall wait until you have the courage to try again")
    time.sleep(1)
    print("\nGAME OVER.")
    time.sleep(1)
    print("Below are your final statistics")
    print("Player Name: {0}, {1}".format(PlayerName, PlayerClass))
    print("Health: {0}".format(PlayerHealth))
    print("Gold: {0}".format(GoldAmt))
    print("Enemies defeated: {0}".format(PlayerKills)) 

def main():
    PlayerName, PlayerClass = getInputs()
    MainCharacter = Adventurer(PlayerName, PlayerClass)
    getSkillPoints(MainCharacter)
    MonsterList = []
    MonsterList = generateMonsters()
    for PortalCounter in range(10):
        EnterChoice = EnterPortalChoice()
        if EnterChoice == 'n':
            getQuitSequence(MainCharacter.getName(), MainCharacter.getClass(), MainCharacter.getGold(), MainCharacter.getHealth(), MainCharacter.getKills())
            break
        elif EnterChoice == 'y':
            if PortalCounter == 9:
                getWinSequence(MainCharacter.getName(), MainCharacter.getClass(), MainCharacter.getGold(), MainCharacter.getHealth(), MainCharacter.getKills())            
            else:
                PortalDestination = getPortalOutcome()
                TakePlayerToPortalOutcome(MainCharacter, PortalDestination, MonsterList)
                time.sleep(.5)
                if MainCharacter.getHealth() == 0:
                    getLoseSequence(MainCharacter.getName(), MainCharacter.getClass(), MainCharacter.getGold(), MainCharacter.getHealth(), MainCharacter.getKills())
                    break
                else:
                    print("\n{0} has {1} health and {2} gold.".format(MainCharacter.getName(),MainCharacter.getHealth(), MainCharacter.getGold()))
                    time.sleep(2)
    
main()