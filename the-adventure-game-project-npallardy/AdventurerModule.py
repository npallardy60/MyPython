from random import random

class Adventurer:
    def __init__( self, playerName, playerClass  ):
        self.PlayerName = playerName
        self.playerClass = playerClass
        self.playerGold = 0
        self.playerKills = 0
        
        if playerClass == "Rogue":
            self.playerHealth = 40
            self.startingHealth = 40
            self.attackDamage = 4
            self.criticalPct = float(.07)
            self.dodgePct = float(.07)
        elif playerClass == "Barbarian":
            self.playerHealth = 50
            self.startingHealth = 50
            self.attackDamage = 5
            self.criticalPct = float(.02)
            self.dodgePct = float(.02)
        else:
            self.playerHealth = 45
            self.startingHealth = 45
            self.attackDamage = 6
            self.criticalPct = float(.03)
            self.dodgePct = float(.03)
        
    def AddSkillPoints(self, Vitality, Strength, Skill):
        self.playerHealth = self.playerHealth + (Vitality * 5)
        self.startingHealth = self.playerHealth + (Vitality * 5)
        self.attackDamage = self.attackDamage + (Strength * 1)
        self.criticalPct = float(self.criticalPct + (Skill * .02))
        self.dodgePct = float(self.dodgePct + (Skill * .02))
        
    def getStartingHealth(self):
        return self.startingHealth
    
    def getName( self ):
        return self.PlayerName
    
    def getClass( self ):
        return self.playerClass
    
    def getGold( self ):
        return self.playerGold
    
    def getKills(self):
        return self.playerKills
    
    def getHealth(self):
        return self.playerHealth
    
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
    
    def addKill(self):
        self.playerKills = self.playerKills + 1
        
    def lowerHealth(self, damageAmt):
        self.playerHealth = self.playerHealth - damageAmt
        
    def setHealth(self, HealthLevel):
        self.playerHealth = HealthLevel
    
    def addGold(self, goldAmt):
        self.playerGold = self.playerGold + goldAmt
        
    def __repr__(self):
        return "{0}, {1} Damage,, {2} Health".format(self.PlayerName, self.attackDamage, self.playerHealth)   
