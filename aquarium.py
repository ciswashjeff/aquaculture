#=====================================================================================================================================================================================================================
#                                                                     ~ Continuous-Time Simulation Of Chemical Concentration in Aquariums ~
#                                                                      File: aquarium.py
#                                                                      Authors: 
#                                                                      Description: Keeps track of the values of relevant chemicals in an aquarium system over time.
#
#
#
#=====================================================================================================================================================================================================================
# Imports 
import numpy as np
import math
import random
import matplotlib.pyplot as plt
from alive_progress import alive_bar
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox, QComboBox
from fish import fish



# Constants
Xmin = 0
Xmin = 0
Xmax = (24*math.pi)
Ymin = -(6*math.pi)
Ymax = (5* math.pi)
Zmin = (-6* math.pi)
Zmax = (2* math.pi)
Wishbone = (5 * pow(10,-6))
Wishbone1 = (2 * pow(10,-8))
Wishbone2 = (3 * pow(10,-6))
V = 4838400     # Period of time to run sim over before list is cleared
numV = 1        # Amount of times period of V is simulated 
tmin = 0


def p1(t):
  step1 = np.arctan(t0(t))             
  step2 = step1 - np.arctan(t0(0))              
  step3 = Wishbone * step2
  return step3

p2 = pow(10,-4)
p3 = 0
p4 = (2* pow(10,-17))
q1 = (1/5)
q2 = (1/8.5)

# inital p2 and p4 for calculation
p2i = p2
p4i = p4



# Other Factors
DO = 10
L = 75 # Size of tank in liters
SelfSuffcient = True


# Define Functions

def convert_seconds_to_weeks(seconds):
    dtWeeks = []
    for t in seconds:
        weeks = t/(604800)  # 604800 seconds in a week
        dtWeeks.append(weeks)
    return dtWeeks  
# Mu s
def mu1(t):
  result = Wishbone1*(np.arctan([t1(t)])-np.arctan([t1(tmin)]))
  return result
  
def mu2(t):
  result = Wishbone2*(np.arctan(t2(t))-np.arctan(t2(tmin)))
  return result
  
def t0(t):
    return(((Xmax - Xmin) / V)*t + Xmin)

def t1(t):
    return(((Ymax - Ymin) / V)*t + Ymin)
    
def t2(t):
    return(((Zmax - Zmin) / V)*t + Zmin)  


# Change of concentration of Nitrate

def changeInAmmonia(t,C1,C2):
  step1 = p1(t) * (1 - ((q1) * C1))
  step2 = step1 - mu1(t) * ((C1 * C1) * (C2 * C2 * C2))
  concentrationChange = step2
  return concentrationChange



def changeInOxygen(t,C1,C2,C3):    # Change of Oxygen concentration over time 
    result = p2*(1-(q1)*(C2))-mu1(t)*pow(C1,2)*pow(C2,3)-mu2(t)*math.sqrt(C2)*C3
    return result
  
def changeInNitrite(t,C1,C2,C3):    # Change of Nitrite concentration over time 
    result = mu1(t)*(pow(C1,2))*(pow(C2,3))-mu2(t)*math.sqrt(C2)*C3-p3*C3
    return result

def changeInNitrate(t,C2,C3,C4):    # Change of Nitrate concentration over time 
  dt = 1
  dC4 = dt*(mu2(t)* math.sqrt(C2)*C3-(p4*C4))
  return dC4


   


