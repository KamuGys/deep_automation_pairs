print("task")
'''
## Описание
Cоздать BaseCharacter, BaseInAnctionCaracter, BaseFunkoPop, BaseCosplayer, BaseHuman
составить из них и из Mixin...able логику наследований
так, чтобы было минимум 6+ Mixin'ов (созданных, а не у каждого класса)
с помощью этих интерфейсов (миксинов) и наследования создать:

## Персонажи

Shrek, PussInBoots, Donkey, JackHorner

на каждого должен быть и персонаж, и фанко поп, и косплеер

итого должно быть:

BaseCharacter:
    Shrek
    PussInBoots
    Donkey
    JackHorner


    
'''

class CanSwim:
    def swim(self):
        print(f"{self.name} is swimming?!")

class CanDanse:
    def danse(self):
        print(f"{self.name} is dansing?!")

class CanDie:
    def die(self):
        print(f"{self.name} die")
    
class CanCan:
    def can(self):
        print(f"{self.name} can somuthing")
    
class CanFlight:
    def flight(self):
        print(f"{self.name} is flight?!")
    
class CanNotTalk:
    def nottalk(self):
        print(f"{self.name} nottalk, he die)")

class CanTalk:
    def talk(self):
        print(f"{self.name} talk, he live)")

class BaseCharacter(CanCan, CanDie):
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"hi, my name is {self.name}")

class BaseInAnctionCaracter(BaseCharacter, CanFlight):
    def __init__(self, name, panache):
        super().__init__(name)
        self.panache = panache
    
    def greet(self):
        print(f"hi,i am have {self.panache}")

class BaseFunkoPop(BaseCharacter, CanNotTalk):
    def __init__(self, name, material):
        super().__init__(name)
        self.material = material
    
    def greet(self):
        print(f"hi, my material is {self.material}")

class BaseCosplayer(BaseCharacter, CanSwim):
    def __init__(self, name, soul):
        super().__init__(name)
        self.soul = soul
    
    def greet(self):
        print(f"hi, my soul is {self.soul}")

class BaseHuman(BaseCharacter, CanTalk):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    
    def greet(self):
        print(f"hi, my age is {self.age}")

class Shrek(BaseInAnctionCaracter, CanTalk, CanSwim):
    def __init__(self):
        super().__init__("Shrek", "ogre power")
    
    def greet(self):
        print("i am Shrek and I talk and make something!! YEEEE")

class PussInBoots(BaseInAnctionCaracter, CanTalk):
    def __init__(self):
        super().__init__("Puss in Boots", "cat style")
    
    def greet(self):
        print("....")

class Donkey(BaseCharacter, CanTalk, CanDanse):
    def __init__(self):
        super().__init__("Donkey")
    
    def greet(self):
        print("i am Donkey and i can dance!!")

class JackHorner(BaseHuman, CanFlight):
    def __init__(self):
        super().__init__("Jack Horner", "100 years")
    
    def greet(self):
        print("he i can flight - JackHorner")

class ShrekFunkoPop(BaseFunkoPop):
    def __init__(self):
        super().__init__("Shrek", "green plastic")

class PussInBootsFunkoPop(BaseFunkoPop):
    def __init__(self):
        super().__init__("Puss in Boots", "orange plastic")

class DonkeyFunkoPop(BaseFunkoPop):
    def __init__(self):
        super().__init__("Donkey", "gray plastic")

class JackHornerFunkoPop(BaseFunkoPop):
    def __init__(self):
        super().__init__("Jack Horner", "evil plastic")

class ShrekCosplayer(BaseCosplayer):
    def __init__(self):
        super().__init__("Shrek", "green soul")

class PussInBootsCosplayer(BaseCosplayer):
    def __init__(self):
        super().__init__("Puss in Boots", "cat soul")

class DonkeyCosplayer(BaseCosplayer):
    def __init__(self):
        super().__init__("Donkey", "donkey soul")

class JackHornerCosplayer(BaseCosplayer):
    def __init__(self):
        super().__init__("Jack Horner", "dark soul")

shrek = Shrek()
shrek_pop = ShrekFunkoPop()
shrek_cos = ShrekCosplayer()

puss = PussInBoots()
puss_pop = PussInBootsFunkoPop()
puss_cos = PussInBootsCosplayer()

donkey = Donkey()
donkey_pop = DonkeyFunkoPop()
donkey_cos = DonkeyCosplayer()

jack = JackHorner()
jack_pop = JackHornerFunkoPop()
jack_cos = JackHornerCosplayer()

shrek.greet()
shrek.talk()
shrek.swim()
shrek.flight()

shrek_pop.greet()
shrek_pop.nottalk()
shrek_pop.can()

shrek_cos.greet()
shrek_cos.swim()
shrek_cos.die()

puss.greet()
puss.talk()
puss.flight()

puss_pop.greet()
puss_pop.nottalk()
puss_pop.die()

puss_cos.greet()
puss_cos.swim()
puss_cos.can()

donkey.greet()
donkey.talk()
donkey.danse()

donkey_pop.greet()
donkey_pop.nottalk()
donkey_pop.can()

donkey_cos.greet()
donkey_cos.swim()
donkey_cos.die()

jack.greet()
jack.talk()
jack.flight()

jack_pop.greet()
jack_pop.nottalk()
jack_pop.can()

jack_cos.greet()
jack_cos.swim()
jack_cos.die()