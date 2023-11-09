#=====================================================================================================================================================================================================================
#                                                                     ~ Continuous-Time Simulation Of Chemical Concentration in Aquariums ~
#                                                                      File: plant.py
#                                                                      Authors: 
#                                                                      Description: 'plant' interface, used to impliment different species of plants
#
#
#
#=====================================================================================================================================================================================================================

from asyncio.constants import DEBUG_STACK_DEPTH


"""
To-do List:
-Create constructor
-Create get methods
-Create growth methods
-Determine probabilities
    -methods to change probabilities
    -calcs to determine proba
    -markov chain

"""

class Plant:
    """ *ARGUMENTS*
    size # numeric value from 0-1 that tracks the size of the plant
    growthRate # calculated growth rate of plant
    growPercent # percent chance of growing
    oxygenPercent # percent chance of producing oxygen
    deathPercent # percent chance of plant dying
    living # boolean of whether or not the plant is living
    """
    def __init__(self, size, growthRate, growPercent, oxygenPercent, deathPercent, living):
        self.size = size
        self.growthRate = growthRate
        self.growPercent = growPercent
        self.oxygenPercent = oxygenPercent
        self.deathPercent = deathPercent
        self.living = living
        
    def getPlantSize(self):
        return self.size

    def getPlantGrowthRate(self):
        return self.growthRate

    def getPlantGrowPercent(self):
        return self.growPercent

    def getPlantOxygenPercent(self):
        return self.oxygenPercent
    
    def getPlantDeathPercent(self):
        return self.deathPercent
    
    def getPlantLiving(self):
        return self.living
    
    def plantDie(self):
        self.living = False
  
    def setPlantGrowthRate(self, newRate):
        self.growthRate = newRate      

    def setPlantGrowPercent(self, newPercent):
        self.growPercent = newPercent

    def setPlantOxygenPercent(self, newPercent):
        self.oxygenPercent = newPercent
    
    def setPlantDeathPercent(self, newPercent):
        self.deathPercent = newPercent

    def plantGrow(self):
        self.size = self.size + self.growthRate
        print(self.size)
        
