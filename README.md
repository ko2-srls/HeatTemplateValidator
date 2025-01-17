# Heat Template Validator
![N|Solid](https://inizanhugo.files.wordpress.com/2018/11/heat.png?w=200)

Heat Template Validator (HTV) is a tool created to validate *Heat templates* (yaml files) and check the parameters' existence in the Openstack server. 

### What does it do?
The main script *htv* will analyze every single file from the dir */htv/TemplateLocalStorage*. 
It moves the valid files into the dir */htv/ValidHeatFiles*.
It moves the warning files into the dir */htv/WarnHeatFiles*. 
It moves the error files into the dir */htv/ErrorHeatFiles* and for each file of the error and warn groups it creates a log and then it moves all log files into the dir */htv/Log*. 
At the very beginning of the installation HTV will also create crontab lines inside the */htv/list_cron.txt* file.
### Installation
HTV requires [python>=3.5] and pip in order to run.
Open the terminal and download the application through *pip*:
```sh
$ pip install htv
```
Then install and configure the package via *htv -i* or *htv --install*:
```sh
$ htv -i
```
This command will create the *htv* into your home directory with the relative subdirectories (Log, TemplateLocalStorage and so on).
There are few simple steps to follow in order to correctly use HTV:
 - Move the Heat files into the *./TemplateLocalStorage* dir
 - Move the open.rc files into the *./rc_files* dir
After this transfer execute *htv -s* or *htv --shadow*:
```sh
$ htv -s
```
Then the application will prompt you the Openstack server password.
Remember to enter this command only once: during the HTV installation, or everytime you need to change the Openstack passwords or *openrc.hs* files.
The *htv -s* command will also generate a list of crontabs in the *list_cron.txt* file that you can use in your system crontab file depending on which *openrc.sh* file is needed.
### Usage
You can choose to run the application using the crontabs created in *list_cron.txt*.
Or to run it no-interactively via *htv*:
```sh
$ htv
```
Or in the interactive mode where the application will ask for which openrc file to use for the Openstack authentication:
```sh
$ htv /Path/To/The/Openrc/File.sh
```
After this you are ready to go, the Heat templates will be moved accordingly with their warnings or errors and logs will be created and moved to the */htv//Log* dir.
### Remember
Whenever you want to use *htv* you first need to move the yaml files to the */htv/TemplateLocalStorage* dir.
### In case the application directory changes
In case you move the HeatTemplateValidator directory to a different path it is necessary to do as follows:
```sh
$ htv -i
$ htv -s
```
This is a requirement in order to generate the new crontabs and having the whole application working.
### Notes
This application fully functions on Ubuntu and MacOS with *python3*, *pip* and *python-dev* installed.
All advice welcome!


   [python>=3.5]: <https://www.python.org/downloads/release/python-350/>
