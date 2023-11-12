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
-Create constructor (done)
-Create get methods (done)
-Create growth methods (done)
-Determine growth rates and death conditions

"""

class Plant:
    """ *ARGUMENTS*
    size # numeric value from 0-1 that tracks the size of the plant
    growthRate # calculated growth rate of plant
    living # boolean of whether or not the plant is living
    """
    
    def __init__(self, size, growthRate, living):
        self.size = size
        self.growthRate = growthRate
        self.living = living
        
    def getPlantSize(self):
        return self.size

    def getPlantGrowthRate(self):
        return self.growthRate
    
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
        
    def eaten(self, amount):
        if((self.size - amount) <= 0):
            self.plantDie()
        else:
            self.size = self.size - amount
        
        
