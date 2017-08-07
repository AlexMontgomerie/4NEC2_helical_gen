#This script will hopefully install the dependancies for the python files
#this works on ubuntu 16 LTS

#to run this open a shell in this file's directory and use the command
#bash python-setups.sh

sudo apt-get install python pip

sudo pip install --upgrade pip

#now get the packages
sudo pip install numpy matplotlib

sudo apt-get install python-tk
#do some cool end sript message
echo '--------------------------------------------'
echo '--------------- Script ended ---------------'
echo '--------------------------------------------'


