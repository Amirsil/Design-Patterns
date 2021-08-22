from utils import Interface

class Logging(Interface):
    def log(self, msg: str) -> None:
        pass