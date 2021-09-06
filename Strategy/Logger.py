from Logging import Logging


class Logger():
    loggingMethod: Logging
    
    def __init__(self, strategy: Logging):
        self.loggingMethod: Logging = strategy
        
        
    def log(self, msg: str) -> None:
        self.loggingMethod.log(msg)
        
    
    def changeLoggingMethod(self, strategy: Logging) -> None:
        self.loggingMethod = strategy