#======================================================================================================================================
# Sim Function 
#======================================================================================================================================
def simulation(tank_size, number_of_fish, type_of_fish, duration, production, save_log, fish_list):
    print("=============================================================================================================================")
    print("\n\n")
    print("                              Agent-Based Continuous-Time Simulation of Aquaculture Systems                                     ")
    print("                           Written By: Alex Puskaric, Devon Godde, Elijah Muzzi, Jacob Sinclair                                 ") 
    print("\n")
    print("=============================================================================================================================")
    print("\n\nStarting Simulation...\n\n")


    # Plant Biomass List
    plantPopulation = [0.5, (0.00000019*1)] # Normalized Plant Biomass, Growth Rate per Second

    # Constants
    fish_population = fish_list
    V = int(duration)
    dt = 1
    alivebaramount = V // dt

    

   
    # Reset chemical concentrations for each simulation run
    C1, C2, C3, C4 = 0, 8.5, 0, 0
    C1i, C2i, C3i, C4i = 0, 8.5, 0, 0
    dC1, dC2, dC3, dC4, dT = [], [], [], [], []
    fishHealth = 100

    with alive_bar(alivebaramount) as bar:
        for t in range(V):
            for fish in fish_population:
                action_result, status = fish.action(t)
                if status == 'Eating':
                    print("eating")
                    plantPopulation[0] = plantPopulation[0] - fish.getAmmountEaten()
                    # Modify chemicals accordingly
                    pass
                elif status == 'Pooping':
                    C1 += action_result  # Assuming action_result is the increase in Ammonia
                    print("pooping")
                elif status == 'Peeing':
                    print("peeing")
                    # Modify chemicals accordingly
                    pass
                # (could move this to fish class)
                # if the ammonia levels exceed 2 mg/L or nitrite levels exceed 5 mg/l
                # the fish begin to die 
                if C1 >= 2 or C3 >= 5:
                    # each time of the simulation is one sec
                    # if we assume it takes one week for the fish to die, it loses
                    # 1/604800 (one week in seconds) of health each second
                    fishHealth -= 1 / 604800
                    if fishHealth <= 0:
                        # pop the fish from the array
                        for i in range(number_of_fish):
                            fish_population.pop(0)
                            print("a fish has died")
                            
                        # report that the fish are dead and the tank is not sufficient
                        SelfSuffcient = False


            # If plant biomass is greater than max, set it to max
            if((plantPopulation[0] + plantPopulation[1]) >= 1):
                plantPopulation[0] = 1
            # If plant biomass is at or less than 0, keep it at 0
            elif(plantPopulation[0] <= 0):
                plantPopulation[0] = 0
            # Otherwise, grow
            elif(plantPopulation[0] > 0):
                plantPopulation[0] = plantPopulation[0] + plantPopulation[1]

            p2 = p2i * (0.5 + plantPopulation[0])
            p4 = p4i * (0.5 + plantPopulation[0])  

            C1 += changeInAmmonia(t,C1,C2)
            C2 += changeInOxygen(t,C1,C2,C3)
            C3 += changeInNitrite(t,C1,C2,C3)
            C4 += changeInNitrate(t,C2,C3,C4)

            dC1.append(C1 - C1i)
            dC3.append(C3 - C3i)
            dC4.append(C4 - C4i)
            dT.append(t)

            bar()
    print("Generating plots...")
    plot_results(dC1, dC3, dC4, dT, number_of_fish, fish_population, production, tank_size)


#======================================================================================================================================
# Plotting Start
#======================================================================================================================================
 # Create a figure and axis
fig, ax = plt.subplots(2,2)
fishPop = [0,0]
plantPop = [0,0]


def plot_results(dC1, dC3, dC4, dT, number_of_fish, fish_population, production, tank_size):
    fig, ax = plt.subplots(2, 2, figsize=(10, 8))
    

    # Chemical plots
    ax[0, 0].plot(convert_seconds_to_weeks(dT), dC1, label='Ammonia')
    ax[0, 0].plot(convert_seconds_to_weeks(dT), dC3, label='Nitrite')
    ax[0, 0].plot(convert_seconds_to_weeks(dT), dC4, label='Nitrate')
    ax[0, 0].legend()
    ax[0, 0].set_title('Aquarium Chemicals Over Time') 
    ax[0, 0].set_xlabel('Time (Weeks)')
    ax[0, 0].set_ylabel('Change in Concentration: mg/L')

    
    # Fish population plot
    '''for fish in range(number_of_fish):
        currentFish = fish_population[fish]
        production += currentFish.getWeight()
        print(fish_population[fish].getWeight())'''
        
    for fsh in fish_population: # This one should work for populating production
        production += fsh.getWeight()
    
    tankStatus = f"Aquaponic Stats\n_____________________\n\nTank Size: {L} Liters \n\nThe tank is self suffcient: {SelfSuffcient}\n\nAmount of Fish Produced (g): {production}\n\nTime Elapsed in Week(s): {V/604800}"
    
    ax[1, 0].plot(convert_seconds_to_weeks(dT), [len(fish_population)] * len(dT), label='Fish Population')
    ax[1, 0].set_title('Populations Over Time')
    ax[1, 0].set_xlabel('Time (Weeks)')
    ax[1, 0].set_ylabel('Population Size')
    ax[1, 0].legend()

    # Tank status
    ax[0, 1].axis('off')

    ax[1, 1].axis('off')
    ax[1, 1].text(0.421, 0.998, tankStatus, fontsize=16, ha='left', va='bottom')

    plt.tight_layout()
    plt.show()


