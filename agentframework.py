"""The module agentframework

Author: Shahreen Muntaha Nawfee
Created on: 15th December 2018
Version used: Python 3.7

Creates the agent class and pass on object properties
"""

import random  #module random imported



class Agent(): 
    """ Create a class named Agent"""
    
    def __init__ (self,environment,agents,y,x):
        """define methods for initializing objects
        
        Positional arguments:
        environment-- the space given to agents where they exist
        agents-- 
        y--the coordinate of y value of the agents
        x--the coordinate of x value of the agents
        """

        if (y == None):
            self.y = random.randint(0,100)
        else:
            self.y = y
            """Assign values to y coordinate
            
            missing values of y are assigned random integer value between 0 
            and 100
            """
        if (x == None):
            self.x = random.randint(0,100) #integer value between 0 and 100
        else:
            self.x = x
            """Assign values to x coordinate
            
            missing values of x are assigned random integer number between 0 
            and 100
            """ 
        
        #Assign list of environment to other agents
        self.environment = environment 
        #Each agent starts with no food to eat
        self.store = 0  
        #Assign store to the agents
        self.agents = agents 
        #Assign list of agents 
        self.neighbourhood = 20 
        #The distance around each agent where it will search for other agents


       
    def move(self):
        """Move method defined for agents
        
        if the random function of the random module is less than 0.5
        the y value of the self agent will increase by 1 randomly, within the
        grid boundary, if not the y value will decrease by 1 unit
        
        the same moving condition will be followed by x
        """
        
        # Move agent randomly by 1 cell at a time within the grid boundary set
        if random.random() < 0.5:            
            self.y  = (self.y  + 1) % 100  #%100 to set up bounding effects
        else:
            self.y  = (self.y  - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
            
            
    
    def eat(self):
        """ eat method for agents defined
        
        the agents will eat from the environment based on the condition set
        """
        if self.environment[self.y][self.x] > 10: 
            self.environment[self.y][self.x] -= 10
            self.store += 10 
            
            
 
    def distance_between (self, agents):
        """ Euclidian distance between agents
        
        returns distance between agents calculated using Pythagoras' theorem
        """
        return (((self.x - agents.x)**2) + ((self.y - agents.y)**2))**0.5
     
        
    
    def share_with_neighbours(self,neighbourhood):
        """Define methods for sharing with neighbours
        
        the sharing withneighbours depends on the neighbourhood distance. Distance 
        between agents are calculated. If there is an agent within the neighbourhood
        they share the food in store equally.
        """
        for agents in self.agents:  #Loop though agents in self agent
            dist = self.distance_between(agents) 
            #When distance is less than or equal to the neighourhood that is 20
            if dist <= neighbourhood: 
                sum = self.store + agents.store  
                ave = sum/2 #Average calculated by dividing sum by two
                self.store = ave
                agents.store = ave
                print (str (dist) + " " + str (ave)) 
                

                
                 
            
    