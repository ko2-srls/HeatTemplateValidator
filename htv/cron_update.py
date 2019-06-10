# Utilities imports
from htv.os_utility.crongen import direct_cron_gen
from htv.os_utility.miscellanea import printout
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

#####################
#  Update crontabs  #
#####################
# It just calls the function dorect_cron_gen from its package
direct_cron_gen()
printout(">> Crontabs have been correctly updated\n", CYAN)
