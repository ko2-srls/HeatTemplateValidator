# Yaml Validator
![N|Solid](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ47aU08PZRgClNPiVoUqoQ0u87vwVpNMudL9090VE6WIzmEc5p)

YamlValidator is a tool created to validate *.yaml* files and check the parameters' existence in the server Openstack. 

### What does it do?
The main script *validator.py* will analyze every single file from the dir *./TemplateLocalStorage*. 
It moves the valid files into the dir *./ValidYamlFiles*.
It moves the warning files into the dir *./WarnYamlFiles*. 
It moves the error files into the dir *./ErrorYamlFiles* and for each file of the last two groups it creates a log and then it moves all log files into the dir *./Log*. 
At the very beginning of the installation YamlValidator will also create crontab lines inside the *list_cron.txt*.
### Installation
YamlValidator requires [python3] and pip in order to run.
Open the terminal and download the application through *git*:
```sh
$ git clone git@bitbucket.org:iumii/yamlvalidator.git
```
Then change directory:
```sh
$ cd yamlvalidator/
```
install the requirements from the *requirements.txt* file and  create the virtual environment:
```sh
$ ./setup.sh
```
There are few simple steps to follow in order to correctly use YamlValidator:
 - Move the yaml files into the *./TemplateLocalStorage* dir
 - Move the open.rc files into the *./rc_files* dir
After these files transfer activate the virtual environment:
```sh
$ source ./venv/bin/activate
```
Then the application will need the Openstack server password.
Remember to enter this command only once: during the YamlValidator installation, or everytime you need to change the Openstack passwords or *openrc.hs* files.
Enter the passwords after executing the *shadow.py* script:
```sh
$ python shadow.py
```
This command will also generate a list of crontabs in the *list_cron.txt* file that you can use in the general crontab file depending on which *openrc.sh* file is needed.
### Usage
You can choose to run the application using the crontabs created or to run it interactively via *validator.py*:
```sh
$ python validator.py
```
In the interactive mode the application will ask for which openrc file to use for the Openstack.
After this you are ready to go, the files will be moved accordingly with their warnings or errors and logs will be created and moved to the *./Log* dir.
### In case the application directory changes
In case you move the YamlValidator directory to a different path it is necessary to do as follows:
```sh
$ python cron_update.py
```
This is a requirement in order to generate the new crontabs and having them working.
### Clean environment for testing
To go back to a clean environment use the *goback.py* script:
```sh
$ python goback.py
```
### Notes
All advice welcome


   [python3]: <https://www.python.org/download/releases/3.0/>
