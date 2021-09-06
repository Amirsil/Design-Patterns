from Logging import Logging


class ConsoleLogging(Logging):
    def __init__(self):
        pass
    
    def log(self, msg: str) -> None: 
        print(msg)