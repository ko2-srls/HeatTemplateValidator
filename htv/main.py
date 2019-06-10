# System imports
import sys
from .install import install
from .shadow import shadow
from .validate import validate_template


def main_entry():
    print("entry")
    print(sys.argv)
    if len(sys.argv) > 1:
        # It saves the arguments in a list
        arguments = sys.argv[1:]
        for arg in arguments:
            if "--install" in arg or "-i" in arg:
                install()
            elif "--shadow" in arg or "-s" in arg:
                shadow()
            else:
                print("No args")
                #validate_template()
    else:
        print("No args")
