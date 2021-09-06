from ConsoleLogging import ConsoleLogging
from FileLogging import FileLogging
from Logger import Logger

logger: Logger = Logger(FileLogging("foo.txt"))

logger.log("hi")

logger.changeLoggingMethod(ConsoleLogging())

logger.log("foo")