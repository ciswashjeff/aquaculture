#=====================================================================================================================================================================================================================
#                                                                     ~ Continuous-Time Simulation Of Chemical Concentration in Aquariums ~
#                                                                      File: fish.py
#                                                                      Authors: 
#                                                                      Description: 'Fish' interface, used to implement fish objects to interact with the system  
#
#
#
#=====================================================================================================================================================================================================================


import numpy as np 
import matplotlib.pyplot as plt
import random 


class Fish:

    '''
    name = "tetra"
    eatPercent = 0.0
    poopPercent = 0.0
    deathPercent = 0.0
    servingSize = 0.0
    poopAmount = 0.0
    fishGramWeight = 0.13
    living = True 
    '''

    def _init_(self, name, eatPercent, poopPercent, deathPercent, servingSize, poopAmount, fishGramWeight, living):
        self.eatPercent = eatPercent
        self.poopPercent = poopPercent
        self.deathPercent = deathPercent
        self.servingSize = servingSize
        self.poopAmount = poopAmount
        self.fishGramWeight = fishGramWeight
        self.living = True 


        #fish poop every 48hrs and pee every 24hrs
        #fish eat once or twice a day
        #fish eat about 2% of their body weight daily
        
        #generate random num between 0-100
            #if 0-2
                #fish poops
            #if 2-4
                #fish pees
            #if 5-8 
                #fish eats
            #if 9-100
                #fish does nothing 