
The program contains code for running an animation of a agent based model. The source code for running an agent based model is set into 
two python files, agentframework and Final Model, in (.py) format. Within the folder is also the liscence file. Within the python files
are documentation and comments, which explain what each part of the code means. The codes were witten in an object-oriented programming
language- i.e, python. Spyder IDE was used for code editing and viewing. The code development was done in Windows 10. The details of the 
code files are as follows:

###agentframework.py: This file has to be open from Spyder. It contains code to build the agents and give characters to them. A class named
'Agent' is created here and __init__ function used to pass initialize the agents for the model. The parameters set for the objects are: 
environment, agents, x and y location of agents.
The methods passed to this object gave behaviour of the agents. the function 'move' set the conditions of the agents to move, 'eat' set
the condition of feeding of the agents, the 'share_with_neighbours' functions assigned the communication of the agents. The distance between agents
were calculated using the Pythagoras' theorem.
This file has to be run once, before the FinalModel.py is run. 

###FinalModel.py: This file imports modules and packages from internal and external libraries and contain the code to pass the behaviour to the 
agents, extract values from webpage and create an animation of the model.The module created 'agentframework' is imported here. 

The file contains the code to genrate number of agents, and to extract their y and x coordinate value from a web page. The text values are 
extracted from the html using BeautifulSoup package.

The enviornment data is imported from a webpage containg raster grid values, using csv read code. The webpage link to the environment data 
is provided with the code. The environment data is appended to anenvironment list created.

The image of the environment and plot of agents in them are displayed using matplotlib. So the matplotlib is imported in to this file. 

The 'gen-function' is used to generate frames, between animation function. And 'run' function is used to run the model.

The model output is displayed in a new window. The title, and layout of this new window by using TKinter, a GUI package. The new windows 
title is set as 'Model' with a sub-tab 'Model' chowing 'Run model' option

------------------------------------------------------------------------------------------------------------------------------------
### Running the model
To run the model the FinalModel python file has to be open in Spyder. along with the agentframework, which has been already loaded. By 
pressing the 'Run' button in main window, the model can be began in the IPython console. 

Running the model prints the y and x values of the html first in to the iPython console. Besides, an image showing the initial condition 
of the environment is also printed out.

The 'Model' window has to be opened. In this window, there is the sun-tab named 'Model' it has to be opened. It shows option' Run Model' 
which has to be pressed. This runs the animation. Running the animation shows the movement of the agents in the environment, with 
changes in the environment. the animation runs the number of iteration or unless the stopping condition is met. The final condition is
printed out in the IPython console once the animation stops and the model window is closed. Moreover, the distance between agents and 
the average value of their sharing of the food is printed out in the Ipython console. 

----------------------------------------------------------------------------------------------------------------------------------
###Warnings: The agentframework.py file, the FinalModel.py file and the in.txt file should be present in the same directory. Here
all the files have to be opened from the folder named: GEOG5990M_[201277909]_Assessment1 folder. 
Otherwise the code will not run

---------------------------------------------------------------------------------------------------------------------------------
##Licence
The model code has been licenced using : MIT License

Copyright (c) 2018 Nawfee. A text file, detailing the licence terms and conditions has been attached in the model folder. 

--------------------------------------------------------------------------------------------------------------------------------------

