import os
import traceback
from htv.config.keygen import keygen

home = os.environ['HOME']

def install():
    app_dir = "{}/htv".format(home)

    paths = ["/.key", "/TemplateLocalStorage", "/WarnYamlFiles", "/ErrYamlFiles", "/ValidYamlFiles", "/Log", "/rc_files"]
    # Main and sub directories creation in $HOME
    try:
        os.system("mkdir $HOME/htv")
    except:
        print(str(traceback.format_exc()))
        return "An error occurred"
    for path in paths:
        try:
            new_path = "{}{}".format(app_dir, path)
            os.system("mkdir -p {}".format(new_path))
        except:
            print(str(traceback.format_exc()))
    print("Now move the Heat template files in {0}/TemplateLocalStorage "
          "and the openrc files (for Openstack authentication) to {0}/rc_files".format(app_dir))

    keygen()
