from Dog import Dog
from SoundMaker import SoundMaker


class DogToSoundMaker(SoundMaker):
    adapted: Dog
    
    def __init__(self, dog: Dog) -> None:
        self.adapted = dog
        
    def sound(self) -> None:
        self.adapted.bark()