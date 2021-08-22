from Cat import Cat
from SoundMaker import SoundMaker


class CatToSoundMaker(SoundMaker):
    adapted: Cat
    
    def __init__(self, cat: Cat) -> None:
        self.adapted = cat
        
    def sound(self) -> None:
        self.adapted.meow()