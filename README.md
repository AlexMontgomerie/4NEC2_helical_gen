# 4NEC2_helical_gen
source code to generate .nec files for helical wire antennas. Purpose is to generate simulations that will help with the mechanical design of the antenna. 

# Code Structure
Will have a class to handle creating the correct geometry for the antenna. Then we'll use a handler to translate the geometry into a .nec file for simulation.

# NEC2 class
* Class description:
  Include a description of the parameters and a link to the relevant page in nec manual
* Initialisation:
  initialise the parameters for that nec line
* Construct:
  Function to create a string for that line of nec code
* Verification:
  Verify that the parameters in the class fit NEC2 specification
* (Optional) relevant functions:
  Any other functions relevant to that class

# CPP install

1. clone the NECPP repo 
``` 
git clone https://github.com/tmolteno/necpp 
```
1. follow the instructions to install necpp [here](https://github.com/tmolteno/necpp/blob/master/INSTALL.md). make sure you are in the necpp folder. 

1. copy the configuration header into the 4NEC2... folder 
```
cp (necpp_location)/config.h (4NEC2_location)/
```
1. go to the src folder and export the NECPP_SRC_PATH environmental variable 
``` 
export NECPP_SRC_PATH=$PWD
```
1. to compile, just go into the cpp folder and call make
```
make
```
