from Logging import Logging


class FileLogging(Logging):
    file_name: str
    
    def __init__(self, file_name: str):
        self.file_name = file_name
        
        
    def log(self, msg: str) -> None: 
        with open(self.file_name, 'a') as file:
            file.write(f"\n{msg}")