# GUI

class AquariumSimulatorGUI(QWidget):
    def __init__(self):
        super().__init__()

        # GUI layout
        layout = QVBoxLayout()

        # Tank Size Input
        self.tankSizeInput = QLineEdit(self)
        layout.addWidget(QLabel('Tank Size (Liters):'))
        layout.addWidget(self.tankSizeInput)

        # Number of Fish Input
        self.numberOfFishInput = QLineEdit(self)
        layout.addWidget(QLabel('Number of Fish:'))
        layout.addWidget(self.numberOfFishInput)

        # Creating a QComboBox
        self.dropdown = QComboBox()
        layout.addWidget(QLabel('Size of Fish:'))
        self.dropdown.addItem('Fry- 1 gram')
        self.dropdown.addItem('Juveniles- 8 to 9 grams')
        self.dropdown.addItem('Adults- 450 to 900 grams (1 to 2 pounds)')

        # Connecting a function to handle the item selection change
        self.dropdown.currentIndexChanged.connect(self.on_selection_change)

        layout.addWidget(self.dropdown)

        # Duration of Simulation Input
        self.durationInput = QLineEdit(self)
        layout.addWidget(QLabel('Duration of Simulation (Seconds):'))
        layout.addWidget(self.durationInput)

        # Save Log Checkbox
        self.saveLogCheckbox = QCheckBox('Save Log to Folder', self)
        layout.addWidget(self.saveLogCheckbox)

        # Start Simulation Button
        self.startButton = QPushButton('Start Simulation', self)
        self.startButton.clicked.connect(self.start_simulation)
        layout.addWidget(self.startButton)

        # Dropdown menu for fish weight / age
        self.setWindowTitle('Dropdown Menu Example')

        label = QLabel('Select age range:')
        layout.addWidget(label)

        self.setLayout(layout)

    def on_selection_change(self, index):
        selected_item = self.dropdown.currentText()
        print(f"Selected: {selected_item}")

    def start_simulation(self):
        # Get input values
        tank_size = int (self.tankSizeInput.text())
        number_of_fish = int (self.numberOfFishInput.text())

        # choosing the starting weight of the fish based on the value the user selects
        if 'Fry- 1 gram' in self.dropdown.currentText():
            fish_weights = 1
        elif 'Juveniles- 8 to 9 grams' in self.dropdown.currentText():
            fish_weights = random.randint(8, 9)
        elif 'Adults- 450 to 900 grams (1 to 2 pounds)' in self.dropdown.currentText():
            fish_weights = random.randint(450, 900)

        duration = self.durationInput.text()
        save_log = self.saveLogCheckbox.isChecked()
        production = 0
        
        fish_population = [fish(f'Tilapia{x}', 0.0000069, 0.0000104, 0.0000173, 0, 0.02, fish_weights) for x in range(number_of_fish)]


        # Start the simulation with these parameters
        # Implement the logic to start the simulation here
        print(f"Starting simulation with: Tank size: {tank_size} liters, Number of fish: {number_of_fish}, Size of fish: {self.dropdown.currentText()}, Duration: {duration} seconds, Save log: {save_log}")
        simulation(tank_size, number_of_fish, fish_weights, duration, production, save_log, fish_population)

            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AquariumSimulatorGUI()
    window.show()
    sys.exit(app.exec_())