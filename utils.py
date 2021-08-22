class Interface:
    def __init__(self) -> None:
        raise NotImplementedError(f"{self.__class__.__name__} is an Interface and cannot be instantiated")
    