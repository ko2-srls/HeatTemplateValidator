#!/usr/bin/env bash

echo "Creating virtual environment";
pip3 install -U pip
pip3 install -U virtualenv
rm -rf venv
virtualenv venv &&
source ./venv/bin/activate
pip install -r requirements.txt
mkdir ValidYamlFiles WarnYamlFiles ErrYamlFiles Log TemplateLocalStorage
echo "Environemnt created and requirements installed"

