#!/usr/bin/env python3

from lib.checks import Checker
from lib.logger import Logger
from lib.system_functions import System


# Initialize Checker
checker = Checker()
# Check python version
checker.check_python_version()

# Initialize Logger
logger = Logger()

# Initialize System Functions
system = System()


# Start the bot
if __name__ == "__main__":
    logger.log()
    system.quit()
