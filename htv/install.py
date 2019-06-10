import os
import sys
import subprocess

curr_dir = os.getcwd()

# Main and sub directories creation
print("Enter the full path where to install the app: ")
"""app_path = input()
if app_path.endswith("/"):
    app_path = app_path[:-1]
try:
    os.chdir(app_path)
except:
    print("This is not a valid path")

try:
    app_dir = "{}/HeatTemplateValidator".format(app_path)
    os.mkdir(app_dir, 0o777)
    template_dir = "{}/HeatTemplateValidator/TemplateLocalStorage".format(app_path)
    os.mkdir(template_dir, 0o777)
    warn_dir = "{}/HeatTemplateValidator/WarnYamlFiles".format(app_path)
    os.mkdir(warn_dir, 0o777)
    err_dir = "{}/HeatTemplateValidator/ErrYamlFiles".format(app_path)
    os.mkdir(err_dir, 0o777)
    valid_dir = "{}/HeatTemplateValidator/ValidYamlFiles".format(app_path)
    os.mkdir(valid_dir, 0o777)
    log_dir = "{}/HeatTemplateValidator/Log".format(app_path)
    os.mkdir(log_dir, 0o777)
except Exception as e:
    print(e)"""

ll = subprocess.run(['ls', '-lart'], stdout=subprocess.PIPE).stdout.decode('utf-8')

cristoddio = subprocess.run(['/Users/pc-ko2/PycharmProjects/MinorTest/HeatTemplateValidator/htv/htvalidator/install.sh'], stdout=subprocess.PIPE).stdout.decode('utf-8')

print(cristoddio)




