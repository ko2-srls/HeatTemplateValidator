# System imports
import os
from os import listdir
from os.path import isfile, join
from os_utility.miscellanea import printout
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

try:
    # It creates the list of valid files inside the valid directory
    validfiles = [f for f in listdir("./ValidYamlFiles") if isfile(join("./ValidYamlFiles", f))]
    # It creates the list of warning files inside the warning directory
    warnfiles = [f for f in listdir("./WarnYamlFiles") if isfile(join("./WarnYamlFiles", f))]
    # It creates the list of error files inside the error directory
    errfiles = [f for f in listdir("./ErrYamlFiles") if isfile(join("./ErrYamlFiles", f))]
    # It first saves a list of files of the same directory of this file main.py
    onlyfiles = [f for f in listdir(".") if isfile(join(".", f))]
    # It then saves a list of only log files out of the previous list
    onlylog = [f for f in listdir("./Log") if isfile(join("./Log", f)) and f.endswith(".log")]

    # It gets the current working directory
    dir_base = os.getcwd()
    # It defines the name of the directories (for valid files and for warning files)
    pathvalid = dir_base + "/ValidYamlFiles"
    pathwarn = dir_base + "/WarnYamlFiles"
    patherr = dir_base + "/ErrYamlFiles"
    pathfiles = dir_base + "/TemplateLocalStorage"
    pathlog = dir_base + "/Log"

    # It removes the Log files
    for logfile in onlylog:
        os.remove("{0}/{1}".format(pathlog, logfile))

    # It moves the valid file from the ValidYamlFile directory
    for validfile in validfiles:
        os.rename("{}/{}".format(pathvalid, validfile), "{}/{}".format(pathfiles, validfile))

    # It moves the warning file from the WarnYamlFile directory
    for warnfile in warnfiles:
        os.rename("{}/{}".format(pathwarn, warnfile), "{}/{}".format(pathfiles, warnfile))

    # It moves the warning file from the WarnYamlFile directory
    for errfile in errfiles:
        os.rename("{}/{}".format(patherr, errfile), "{}/{}".format(pathfiles, errfile))

    printout(">> Back to a clear testing environment, now you can execute:\n       - python validator.py\n", CYAN)

except Exception as e:
    printout(">> An error occurred:\n{}\n".format(e), CYAN)
