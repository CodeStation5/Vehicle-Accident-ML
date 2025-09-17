# Vehicle-Accident-ML

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)  
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)  
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-yellow)  
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-lightblue)  
![Matplotlib](https://img.shields.io/badge/Matplotlib-Charts-green)  
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)  
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

---

## Overview

**Vehicle-Accident-ML** is a machine learning project designed to predict the likelihood and severity of motor vehicle accidents using historical accident data. The goal is to identify key contributing factors (weather, road conditions, time, etc.) and improve accident prevention strategies for autonomous vehicles and safety-focused applications.

This project was developed as part of a capstone project and includes:

- Data ingestion and preprocessing  
- Exploratory Data Analysis (EDA)  
- Predictive modeling using multiple ML algorithms  
- Interactive visualizations and user input sliders  
- Accuracy assessment using test data  

---

## Dataset

- **Source**: [Car Accident Dataset – Kaggle](https://www.kaggle.com/datasets/nextmillionaire/car-accident-dataset/data)  
- **Scope**: Road accidents in Kensington and Chelsea, Jan 2021  
- **Features**:  
  - Date & time  
  - Location  
  - Light & weather conditions  
  - Vehicle count  
  - Accident severity  

The dataset is preprocessed with **Pandas** and visualized using **Seaborn** and **Matplotlib**.

---

## Installation

Clone the repo:
`git clone https://github.com/CodeStation5/Vehicle-Accident-ML.git
cd Vehicle-Accident-ML
`

Install dependencies:
`pip install -r requirements.txt`

Run the Jupyter Notebook:
`jupyter notebook main.ipynb`


## Results

- Achieved **91.1% accuracy** on predicting accident likelihood using 2021 data against 2022 test data.  
- Random Forest performed best among tested models.  
- **Key predictors** included:  
  - Weather conditions  
  - Time of day / day of week  
  - Location of accident
