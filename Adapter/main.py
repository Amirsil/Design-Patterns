from Cat import Cat
from CatToSoundMaker import CatToSoundMaker
from Dog import Dog
from DogToSoundMaker import DogToSoundMaker
from SoundMaker import SoundMaker
from typing import List


def main() -> None:
    cat: Cat = Cat()
    dog: Dog = Dog()
    
    soundMakers: List[SoundMaker] = [DogToSoundMaker(dog), CatToSoundMaker(cat)]
    
    for soundMaker in soundMakers:
        soundMaker.sound() 
    

if __name__ == "__main__":
    main()