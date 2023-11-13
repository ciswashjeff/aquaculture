#=====================================================================================================================================================================================================================
#                                                                     ~ Continuous-Time Simulation Of Chemical Concentration in Aquariums ~
#                                                                      File: fish.py
#                                                                      Authors: 
#                                                                      Description: 'Fish' interface, used to implement fish objects to interact with the system  
#
#
#
#=====================================================================================================================================================================================================================

import matplotlib.pyplot as plt
import random 

class Fish:

    def __init__(self, name, eatPercent, poopPercent, deathPercent, servingSize, poopAmount, fishGramWeight, living):
        self.name = name
        self.eatPercent = eatPercent
        self.poopPercent = poopPercent
        self.deathPercent = deathPercent
        self.servingSize = servingSize
        self.poopAmount = poopAmount
        self.fishGramWeight = fishGramWeight
        self.living = True
    
    #these still need work, specifically in calculating the chemical changes
    '''
    def fishEat(eatPercent, fishGramWeight, servingSize):
        self.servingSize = fishGramWeight = 0.02
        self.eatPercent += 0.02
        
    def fishPoop(fishGramWeight, poopPercent, poopAmount):
        self.poopAmount += fishGramWeight = 0.33 #fish poop equal to about 1/3 of their body weight a day
        self.poopPercent -= fishGramWeight = 0.33 #total percent - the percent they poop

    '''

    #def fishPee():
    #need to work on this one a lot

    #lists storing an index for each time a fish does an actions
    numFishEatingActions = []
    numFishPoopingActions = []
    numFishPeeingActions = []

    #these are used to iterate over the different action lists
    eatIndex = 0
    poopIndex = 0
    peeIndex = 0

    def fishActionGenerator(numFishEatingActions, numFishPoopingActions, numFishPeeingActions, eatIndex, poopIndex, peeIndex):
        fishActionProb = random.random()
        if fishActionProb >= 0.0 and fishActionProb <= 0.0000069: #fish eats if the random number is in this range
            eatIndex += 1
            numFishEatingActions.append(eatIndex)
            #fish.fishEat() 
        if fishActionProb > 0.0000069 and fishActionProb <= 0.0000104: #fish poops if the random number is in this range
            poopIndex += 1
            numFishPoopingActions.append(poopIndex)
            #fish.fishPoop()
        if fishActionProb > 0.0000104 and fishActionProb <= 0.0000173: #fish pees if the random number is in this range
            peeIndex += 1
            numFishPeeingActions.append(peeIndex)
            #fish.fishPee() 
            #if none of these if statements are fulfilled, the fish is doing no actions


    #====================================================================================================================================
    # After this point can be commented out if prefered. This portion of the 
    # code visualizes the actions fish have made.
    #
    #
    #====================================================================================================================================

    secs = 604800
    numweeks = 6
    for i in range(secs = numweeks):  #running the loop this many times to represent the 604,800 secs in a week
        fishActionGenerator(numFishEatingActions, numFishPoopingActions, numFishPeeingActions, eatIndex, poopIndex, peeIndex)

    print("Times the fish ate: " + str(len(numFishEatingActions)))
    print("Times the fish pooped: " + str(len(numFishPoopingActions)))
    print("Times the fish peed: " + str(len(numFishPeeingActions)))
        
    #plotting
    plt.figure()

    plt.bar(len(numFishEatingActions), len(numFishEatingActions), label = 'Times ate', width = 4)
    plt.bar(len(numFishPoopingActions),len(numFishPoopingActions), label = 'Times pooped', width = 4)
    plt.bar(len(numFishPeeingActions), len(numFishPeeingActions), label = 'Times peed', width = 4)

    # Create a legend for the bars
    plt.legend()

    plt.title('Fish actions over ' + str(numweeks) + ' week span')
    plt.xlabel('Times action was performed')

    #hiding the y axis values
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    # Display the plot
    plt.show() 
    
       
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