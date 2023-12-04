#=====================================================================================================================================================================================================================
#                                                                     ~ Continuous-Time Simulation Of Chemical Concentration in Aquariums ~
#                                                                      File: fish.py
#                                                                      Authors: 
#                                                                      Description: 'Fish' object, used to implement fish objects to interact with the system  
#
#
#
#=====================================================================================================================================================================================================================

import random 

class fish:

    def __init__(self, name, eatPercent, poopPercent,peePercent, deathPercent, servingSize, weight):
        self.name = name
        self.eatPercent = eatPercent
        self.poopPercent = poopPercent
        self.peePercent = peePercent
        self.deathPercent = deathPercent
        self.servingSize = servingSize
        self.weight = weight
        self.living = True
        self.status = 'Nothing'
    
    #these still need work, specifically in calculating the chemical changes
    
    def Eat(self):
        self.status = 'Eating'
        result = (self.weight*self.servingSize)
        return result
        
    def Poop(self):
        self.status = 'Pooping'
        result = (self.weight/3)
        return result
        
    def Pee(self,t):
        self.status = 'Peeing'
        hours = t/3600
        result = (pow((0.0014*self.weight),2)-0.4384*self.weight+43.303)
        result = result*hours
        return result
    
    def grow(self, T, DO, A, BOD, t):
            # Hardcoded parameters from the table paper
            a = 0.53
            DOcrit = 1.0
            DOmin = 0.3
            h = 0.8
            j = 0.0132
            kmin = 0.00133
            m = 0.67
            n = 0.81
            s = 21.38
            Tmin = 15
            Tmax = 41
            Topt = 33
            Acrit = 0.06
            Amax = 1.40
            BODcrit = 20
            BODmax = 40

            # Calculate food assimilation efficiency (b) and other factors
            # Note: The specific formulas for b and daily ration need to be based on the paper and environmental parameters T, DO, A, BOD

            # Calculate the rate of weight change
            # Note: The specific formula needs to be adapted from the paper
            # Example (simplified):
            weight_change = h * (self.weight ** m) - kmin * (self.weight ** n)
            self.weight += weight_change * t  # Update weight, t is the time step in days


    def action(self,t):
        fishActionProb = random.random()
        print(fishActionProb)
        if fishActionProb >= 0.0 and fishActionProb <= self.eatPercent:      #fish eats if the random number is in this range 
            result = self.Eat() 
        if fishActionProb > self.eatPercent and fishActionProb <= self.poopPercent: #fish poops if the random number is in this range   
            result = self.Poop()
        if fishActionProb > self.poopPercent and fishActionProb <= self.peePercent: #fish pees if the random number is in this range
            result = self.Pee(t) 
        else:                                                          #if none of these if statements are fulfilled, the fish is doing no actions
            result = 0
            self.status = "Nothing"
            
        print(self.status)
        return result,self.status
    

            
       


   
