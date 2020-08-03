from graphics import *
from AdventurerModule import Adventurer
from MonsterModule import Monster
import time


class HealthBars:
    def __init__( self, Player, Monster):
        self.windowWidth = 500
        self.windowHeight = 550
        self.HealthBarHeight = 400
        self.PlayerStartingHealth = Player.getStartingHealth()
        self.MonsterStartingHealth = Monster.getStartingHealth()
        self.BottomTextGap = 50
        
        
        self.win = GraphWin("Fight Sequence", self.windowWidth, self.windowHeight)
        self.win.setBackground('dark grey')
        
        # Draw Outline for the Player's health bar
        barBottomBorder = self.windowHeight - 50
        self.HealthBarWidth = self.windowWidth / 5
        self.lrPlayerHealthBarPoint = Point(self.HealthBarWidth * 2, barBottomBorder)
        ulPlayerHealthBarPoint = Point(self.HealthBarWidth, self.windowHeight - self.HealthBarHeight - self.BottomTextGap)
        PlayerHealthBarOutline = Rectangle(ulPlayerHealthBarPoint,self.lrPlayerHealthBarPoint)
        PlayerHealthBarOutline.draw(self.win)
        
        #Draw outline for the Monster's health bar
        self.lrMonsterHealthBarPoint = Point(self.HealthBarWidth * 4, barBottomBorder)
        ulMonsterHealthBarPoint = Point(self.HealthBarWidth * 3, self.windowHeight - self.HealthBarHeight - self.BottomTextGap)
        MonsterHealthBarOutline = Rectangle(self.lrMonsterHealthBarPoint,ulMonsterHealthBarPoint)
        MonsterHealthBarOutline.draw(self.win)
        
        #Write the player and Monster names underneath the health bars
        textHeight = self.windowHeight - 25
        PlayerTextPoint = Point(int(self.HealthBarWidth * 1.5),textHeight)
        PlayerText = Text(PlayerTextPoint, Player.getName())
        PlayerText.setStyle('bold')
        PlayerText.setTextColor('green')
        PlayerText.draw(self.win)
        
        MonsterTextPoint = Point(int(self.HealthBarWidth * 3.5),textHeight)
        MonsterText = Text(MonsterTextPoint, Monster.getName())
        MonsterText.setStyle('bold')
        MonsterText.setTextColor('red')
        MonsterText.draw(self.win)
        
        #add the fill level to the bars
        self.PlayerHealthPct = Player.getHealth() / self.PlayerStartingHealth
        self.PlayerHealthFillHeight =round(self.BottomTextGap + self.PlayerHealthPct * self.HealthBarHeight)
        ulPlayerFillPoint = Point(self.HealthBarWidth, self.windowHeight - self.PlayerHealthFillHeight)
        self.PlayerHealthFillBar = Rectangle(self.lrPlayerHealthBarPoint, ulPlayerFillPoint)
        self.FormatAndColorBar(self.PlayerHealthPct,self.PlayerHealthFillBar)
        self.PlayerHealthFillBar.draw(self.win)
        
        self.MonsterHealthPct = Monster.getHealth() / self.MonsterStartingHealth
        self.MonsterHealthFillHeight =round(self.BottomTextGap + self.MonsterHealthPct * self.HealthBarHeight)
        ulMonsterFillPoint = Point(self.HealthBarWidth * 3, self.windowHeight - self.MonsterHealthFillHeight)
        self.MonsterHealthFillBar = Rectangle(self.lrMonsterHealthBarPoint, ulMonsterFillPoint)
        self.FormatAndColorBar(self.MonsterHealthPct,self.MonsterHealthFillBar)
        self.MonsterHealthFillBar.draw(self.win)
        
        #Create Battle Message
        self.BattleMessage = ""
        self.BattleTextPoint = Point(self.windowWidth / 2, 50)
        self.BattleText = Text( self.BattleTextPoint,self.BattleMessage)
        self.BattleText.draw(self.win)
        
    def FormatAndColorBar(self, HealthPct, RectObject):
        RectObject.setWidth(0)
        if HealthPct > .5:
            RectObject.setFill('green')
        elif HealthPct > .25:
            RectObject.setFill('yellow')
        else:
            RectObject.setFill('red')
                 
    def changeHealthBars(self, Player, Monster):
        self.PlayerHealthFillBar.undraw()
        self.PlayerHealthPct = Player.getHealth() / self.PlayerStartingHealth
        self.PlayerHealthFillHeight =round(self.BottomTextGap + self.PlayerHealthPct * self.HealthBarHeight)
        ulPlayerFillPoint = Point(self.HealthBarWidth, self.windowHeight - self.PlayerHealthFillHeight)
        self.PlayerHealthFillBar = Rectangle(self.lrPlayerHealthBarPoint, ulPlayerFillPoint)
        self.FormatAndColorBar(self.PlayerHealthPct,self.PlayerHealthFillBar)
        self.PlayerHealthFillBar.draw(self.win)
        
        self.MonsterHealthFillBar.undraw()
        self.MonsterHealthPct = Monster.getHealth() / self.MonsterStartingHealth
        self.MonsterHealthFillHeight =round(self.BottomTextGap + self.MonsterHealthPct * self.HealthBarHeight)
        ulMonsterFillPoint = Point(self.HealthBarWidth * 3, self.windowHeight - self.MonsterHealthFillHeight)
        self.MonsterHealthFillBar = Rectangle(self.lrMonsterHealthBarPoint, ulMonsterFillPoint)
        self.FormatAndColorBar(self.MonsterHealthPct,self.MonsterHealthFillBar)
        self.MonsterHealthFillBar.draw(self.win)
        
    def displayDamage(self, damageAmt, target):
        BattleMessage = "{0} takes {1} damage".format(target, damageAmt)
        self.BattleText.setText(BattleMessage )
        #self.BattleTextPoint = Point(self.windowWidth / 2, 50)
        #self.BattleText = Text( self.BattleTextPoint,self.BattleMessage)
        #self.BattleText.draw(self.win)        
        
    def displayWinner(self, winner):
        WinnerMessage = "{} has won the battle!".format(winner)
        #WinnerTextPoint = Point(self.windowWidth / 2, 50)
        #self.WinnerText = Text( WinnerTextPoint,WinnerMessage)
        #self.WinnerText.draw(self.win)
        self.BattleText.setText(WinnerMessage )
        
    def closeFightScreen(self):
        self.win.close()
        

    
    
    