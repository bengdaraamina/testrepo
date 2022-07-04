#display the output
print("new peython file")
Final Assignment Statistics for Data Science
import numpy as np
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt 
import scipy.stats as stats
boston_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ST0151EN-SkillsNetwork/labs/boston_housing.csv'
boston_df=pd.read_csv(boston_url)
boston_df.head()
Unnamed: 0	CRIM	ZN	INDUS	CHAS	NOX	RM	AGE	DIS	RAD	TAX	PTRATIO	LSTAT	MEDV
0	0	0.00632	18.0	2.31	0.0	0.538	6.575	65.2	4.0900	1.0	296.0	15.3	4.98	24.0
1	1	0.02731	0.0	7.07	0.0	0.469	6.421	78.9	4.9671	2.0	242.0	17.8	9.14	21.6
2	2	0.02729	0.0	7.07	0.0	0.469	7.185	61.1	4.9671	2.0	242.0	17.8	4.03	34.7
3	3	0.03237	0.0	2.18	0.0	0.458	6.998	45.8	6.0622	3.0	222.0	18.7	2.94	33.4
4	4	0.06905	0.0	2.18	0.0	0.458	7.147	54.2	6.0622	3.0	222.0	18.7	5.33	36.2
sns.boxplot(x="CHAS", y="MEDV", data=boston_df).set_title('Median value depending on river Charles boundness')
Text(0.5, 1.0, 'Median value depending on river Charles boundness')

sns.boxplot(y="MEDV", data=boston_df).set_title('Median value')
Text(0.5, 1.0, 'Median value')

Explanation The median value is slightlz above 20

sns.catplot(x="CHAS", kind='count', data=boston_df)
<seaborn.axisgrid.FacetGrid at 0x7f14a4372a10>

Explanation: There are many more houses not river Charles bound than Charles bound houses

boston_df.loc[(boston_df['AGE'] <= 35), 'AGE_group'] = '35 years and younger'
boston_df.loc[(boston_df['AGE'] > 35)&(boston_df['AGE'] < 70), 'AGE_group'] = 'between 35 and 70 years'
boston_df.loc[(boston_df['AGE'] >= 70), 'AGE_group'] = '70 years and older'
#boston_df.loc[(boston_df['AGE'] <= 70), 'AGE_group'] = 'younger than 70 years'
sns.boxplot(x="AGE_group", y="MEDV", data=boston_df).set_title('Median values for different age groups')
Text(0.5, 1.0, 'Median values for different age groups')

Explanation: the younger the age, the higher the median value

sns.scatterplot(x='NOX', y='INDUS', data=boston_df).set_title('Nitric oxide concentrations vs non-retail business acres per town')
#sns.scatterplot(x='INDUS', y='NOX', data=boston_df)
Text(0.5, 1.0, 'Nitric oxide concentrations vs non-retail business acres per town')

The nitrox oxcide concentrations plotted agains the acres of non retail businesses per town

boston_df["PTRATIO"].plot(kind="hist")
plt.title ("Pupil to Teacher ratio")
plt.show()

Explanation: The amount of towns with certain pupil to teacher ratios

f, ax = plt.subplots(figsize=(18, 3))
sns.countplot(x="PTRATIO", data=boston_df).set_title('Count of pupil-teacher ratio by town')
Text(0.5, 1.0, 'Count of pupil-teacher ratio by town')

Is there a significant difference in median value of houses bounded by the Charles river or not?
Hypothesis
Null Hypothesis There is no significant difference in the median values of houses which are bound by the Charles river and those which are not

Alternate Hypothesis There is a significant difference in the median values of houses which are bound by the Charles river and those which are not

sns.boxplot(x="CHAS", y="MEDV", data=boston_df).set_title('Median value depending on river Charles boundness')
Text(0.5, 1.0, 'Median value depending on river Charles boundness')

T-test for independent samples
stats.ttest_ind(boston_df[boston_df['CHAS'] == 0.0]['MEDV'], boston_df[boston_df['CHAS'] == 1.0]['MEDV'], equal_var = False)
Ttest_indResult(statistic=-3.113291312794837, pvalue=0.003567170098137517)
Conclusion
The p-Value is much smaller than  α=0.05 . Hence we reject the hypothesis and conclude that there is a significant difference in the median values of houses depending on being bound to Charles river and not

