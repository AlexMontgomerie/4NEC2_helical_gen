# Project aims
We intend to create a tool that will take an initial description of an antenna and through some machine learning algorithm, be able to create an optimised version of the antenna. We will need modules as follows:
- NEC card generator
- NEC parser and output generator
- graphics generator
- parameter learning module

## NEC card generator
this will be a simple python module that will take certain defined parameters and generate an nec card associated with it. It should remove some of the details such as segment count and other parameters, making the parameters that need to be learned more focused.

## NEC parser and output generator
This module will use necpp to take an NEC card and create an output csv file to be used by other modules. 

## graphics generator
a python module that can generate graphics for the radiation pattern of the antenna.

## parameter learning module
This still needs to be researched. It will probably be an implimentation of some sort of genetics algorithm, that will keep refining the parameters until they are optimal. We will have to decide on some sort of metric that tells us when we have a good antenna.
