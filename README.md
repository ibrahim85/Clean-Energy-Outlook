<img src = "Clean-Energy-Outlook/doc/Images/Logo.jpg">

### Due Mar. 15, 2017 at 5PM

### Project Description
**Clean Energy Outlook** is a software that reads in energy generation data from 1960 to 2014 of various states of the United States as well as other data like GDP, climate, oil price, and other factors and predicts the renewable energy generation of each state for the next 5 years. Software will be useful for investors and policy makers in renewable energy. Investors in clean energy can use this software to identify states where clean energy has high potential. Policy makers can also use this software to develop clean energy policies for different states.  

A regression model is used to predict the clean energy produced in the next 5 years for every state. Machine Learning algorithms like Linear Regression, Ridge Regression, and Lasso Regression from the scikit-learn library in Python are used to perform the regression. The output is an interactive map on Tableau with a time slider for the year and displays the amount of solar, wind, hydro, and nuclear energy produced in all the states for that particular year. It also has a drop down menu to select a state and view the trend of these 4 energies for the state selected with the projections for the future.  

### License Choice
We choose MIT License since it is a permissive license that is short and to the point. It lets people do anything they want with our code as long as they provide attribution back to us and don’t hold us liable.  

### Data Sources
All data sources are open source and can easily be downloaded.
* State Energy Data System (https://www.eia.gov/state/seds/seds-data-complete.php)
* Domestic Crude Oil Prices (in $/Barrel) (http://inflationdata.com/Inflation/Inflation_Rate/Historical_Oil_Prices_Table.asp)
* Gross Domestic Product by State (https://www.bea.gov/iTable/iTable.cfm?reqid=70&step=1&isuri=1&acrdn=2%23reqid=70&step=1&isuri=1#reqid=70&step=1&isuri=1)
* Climate
* NOAA Satellite and Information Service (https://www7.ncdc.noaa.gov/CDO/CDODivisionalSelect.jsp)

### Software Dependencies

All data cleaning and machine learning algorithms are written in Python 3.5 using open source libraries.  
The libraries used are:
* scikit-learn  
* pandas  
* numpy  

Visualizations are done using Tableau software.

### Directory Structure
Here is a simple tree plot of the current structure:
```
├── LICENSE
├── README.md
├── Clean-Energy-Outlook
│   ├── Data
│   │   ├── Actual Data
│   │   ├── Cleaned Data
│   ├── Machine Learning
│   │   ├── Ridge Regression
│   │   ├── LASSO Regression
│   │   ├── Simple Linear Regression
│   ├── Documentation
│   ├── Visualization
│   ├── Testing
```
### Flow Map  

<img src = "Clean-Energy-Outlook/doc/flowchart.png">

### Contributors
* Hanyang Xu
* Kejia Wu
* Rahul Avadhoot
* Richard Zhang

### Acknowledgements
* David Beck
* Jim Pfaendtner
