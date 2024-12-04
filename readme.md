## Second Exam Work & Results Summary
### Question 1
- created a shell script, prepare.sh, that performed data cleaning on the dirty dataset ms_data_dirty.csv
- cleaned ms_data_dirty.csv file over 4 steps, final product was saved as ms_data.csv
- printed summary of the ms_data.csv dataset & row count
- insurance file, insurance.lst was created, with 4 levels of insurance status (Bronze, Silver, Gold, Platinum) added to this file
- ms_data.csv differences from the initial raw file: no double commas, no empty lines, no comments, only 5 essential columns included
### Question 2
- the updated csv file ms_data.csv was read in as ms_data
- [visit_date] column was converted to datetime format
- 5 columns were confirmed to be of appropriate data type
- the only column with missing values was walking_speed, so missing values were filled with the median value in that column
- the dataset was sorted by both patient_id and visit_date
- insurance types were randomly assigned to each patient, including appropriately corresponding costs (with random variation incorporated)
- the new cleaned dataset was saved as a new csv file, ms_data_new.csv for use in future questions
-groupby() was used for aggregations to print summary statistics
### Question 3
- in order to perform linear regression using statsmodels, needed to convert education_level to a numeric format (using a label encoder)
- Multiple Regression with Education and Age on Walking Speed: The coefficients for education level and age in the linear model were -0.215 and -0.0262, respectively. All results were statistically significant. The r-squared value was 0.52.

- Cost analysis: As insurance type increased (bronze to silver to gold to platinum), costs decreased per visit. The r-squared value was 0.1097, with very small p-values indicating that all results were statistically significant.

- Advanced analysis: The model showed that the most significant association between a predictor variable and walking speed was education level. The least strong association was with visit cost. All p-values were very small. The coefficient of the age-edu-effects column was very small at 0.00049, with a very small p-value as well, indicating that there is a minimal but statistically significant interaction effect between age and education.

### Question 4
1. Walking Speed Analysis Section
-seaborn was used for all 3 of these plots
- Scatter plot of age vs. walking speed: linear regression model with regression line shown tells us that as age increases, walking speed decreases
- Box plots of walking speed by education level: As education level increases, walking speed also increases. Patients with higher levels of education showed better results in their walking speeds.
- Education/Age interaction lineplot: education level had less of an impact on walking speed in younger age groups; as age increased, education level more clearly associated with walking speed (higher education, higher walking speed)

2. Cost Analysis Section
- seaborn used for both plots
- Barplot of Costs by Insurance Type: As designed, patients with the most premium insurance plan, Platinum, had the lowest visit costs, followed by Gold, Silver, then Bronze
- Box Plots of Cost Distributions: Bronze insurance has the greatest spread in its cost distribution, while Platinum insurance has the narrowest range of costs

3. Combined Visualizations
- pairplot shows all possible pairs of key variables, distributions of patients with respect to all key variables
- faceted plot shows insurance type count by education level: insurance counts are fairly constant across all education levels, they were randomly assigned to patients irrespective of education. With real non-simulated data, we may have expected higher education levels to correlate with the higher insurance plans (ie: Gold, Platinum)
- Time trends: Walking speeds seem to fluctuate randomly but do not seem to vary seasonally or by visit-date according to the time trend plot