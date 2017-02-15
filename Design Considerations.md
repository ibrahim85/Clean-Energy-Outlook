## Overview
Big picture of software goes here.

## Use Cases

### 1. Predict Energy Outlook for a State in the United States
**Use Case Name:**   
Predict Energy Outlook for a State in the United States  
**Description:**   
Predict Energy Outlook for a State in the United States using past 50 years data.  
**Actors:**   
User (Primary)  
**Assumptions:**  
**Steps:**  
* User selects states from the map of the United States  
* The energy outlook of the state is shown from the interactive map

**Issues:**  
How to implement?  

### 2. Optimization of Local Energy Structure.  
**Use Case Name:**  
optimization of local energy structure.  
**Description:**  
according to the cost and developing trend of different energy type, we can offer advice to investors and companies, which would be helpful for the future plan of clean energy investment within different states.  
**Actors:**  
User (Primary)  
**Assumptions:**  
**Steps:**  
* calculate the cost of the four energy type and compare the past as well as future productive trends of them  
* compare their development potentials and come to the conclusion  

**Issues:**  
It might be hard to collect cost data for some of energies.

### Combine to one user case
###
**Use Case Name:**  
Clean energy(photovoltaic) industry outlook and energy source structure optimization  

**Description:**   
Using the energy sector information from the last 50 years, predict the market and need for solar energy in near future for a specific state.  

**Actors:**     
User input request a state   

**Assumptions:**  
* For one state, the total energy demands over the years will go up with the increase of popultation and economy. The energy supplied by traditional energy resource and clean energy resource will therefore, show a corresponding increase with varied growth rates.  
* A remarkable increase would be available in some areas with the advantage of solar radiation resource and other relevant technologies and during the period when solar cell development is much popular here.  
* The future of certain clean energy type (solar energy) may or may not be suitable for a specific state due to above reasons.  

**Steps:**  
* Based on the trend of different energy sectors (both clean and traditional) within a state, predict the demand and feasibility of solar energy development in the next 5 years.  
* With a specified state, the corresponding data prediction and visualization would be displayed.  
* With predictions for all states, we can generate an overall outlook of this type of clean energy in America.  

**Issues:**  
* How much weight does each factor has on the future of one kind of clean energy?  

## Figures/Interaction Diagrams

Figures/Interaction Diagrams go here.  

## Components

`interface`
* Use:  
Allows primary actor to view past data and future trends in clean energy for the selected state.  
* Input:  
User selects a state and the types of energy to view.  
* Output:  
Display past energy data and future trends of the selected energies for the selected state.  

`state_selector`  
* Use:  
* Input:  
* Output:  

`regression`  
* Use:  
Performs regression on the training data and displays plot of future trends based on user specifications.  
* Input:  
State and types of energy selected by used.  
* Output:  
Plot of future energy trends for a particular state.  

`solar_energy_economics`  
* Use:  
Predicts installation costs for PV energy based on future trends.  
* Input:  
State, The Open PV Project, Future trends in solar energy, and year under consideration.  
* Output:  
Predicted installation cost based on past costs.  

`wind_energy_economics`
* Use:  
* Input:  
* Output:  

`hydro_energy_economics`
* Use:  
* Input:  
* Output:  

`nuclear_energy_economics`
* Use:  
* Input:  
* Output:  

## Notes
* Not sure how to build GUI.
* Still looking for datasets for wind, hydro, and nuclear energy economics.
* Possibility to include more datasets.
