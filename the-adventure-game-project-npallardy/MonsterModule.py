from random import random

class Monster:
    def __init__( self, MonsterName ):
        self.MonsterName = MonsterName
        
        if MonsterName == "Golem":
            self.intro = """\nAs you step through the portal you glance around to see a perfectly circular chamber lit evenly by the orange glow of torchlight.
As you step forward you feel the ground tremble beneath your feet and dust fall from the ceiling.
The sound of splitting rock greets your ears as a humanoid creature composed entirely of rock pulls itself from the ground.
The Golem stands and a roar of challenge emanates from its immense chest as it rushes you."""
            self.MonsterHealth = 40
            self.MonsterStartingHealth = 40
            self.attackDamage = 10
            self.criticalPct = float(.01)
            self.dodgePct = float(.005)
            self.attackMethod = "Swings its fist"
        elif MonsterName == "Skeleton":
            self.intro = """\nAs you step through the portal you observe an eerily dark chamber lit by a single purple lantern.
As you step forward you hear the grate of bone on bone as Skeleton clad in a rusted breastplate steps forth.
Your ears ache from the sound of the iron swordtip that drags the ground in its hands and is slowly raised to attack.
The Skeleton bones become a cacaphony of rattles as it bears down on you eager to begin."""
            self.MonsterHealth = 25
            self.MonsterStartingHealth = 25
            self.attackDamage = 8
            self.criticalPct = float(.02)
            self.dodgePct = float(.03)
            self.attackMethod = "Slashes its sword"
        elif MonsterName == "Wisp":
            self.intro = """\nAs you step through the portal you find a simple chamber illuminated by a drifting and slowly pulsing yellow and green light.
The light begins pulsing rapidly and it ceases its movement at the sound of the portal.
Upon closer observation you see that the light is that of a Wisp and its light takes on a blood-red hue.
A small discharge of energy is your only warning as the Wisp zips toward you ready for its meal."""
            self.MonsterHealth = 20
            self.MonsterStartingHealth = 20
            self.attackDamage = 5
            self.criticalPct = float(.03)
            self.dodgePct = float(.10)
            self.attackMethod = "Sucks away your lifeforce"
        else:
            self.intro = """\nAs you step through the portal you are greeted to the sight of a decrepit stone tomb whose slab lays forgotten on the floor.
Suddenly, a high pitched scream emanates from the tomb and you see a decaying hand grasp the tomb from within and a tattered figure slowly rise.
A sudden cold surrounds you as the Lich climbs forth and begins the mirthless laugh of those damned for all eternity.
Dark energy pools around its hands and seems to flow and drip like water as the Lich advances."""
            self.MonsterHealth = 50
            self.MonsterStartingHealth = 50
            self.attackDamage = 13
            self.criticalPct = float(.03)
            self.dodgePct = float(.10)
            self.attackMethod = "Blasts forth necrotic energy"

    def getAttackMethod(self):
        return self.attackMethod
    
    def getStartingHealth(self):
        return self.MonsterStartingHealth
    
    def getIntro(self):
        print(self.intro)
        
    def getName( self ):
        return self.MonsterName
    
    def getHealth(self):
        return self.MonsterHealth
    
    def getDamage( self ):
        ChanceToCrit = random()
        if ChanceToCrit <= self.criticalPct:
            return self.attackDamage * 3
        else:
            return self.attackDamage
        
    def getDodge(self):
        Dodge = False
        ChancetoDodge = random()
        if ChancetoDodge <= self.dodgePct:
            Dodge = True
        return Dodge
        
    def lowerHealth(self, damageAmt):
        self.MonsterHealth = self.MonsterHealth - damageAmt
        
    def setHealth(self, HealthLevel):
        self.MonsterHealth = HealthLevel
    
    def restoreMonsterFullHealth(self):
        self.MonsterHealth = self.MonsterStartingHealth

    def __repr__(self):
        return "{0}, {1} Damage,, {2} Health".format(self.MonsterName, self.attackDamage, self.MonsterHealth)