Is there a difference in Median values of houses (MEDV) for each proportion of owner occupied units built prior to 1940 (AGE)?
Hypothesis
Null Hypothesis There is no difference in median values for each proportion of owner occupied units built prior to 1940

Alternate Hypothesis There is a difference in median values for each proportion of owner occupied units built prior to 1940

ANOVA
sns.boxplot(x="AGE_group", y="MEDV", data=boston_df).set_title('Median values for different age groups')
Text(0.5, 1.0, 'Median values for different age groups')

younger_thirtyfive=boston_df[boston_df['AGE_group'] == '35 years and younger']['MEDV']
thirtyfive_to_seventy= boston_df[boston_df['AGE_group'] == 'between 35 and 70 years']['MEDV']
#up_to_seventy= boston_df[boston_df['AGE_group'] == 'younger than 70 years']['MEDV']
older_seventy= boston_df[boston_df['AGE_group'] == '70 years and older']['MEDV']
stats.levene(younger_thirtyfive, thirtyfive_to_seventy, older_seventy, center='mean')
# the p-value is greater than 0.05, the variance are equal
LeveneResult(statistic=2.7806200293748304, pvalue=0.06295337343259205)
f_statistic, p_value = stats.f_oneway(younger_thirtyfive, thirtyfive_to_seventy, older_seventy)
print("F_Statistic: {0}, P-Value: {1}".format(f_statistic,p_value))
F_Statistic: 36.40764999196599, P-Value: 1.7105011022702984e-15
Conclusion
Since the p-value is smaller than  α=0.05 , we will reject the null hypothesis

Can we conclude that there is no relationship between Nitric oxide concentrations and proportion of non-retail business acres per town?
Hypothesis
Null Hypothesis There is no relationship between Nitric oxide concentrations and proportion of non-retail business acres per town

Alternate Hypothesis There is a relationship between Nitric oxide concentrations and proportion of non-retail business acres per town

sns.scatterplot(x='NOX', y='INDUS', data=boston_df).set_title('Nitric oxide concentrations vs non-retail business acree per town')
Text(0.5, 1.0, 'Nitric oxide concentrations vs non-retail business acree per town')

Pearson Correlation
stats.pearsonr(boston_df['NOX'], boston_df['INDUS'])
(0.763651446920915, 7.913361061239593e-98)
Conclusion
Since the p-value is smaller than  α=0.05 , we reject the null hypothesis.

What is the impact of an additional weighted distance to the five Boston employment centres on the median value of owner occupied homes?
Hypothesis
Null Hypothesis An additional weighted distance to the five Boston employment centres has no impact on the median value of owner occupied homes

Alternate Hypothesis An additional weighted distance to the five Boston employment centres has an impact on the median value of owner occupied homes

sns.scatterplot(x="DIS", y="MEDV", data=boston_df).set_title('Distance to employment centres vs Median values')
Text(0.5, 1.0, 'Distance to employment centres vs Median values')

Regression analysis
## X is the input variables (or independent variables)
X = boston_df['DIS']
## y is the target/dependent variable
y = boston_df['MEDV']
## add an intercept (beta_0) to our model
X = sm.add_constant(X) 

model = sm.OLS(y, X).fit()
predictions = model.predict(X)

# Print out the statistics
model.summary()
OLS Regression Results
Dep. Variable:	MEDV	R-squared:	0.062
Model:	OLS	Adj. R-squared:	0.061
Method:	Least Squares	F-statistic:	33.58
Date:	Sun, 07 Feb 2021	Prob (F-statistic):	1.21e-08
Time:	18:51:49	Log-Likelihood:	-1823.9
No. Observations:	506	AIC:	3652.
Df Residuals:	504	BIC:	3660.
Df Model:	1		
Covariance Type:	nonrobust		
coef	std err	t	P>|t|	[0.025	0.975]
const	18.3901	0.817	22.499	0.000	16.784	19.996
DIS	1.0916	0.188	5.795	0.000	0.722	1.462
Omnibus:	139.779	Durbin-Watson:	0.570
Prob(Omnibus):	0.000	Jarque-Bera (JB):	305.104
Skew:	1.466	Prob(JB):	5.59e-67
Kurtosis:	5.424	Cond. No.	9.32


Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
Conclusion
Since p < 0.05 there is evidence of correlation between the weighted distance to the five Boston employment centres and the median value of owner occupied homes.  R2=0.62  and the coefficient is 0.79.
