import pandas as pd
import numpy as np
import random
#loading and structuring data
ms_data = pd.read_csv('ms_data.csv')
ms_data['visit_date'] = pd.to_datetime(ms_data['visit_date'], format='%Y-%m-%d')
print(ms_data.dtypes)
#handling missing data
print(ms_data.isnull().sum())
#walking speed column missing values filled with median value
ms_data['walking_speed'] = ms_data['walking_speed'].fillna(ms_data['walking_speed'].median())
#sorting data
ms_sorted = ms_data.sort_values(['patient_id', 'visit_date'], ascending=[True, False])
print(ms_sorted.head())

#adding insurance information
#reading info from lst file
insurance_types = []
with open ('insurance.lst', 'r') as file:
    insurance_types = [line.strip() for line in file.readlines()]
#randomly assigning a type of insurance to every patient
np.random.seed(100)
#creating a dictionary to randomly assign insurance types, but keep consistent for each patient
patients = ms_sorted['patient_id'].unique()
ins_type = {patient_id: np.random.choice(insurance_types) for patient_id in patients}
ms_sorted['insurance_type'] = ms_sorted['patient_id'].map(ins_type)
print(ms_sorted.head())
#visit copay costs based on insurance type
ins_costs = {
    'Bronze': 400,
    'Silver': 300,
    'Gold': 150,
    'Platinum': 75
}
#adding random variation
ms_sorted['visit_cost'] = ms_sorted['insurance_type'].map(ins_costs) * (1+ np.random.uniform(-0.1, 0.1, size = len(ms_sorted)))
print(ms_sorted.head())
#saving modified data frame to an updated name
ms_data_new = ms_sorted.copy()
ms_data_new.to_csv('ms_data_new.csv', index=False)

#Summary statistics
#Mean walking speed by edu level
print(ms_sorted.groupby('education_level')['walking_speed'].mean())

#Mean costs by insurance type
print(ms_sorted.groupby('insurance_type')['visit_cost'].mean())
