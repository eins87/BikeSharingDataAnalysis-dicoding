# Dicoding - Final Project 
## Description
Bikes Sharing Data Analysis - Final Project

## Folder Structure 
```
|dashboard  
|├───all.csv  
|└───dashboard.py  
|data  
|├───day.csv  
|└───hour.csv  
|notebook.ipynb  
|README.md  
|requirements.txt  
```

## Setup environment
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit babel
```

## Run streamlit app
```
cd bikesharingdataanalisis-dicoding
streamlit run dashboard/dashboard.py
```
