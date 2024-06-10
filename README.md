# NYC Energy Consumption


# How to run the codebase

## create vitual environment

```bash 
# Navigate to your project directory
cd /path/to/your/project

# Create a virtual environment named 'venv'
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Deactivate the virtual environment
deactivate

# when install a packages do
 pip freeze > requirements.txt 


 # Install dependencies from requirements.txt
pip install -r requirements.txt
```
Group Members

Harrison, Zaigham, Gayane, Emmanuel Awe


## Background research
https://www.urbangreencouncil.org/new-york-citys-2020-energy-and-water-use-report/
https://www.eia.gov/state/?sid=NY#tabs-1
https://climate.cityofnewyork.us/subtopics/systems/
https://energy.cusp.nyu.edu/#/
https://www.sciencedirect.com/science/article/abs/pii/S2210670721007381

As New York City aims to transition to renewable electricity by 2030, it is crucial to monitor and manage energy usage effectively. In 2022, renewable sources and nuclear power collectively supplied 51% of the city's total in-state energy consumption. New York City exhibits lower per capita energy consumption compared to most states, with particularly reduced energy usage in the transportation sector. Due to the growing population, water and power usage has increased significantly in the city.

## Problem Definition

The NYC Energy Dashboard allows the city to track energy usage across its facilities, pinpointing areas for improvement. Analyzing data from energy companies provides insights into citywide energy trends, informing policy decisions to reduce carbon emissions.

## Value
This project will help us to complete an analysis of energy usage in New York City. We will be able to determine how weather metrics such as humidity levels, wind speed and temperatures affect energy usage in the city. aGiven the size of the city and the amount of energy usage,  this analysis can help generate interesting insights that could be applied to similar urban centers across the world.

## Limitations
● data quality issues
● inaccurate information




## Solutions
● Data cleaning
● improved data structures 

Datasets
We will be using datasets from the OpenNYC portal that are related to the energy usage in NYC as well as weather metric datasets from NOAA

## Database/store setup
We will compile an excel sheet with the dataset and the name and description of each column in the dataset. After choosing which columns we want to use for analysis, we will create a python script that transfers the data to PostgreSQL. We will then add an ID column into the table and formulate several SQL queries to analyze the dataset. Finally, we will design the structure of the database using Raw, Clean and final stages

