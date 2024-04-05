# Library imports
from turtle import pd

# Dataset retrieval
dataUrl = 'https://raw.githubusercontent.com/Codestation5/Vehicle-Accident-ML/dataset/accident_data_CSV.csv'
reader = pd.read_csv(dataUrl)
x = reader['x']





