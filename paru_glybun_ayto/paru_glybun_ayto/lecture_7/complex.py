from abc import abstractclassmethod

print('mir')
class dak:
    vings: int =2
    beak: bool =True

    @abstractclassmethod
    def make_noise(self, volume_do: int) -> None:
        raise NotImplementedError
        

class Duck(dak):
    ...

d=Duck
d.make_noise(12)