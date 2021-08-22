from Logging import Logging


class Logger():
    strategy: Logging
    
    def __init__(self, strategy: Logging):
        self.strategy: Logging = strategy
        
        
    def log(self, msg: str) -> None:
        self.strategy.log(msg)
        
    
    def changeStrategy(self, strategy: Logging) -> None:
        self.strategy = strategy