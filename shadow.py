# Encryption utilities imports
from cryptography.fernet import Fernet
# System imports
from os.path import isfile, join
from os import listdir
import os
# Crontab generator import
from os_utility.crongen import cron_generator
from os_utility.miscellanea import printout
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

# It creates an empty list
crontabs = []
# It gets the base directory
dir_base = os.getcwd()
# It deletes list_cron.txt
file = open('./list_cron.txt', 'w')
file.write("")
file.close()

############################################
#              Encryption key              #
############################################
# It gets the encryption key
file = open('./config/key.key', 'rb')
e_key = file.read()
file.close()

# It saves all the .sh files corresponding to the admin-openrc.sh files
onlyfiles = [f for f in listdir("./rc_files") if isfile(join("./rc_files", f))]
onlysh = [f for f in onlyfiles if f.endswith(".sh")]

############################################
#       Password encryption and save       #
############################################
# It opens every openrc.sh file and insert the encrypted password in it
for shfile in onlysh:
    # It gets the openstack password in the form of a string, encodes it and encrypts it.
    openstack_password = input(">> Enter the Openstack password for the file {}: ".format(shfile))
    passwd = openstack_password.encode()
    f = Fernet(e_key)
    encrypted = f.encrypt(passwd)
    # It creates the variable to insert
    password_line = "export OS_PASSWORD={}".format(encrypted)
    # It opens the openrc.sh file and change the PASSWORD line with the new encrypted password
    with open("./rc_files/{}".format(shfile), 'r+') as F:
        lines = F.readlines()
        F.seek(0)
        for line in lines:
            # If 'OS_PASSWORD' is not in the line, it re-writes the line to the file
            if "export OS_PASSWORD=" not in line:
                F.write(line)
        # At the end it appends the new line with the saved password
        F.write("\n{}".format(password_line))
    # It generates the crontab for each openrc file and for each password
    crontab = '*/10 * * * * source {0}/venv/bin/activate && python {0}/validator.py --password="{1}" --openrc="{2}"'.format(dir_base, encrypted, shfile)
    # It adds the crontab to the list 'crontabs'
    crontabs.append(crontab)

############################################
#            Crontabs generator            #
############################################
# It calls the cron_generator function to save the crontabs from the "crontabs" list into the list_cron.txt file
cron_generator(crontabs)
printout(""">> Passwords have been correctly saved\n""", CYAN)


