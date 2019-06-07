# System imports
import os
from os import listdir
from os.path import isfile, join
import traceback
import datetime
# Yaml imports
import yaml
from yamllint.config import YamlLintConfig
from yamllint import linter
# Utilities imports
from os_utility.os_parser import get_images, get_flavors, get_secgroups, get_networks, get_ports, get_keypairs, \
    get_volumes
from os_utility.os_verify import verify_images, verify_secgroups, verify_flavors, verify_networks, verify_ports, \
    verify_keypairs, verify_volumes
from os_utility.miscellanea import printout
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

##################################################################
#                        Variables setting                       #
##################################################################
# It sets the date to the current day, the log will refer to this date when the script will be executed
today = (str(datetime.datetime.now())).split(" ")[0]
# It first saves a list of files of the directory "./TemplateLocalStorage"
onlyfiles = [f for f in listdir("./TemplateLocalStorage") if isfile(join("./TemplateLocalStorage", f))]
# It then saves a list of only YAML files
onlyyaml = [f for f in onlyfiles if f.endswith(".yaml")]
# If there are no yaml file the program will stop
if not onlyyaml:
    printout(""">> There are no YAML files in here! Maybe you forgot to execute:
        - python goback.py\n>>The program will exit\n""", CYAN)
# It gets the current working directory
dir_base = os.getcwd()
# It defines the name of the directories (for valid, warning, error, log files)
pathvalid = dir_base + "/ValidYamlFiles"
pathwarn = dir_base + "/WarnYamlFiles"
patherr = dir_base + "/ErrYamlFiles"
pathlog = dir_base + "/Log"
pathfiles = dir_base + "/TemplateLocalStorage"

##################################################################
#                      Validation process                        #
##################################################################
# For every YAML file in onlyyalm list it will examine the file
for yamlfile in onlyyaml:
    printout("\n\n>>> Examination of \"{}\" <<<\n".format(yamlfile), CYAN)
    # It saves the name of the file
    filename = yamlfile.split('.')[0]
    # It uses the file into the open function
    with open("{}/{}".format(pathfiles, yamlfile)) as F:
        # It reads the data and saves it into the variable 'data'
        data = F.read()
        printout(">> Trying the validity\n", CYAN)
        try:
            # It checks if the file is a valid yaml file
            doc = yaml.safe_load(data)
            print("     Valid YAML file for yaml module")
            conf = YamlLintConfig('extends: default')
            # It saves warnings if there are any
            gen = linter.run(data, conf)
            warnings = list(gen)
            # If there are warnings they will be saved into the Log file with the file name and the timestamp
            if warnings:
                with open("{0}-{1}-warning.log".format(filename, today), 'a+') as output:
                    print("     This file has one or more warnings")
                    for warning in warnings:
                        output.write("{}\n".format(str(warning)))
                    # Then the file will be moved into a directory containing all the files with warnings
                    os.rename("{}/{}".format(pathfiles, yamlfile), "{}/{}".format(pathwarn, yamlfile))
            else:
                # Otherwise the file will be moved into a directory containing all the valid YAML files
                os.rename("{}/{}".format(pathfiles, yamlfile), "{}/{}".format(pathvalid, yamlfile))
                print("     No error for yaml lint too")

            """Files are valid (even if with some warnings), so it will save items (such as the image, flavor etc) 
            in a specific list and then try to check for their existence into the openstack server"""
            printout(">> Analyzing the template structure and items existence:\n", CYAN)
            #################################################
            #    Search for items into openstack server     #
            #################################################
            # Glance: image
            try:
                images = get_images(doc)
            except Exception as e:
                print(e)
            # If the images list is populated it will try to look for the items inside the openstack items
            if images:
                try:
                    verify_images(images, doc, yamlfile)
                except Exception as e:
                    print(e)

            # Nova: flavor
            try:
                flavors = get_flavors(doc)
            except Exception as e:
                print(e)
            # If the flavors list is populated it will try to look for the items inside the openstack items
            if flavors:
                try:
                    verify_flavors(flavors, doc, yamlfile)
                except Exception as e:
                    print(e)
                    
            # Neutron: security group
            try:
                sec_groups = get_secgroups(doc)
            except Exception as e:
                print(e)
            # If the sec_groups list is populated it will try to look for the items inside the openstack items
            if sec_groups:
                try:
                    verify_secgroups(sec_groups, doc, yamlfile)
                except Exception as e:
                    print(e)

            # Neutron: networks
            try:
                networks = get_networks(doc)
            except Exception as e:
                print(e)
            # If the networks list is populated it will try to look for the items inside the openstack items
            if networks:
                try:
                    verify_networks(networks, doc, yamlfile)
                except Exception as e:
                    print(e)

            # Neutron: ports
            try:
                ports = get_ports(doc)
            except Exception as e:
                print(e)
            # If the ports list is populated it will try to look for the items inside the openstack items
            if ports:
                try:
                    verify_ports(ports, doc, yamlfile)
                except Exception as e:
                    print(e)

            # Nova: key pairs
            try:
                keypairs = get_keypairs(doc)
            except Exception as e:
                print(e)
            # If the ports list is populated it will try to look for the items inside the openstack items
            if keypairs:
                try:
                    verify_keypairs(keypairs, doc, yamlfile)
                except Exception as e:
                    print(e)

            # Cinder: volumes
            try:
                volumes = get_volumes(doc)
            except Exception as e:
                print(e)
            # If the ports list is populated it will try to look for the items inside the openstack items
            if volumes:
                try:
                    verify_volumes(volumes, doc, yamlfile)
                except Exception as e:
                    print(e)

        # if the file has errors it is saved in ./ErrorsYamlFiles and a log is created
        except Exception as e:
            # If there is an exception it will be saved into the Log file
            with open("{0}-{1}-error.log".format(filename, today), 'a+') as output:
                output.write("{}\n".format(str(traceback.format_exc())))
            print("     Invalid YAML file")
            os.rename("{}/{}".format(pathfiles, yamlfile), "{}/{}".format(patherr, yamlfile))

if onlyyaml:
    printout("\n>> All files have been analyzed\n", CYAN)

#################################################
#           Logs export to ./Log dir            #
#################################################
# It saves a list of the files present in the same directory of the validator.py file
onlyfiles = [f for f in listdir(".") if isfile(join(".", f))]
# It saves a list of only log files out of the previous list
onlylog = [f for f in onlyfiles if f.endswith(".log")]
# It moves every log file into the Log directory
for log in onlylog:
    os.rename("{}/{}".format(dir_base, log), "{}/{}".format(pathlog, log))
