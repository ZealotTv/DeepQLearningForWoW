import math
import pyautogui as pi
from .Getst import Getst

class WoW(object):
    def __init__(self): 
        self.En1Hp = 100
        self.En2Hp = 100
        self.AllyHp = 100
        self.SelfHp = 100
        self.En1Res = 100
        self.En2Res = 100
        self.AllyRes = 100
        self.SelfRes = 100
        self.En1ALive = True
        self.En2ALive = True
        self.AllyALive = True
        self.SelfALive = True
        self.En1X = None
        self.En1Y = None 
        self.En2X = None
        self.En2Y = None 
        self.AllyX = None
        self.AllyY = None 
        self.SelfX = None
        self.SelfY = None 
        self.En1Class = None
        self.En2Class = None
        self.AllyClass = None
        self.SelfClass = None
        self.En1Race = None
        self.En2Race = None
        self.AllyRace = None
        self.SelfRace = None
        self.En1Covenant1 = None
        self.En1Covenant2 = None
        self.En2Covenant1 = None
        self.En2Covenant2 = None
        self.AllyCovenant1 = None
        self.AllyCovenant2 = None
        self.SelfCovenant1 = None
        self.SelfCovenant2 = None
        self.En1Safe1 = None
        self.En1Safe2 = None
        self.En1Safe3 = None
        self.En2Safe1 = None
        self.En2Safe2 = None
        self.En2Safe3 = None
        self.AllySafe1 = None
        self.AllySafe2 = None
        self.AllySafe3 = None
        self.SelfSafe1 = None
        self.SelfSafe2 = None
        self.SelfSafe3 = None
        self.Win = False
        self.Lose = False

    def Action(self, action):
        if action == 0:
            pi.press("w")

        elif action == 1:
            pi.press("a")

        elif action == 2:
            pi.press("s")
        
        elif action == 3:
            pi.press("d")

        elif action == 4:
            pi.press("1")

        elif action == 5:
            pi.press("2")

        elif action == 6:
            pi.press("3")
        
        elif action == 7:
            pi.press("4")

        elif action == 8:
            pi.press("5")

        elif action == 9:
            pi.press("6")

        elif action == 10:
            pi.press("7")

        elif action == 11:
            pi.press("8")

        elif action == 12:
            pi.press("9")

        elif action == 13:
            pi.press("q")
        
        elif action == 14:
            pi.press("e")

        elif action == 15:
            pi.press("r")

        elif action == 16:
            pi.press("t")

        elif action == 17:
            pi.press("f")

        elif action == 18:
            pi.press("g")
        
        elif action == 19:
            pi.press("z")

        elif action == 20:
            pi.press("x")

        elif action == 21:
            pi.press("c")

        elif action == 22:
            pi.press("v")

    def Is_Done(self):
        if not self.Win or self.Lose:
            return True
        return False
    
    def Observe(self):
        # return state
        Getst().GetEn1X
        Getst().GetEn2X
        Getst().GetEn1Y
        Getst().GetEn2Y
        Getst().GetAllayX
        Getst().GetSelfX
        Getst().GetAllayY
        Getst().GetSelfY
        ret = [0, 0, 0, 0, 0, 0, 0, 0]

        return tuple(ret)

    def CheckDeath(self):
        q = Getst().GetEn1Death
        w = Getst().GetEn2Death
        e = Getst().GetAllayDeath
        r = Getst().GetSelfDeath

        return q, w, e, r

    def CheckHP(self):
        q = Getst().GetEn1Hp
        w = Getst().GetEn2Hp
        e = Getst().GetAllayHp
        r = Getst().GetSelfHp

        return q, w, e, r

    def CheckRes(self):
        q = Getst().GetEn1Res
        w = Getst().GetEn2Res
        e = Getst().GetAllayRes
        r = Getst().GetSelfRes

        return q, w, e, r

    def CheckRace(self):
        q = Getst().GetEn1RaceAbiliti
        w = Getst().GetEn2RaceAbiliti
        e = Getst().GetAllayRaceAbiliti
        r = Getst().GetSelfRaceAbiliti

        return q, w, e, r

    def WinOrLose(self):
        q = Getst().GetInfoAboutWin

        return q

    def CheckClass(self):
        q = Getst().GetEn1Class
        w = Getst().GetEn2Class
        e = Getst().GetAllayClass
        r = Getst().GetSelfClass

        return q, w, e, r

    def CheckCovenant(self):
        q = Getst().GetEn1Covenant
        w = Getst().GetEn2Covenant
        e = Getst().GetAllayCovenant
        r = Getst().GetSelfCovenant
        a = Getst().GetEn1Covenant2
        s = Getst().GetEn2Covenant2
        d = Getst().GetAllayCovenant2
        f = Getst().GetSelfCovenant2

        return q, w, e, r, a, s, d, f

    def CheckSafeAbility(self):
        q = Getst().Get1En1SafeAbility
        w = Getst().Get2En1SafeAbility
        e = Getst().GetAllay1SafeAbility
        r = Getst().GetSelf1SafeAbility
        a = Getst().Get1En2SafeAbility
        s = Getst().Get2En2SafeAbility
        d = Getst().GetAllay2SafeAbility
        f = Getst().GetSelf2SafeAbility
        z = Getst().Get1En3SafeAbility
        x = Getst().Get2En3SafeAbility
        c = Getst().GetAllay3SafeAbility
        v = Getst().GetSelf3SafeAbility

        return q, w, e, r, a, s, d, f, z, x, c, v

    def Evaluate(self):
        reward = 0
        
        if not self.En1ALive:
            reward += 10000

        elif not self.En2ALive:
            reward += 10000

        elif not self.AllyALive:
            reward -= 5000

        elif not self.SelfALive:
            reward -=10000
        
        elif self.Win == True:
            reward += 100000000
        
        elif self.Lose == True:
            reward -= 100000000

        elif self.En1Hp < 100: # it is necessary to add the ability to change the reward with each dimension of hp
            reward += 100

        elif self.En2Hp < 100:
            reward += 100

        elif self.AllyHp < 100:
            reward -= 100

        elif self.SelfHp < 100:
            reward -= 100

        return reward
 