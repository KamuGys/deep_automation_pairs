print("Lecture_7")
class HumanIntal:
    eyes: int = 2
    hands: int = 2
    legs: int = 2
    hair_color: str ="Brown"
    name: str ="Karl"


    def blink(self):
        name='netvova'
        print(f"{name} blinked")
    
    def walk(self):
        print(f"{self.name} fig vam")

human1=HumanIntal()
human1.blink()
human1.walk()
#if __name__= '__main__':



def __init__(self, name:str, legs: int):
    self.name = name
    self.legs = legs
    self.blink()
human2 =HumanIntal(name='notyou')
human2.blink()


class smart_hum(HumanIntal):
    glases: int =1

smart_hum1=smart_hum()
smart_hum1.blink()
print(smart_hum1)