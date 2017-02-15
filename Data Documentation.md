## State Energy Data System (SEDS): 1960-2014
* **Description:**  
Energy production and consumption data from multiple sources like coal, natural gas, wind, hydro, solar nuclear for all the states of the United States.
* **Link**  
https://www.eia.gov/state/seds/seds-data-complete.php
* **Dimensionality:**  
58 columns, covering year 1960 to 2014  
* **Size:**  
6660 rows, covering multiple energy sectors for all 50 states  
* **Data Model:**  
Specific columns to focus on:  
**HYTCP**  
Hydroelectricity, total net generation  
**WYTCP**  
Wind electricity, total net generation  
**SOEGP**  
Photovoltaic and solar thermal electricity net generation in the electric power sector  
**NUETP**  
Nuclear electricity, total net generation  
* **Creating Subset:**  
It is relatively simple to create a subset of the data by considering only a few columns. It is also possible to extract data between specific years. This would be useful to perform unit tests.

## The Open PV Project
* **Description:**  
Summary of photovoltaic system installations in the United States.
* **Link**  
https://openpv.nrel.gov
* **Dimensionality:**  
30 Columns, covering State, zip code, date installed, size, cost per watt etc.
* **Size:**  
1020264 rows, covering all PV projects in the United States
* **Data Model:**  
Specific columns to focus on:
State, Size (in kW), Cost, year
* **Creating Subsets:**  
It is simple to create subsets by selecting a particular state and using values of a single year (like 2012) to perform unit tests.
