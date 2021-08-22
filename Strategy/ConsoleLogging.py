from Logging import Logging


class ConsoleLogging(Logging):
    def log(self, msg: str) -> None: 
        print(msg)