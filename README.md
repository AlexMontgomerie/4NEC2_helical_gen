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
