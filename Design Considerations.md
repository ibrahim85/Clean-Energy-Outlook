## Overview

Clean Energy Outlook is a software that reads in energy generation data from 1960 to 2014 of various states of the United States and predicts the energy outlook of each state for the next 5 years. Software will be useful for investors and policy makers in renewable energy. Investors in clean energy can use this software to identify states where clean energy have higher potential. Policy makers can also use this software to develop clean energy policies and investment plans for different states.

## Use Case  

**Use Case Name:**  
Predict clean energy industry outlook for a state in the United States and display the installation costs for the predicted increase in clean energy.  

**Description:**   
For one state, the total energy demands over the years will go up with the increase of population and economy. The energy supplied by clean energy sources is bound to increase. Using the energy sector information from the last 50 years, predict the market and need for solar energy in near future for a specific state. With such predictions for all states, we can generate an overall outlook of clean energy in the United States.  

**Actors:**     
User (Primary)   

**Assumptions:**  
* Factors that are not considered are neglected.  

**Steps:**  
* User selects a state from the interactive map.  
* Displays the demand and future trends of clean energy like wind, solar, hydro, and nuclear in the next 5 years for the selected state.  
* Display the installation cost of the predicted increase in clean energy.  

**Issues:**  
* How much weight does each factor has on the future of one kind of clean energy?  
* How to create an interactive map of the US?  
* Difficult to collect installation cost data for some of energies.  

## Figures/Interaction Diagrams

Figures/Interaction Diagrams go here.  

## Components

`interface`  
* Use:  
Allows primary actor to view past data and future trends in clean energy for the selected state.  
* Input:  
User selects a specific state and types of energy to view.  
* Output:  
Display past energy production data with the time axis and future trends of the selected energies for the selected state.  

`state_selector`  
* Use:  
Selects a state and displays trends in different kinds of clean energies.  
* Input:  
Gets the input from user.
* Output:  
Displays the expanded map of the state and shows trends of clean energies.  

`regression`  
* Use:  
Performs regression on the training data and displays plot of future trends based on user specifications.  
* Input:  
States and types of energy selected by users.  
* Output:  
Plot of future energy trends for a particular state.  

`solar_energy_economics`  
* Use:  
Predicts installation costs for PV energy based on future trends.  
* Input:  
State, The Open PV Project, Future trends in solar energy, Factors to be considered, and year under consideration.  
* Output:  
Predicted installation cost based on past costs.  

`wind_energy_economics`  
* Use:  
Predicts installation costs for wind energy based on future trends.  
* Input:  
State, Wind Energy Database, Future trends in wind energy, Factors to be considered, and years under consideration.  
* Output:  
Predicted installation cost based on past costs.  

`hydro_energy_economics`  
* Use:  
Predicts installation costs for Hydro energy based on future trends.  
* Input:  
State, Hydro Energy Database, Future trends in Hydro energy, Factors to be considered, and years under consideration.  
* Output:  
Predicted installation cost based on past costs.  

`nuclear_energy_economics`  
* Use:  
Predicts installation costs for nuclear energy based on future trends.  
* Input:  
State, Nuclear Energy Database, Future trends in nuclear energy, Factors to be considered, and year under consideration.  
* Output:  
Predicted installation cost based on past costs.  

## Notes  
* Still looking for datasets for wind, hydro, and nuclear energy economics.  
* Not sure how to build GUI and maps of the US.  
* Possibility to include more datasets.  
