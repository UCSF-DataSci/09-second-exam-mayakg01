import statsmodels.api as sm
from scipy import stats
import pandas as pd
ms_df = pd.read_csv('ms_data_new.csv')
#analyzing walking speed
#converting education_level to numeric format so that it can be used in regression model
from sklearn.preprocessing import LabelEncoder
levels = LabelEncoder()
ms_df['education_level'] = levels.fit_transform(ms_df['education_level'])
#checking for outliers in age variable
#calculating the IQR to determine upper/lower bounds
Q1 = ms_df['age'].quantile(0.25)
Q3 = ms_df['age'].quantile(0.75)
IQR = Q3 -Q1
lower_bound  = Q1 - 1.5*IQR
upper_bound = Q3 + 1.5*IQR
print(lower_bound)
print(upper_bound)
#there are no values below the lower bound or above the upper bound, therefore no outliers in age
#checking for outliers in walking speed variable
#calculating IQR to determine bounds
Q1_w = ms_df['walking_speed'].quantile(0.25)
Q3_w = ms_df['walking_speed'].quantile(0.75)
IQR_w = Q3 -Q1
lower_bound_ws = Q1_w - 1.5*IQR_w
upper_bound_ws = Q3_w + 1.5*IQR_w
print(lower_bound_ws)
print(upper_bound_ws)
#no outlier values of walking speed
#building multiple regression model
X = ms_df[['education_level','age']]
y = ms_df['walking_speed']
X = sm.add_constant(X)
lin_model = sm.OLS(y,X)
results = lin_model.fit()
print(results.params)
print(results.rsquared)
print(results.pvalues)
#analyzing costs
import matplotlib.pyplot as plt
#converting insurance type to numeric format
ins_levels = LabelEncoder()
ms_df['insurance_type'] = ins_levels.fit_transform(ms_df['insurance_type'])
X_cost = ms_df[['insurance_type']]
y_cost = ms_df['visit_cost']
X_cost = sm.add_constant(X_cost)
model_cost = sm.OLS(y_cost, X_cost)
results_cost = model_cost.fit()
print(results_cost.params)
print(results_cost.rsquared)
print(results_cost.pvalues)
plt.boxplot(results_cost.resid)
plt.show()
#interaction effects of education & age on walking speed
#creating another column representing the interaction between education & age
ms_df['age_edu_effects'] = ms_df['age'] * ms_df['education_level']
X_interact = ms_df[['age', 'education_level', 'age_edu_effects', 'insurance_type', 'visit_cost']]
X_interact = sm.add_constant(X_interact)
y_interact = ms_df['walking_speed']
int_model = sm.OLS(y_interact, X_interact).fit()
print(int_model.params)
print(int_model.pvalues)
print(int_model.rsquared)
