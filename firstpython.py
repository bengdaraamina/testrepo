#display the output
print("new python file")
Final Assignment Statistics for Data Science
import numpy as np
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt 
import scipy.stats as stats
import scipy.stats
ratings_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ST0151EN-SkillsNetwork/labs/teachingratings.csv'
ratings_df = pd.read_csv(ratings_url)

## X is the input variables (or independent variables)
X = ratings_df['female']
## y is the target/dependent variable
y = ratings_df['eval']
## add an intercept (beta_0) to our model
X = sm.add_constant(X) 

model = sm.OLS(y, X).fit()
predictions = model.predict(X)

# Print out the statistics
model.summary()
sns.boxplot(x="CHAS", y="MEDV", data=ratings_df).set_title('Median value depending on river Charles boundness')
Text(0.5, 1.0, 'Median value depending on river Charles boundness')

sns.boxplot(y="MEDV", data=ratings_df).set_title('Median value')
Text(0.5, 1.0, 'Median value')


sns.catplot(x="CHAS", kind='count', data=ratings_df)
<seaborn.axisgrid.FacetGrid at 0x7f14a4372a10>

Explanation: There are many more houses not river Charles bound than Charles bound houses

ratings_df.loc[(ratings_df['age'] <= 40), 'age_group'] = '40 years and younger'
ratings_df.loc[(ratings_df['age'] > 40)&(ratings_df['age'] < 57), 'age_group'] = 'between 40 and 57 years'
ratings_df.loc[(ratings_df['age'] >= 57), 'age_group'] = '57 years and older'
#boston_df.loc[(boston_df['AGE'] <= 70), 'AGE_group'] = 'younger than 70 years'
sns.boxplot(x="AGE_group", y="MEDV", data=ratings_df).set_title('Median values for different age groups')
Text(0.5, 1.0, 'Median values for different age groups')
from statsmodels.formula.api import ols
lm = ols('beauty ~ age_group', data = ratings_df).fit()
table= sm.stats.anova_lm(lm)
print(table)

Explanation: the younger the age, the higher the median value

  X = pd.get_dummies(ratings_df[['age_group']])
  
  y = ratings_df['beauty']
## add an intercept (beta_0) to our model
X = sm.add_constant(X) 

model = sm.OLS(y, X).fit()
predictions = model.predict(X)

# Print out the statistics
model.summary()
## X is the input variables (or independent variables)
X = ratings_df['beauty']
## y is the target/dependent variable
y = ratings_df['eval']
## add an intercept (beta_0) to our model
X = sm.add_constant(X) 

model = sm.OLS(y, X).fit()
predictions = model.predict(X)

# Print out the statistics
model.summary()
ax = sns.distplot(ratings_df['eval'],
                  bins=20,
                  kde=True,
                  color='red',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Normal Distribution', ylabel='Frequency')
## we can assume it is normal

scipy.stats.levene(ratings_df[ratings_df['gender'] == 'female']['eval'],
                   ratings_df[ratings_df['gender'] == 'male']['eval'], center='mean')

# since the p-value is greater than 0.05 we can assume equality of variance


sns.scatterplot(x='NOX', y='INDUS', data=ratings_df).set_title('Nitric oxide concentrations vs non-retail business acres per town')
#sns.scatterplot(x='INDUS', y='NOX', data=ratings_df

scipy.stats.ttest_ind(ratings_df[ratings_df['gender'] == 'female']['eval'],
                   ratings_df[ratings_df['gender'] == 'male']['eval'], equal_var = True)


ratings_df.loc[(ratings_df['age'] <= 40), 'age_group'] = '40 years and younger'
ratings_df.loc[(ratings_df['age'] > 40)&(ratings_df['age'] < 57), 'age_group'] = 'between 40 and 57 years'
ratings_df.loc[(ratings_df['age'] >= 57), 'age_group'] = '57 years and older'

scipy.stats.levene(ratings_df[ratings_df['age_group'] == '40 years and younger']['beauty'],
                   ratings_df[ratings_df['age_group'] == 'between 40 and 57 years']['beauty'], 
                   ratings_df[ratings_df['age_group'] == '57 years and older']['beauty'], 
                   center='mean')
# since the p-value is less than 0.05, the variance are not equal, for the purposes of this exercise, we will move along

forty_lower = ratings_df[ratings_df['age_group'] == '40 years and younger']['beauty']
forty_fiftyseven = ratings_df[ratings_df['age_group'] == 'between 40 and 57 years']['beauty']
fiftyseven_older = ratings_df[ratings_df['age_group'] == '57 years and older']['beauty']

f_statistic, p_value = scipy.stats.f_oneway(forty_lower, forty_fiftyseven, fiftyseven_older)
print("F_Statistic: {0}, P-Value: {1}".format(f_statistic,p_value))

forty_lower_eval = ratings_df[ratings_df['age_group'] == '40 years and younger']['eval']
forty_fiftyseven_eval = ratings_df[ratings_df['age_group'] == 'between 40 and 57 years']['eval']
fiftyseven_older_eval = ratings_df[ratings_df['age_group'] == '57 years and older']['eval']

f_statistic, p_value = scipy.stats.f_oneway(forty_lower_eval, forty_fiftyseven_eval, fiftyseven_older_eval)
print("F_Statistic: {0}, P-Value: {1}".format(f_statistic,p_value))

cont_table  = pd.crosstab(ratings_df['tenure'], ratings_df['gender'])
cont_table

scipy.stats.chi2_contingency(cont_table, correction = True)
ax = sns.scatterplot(x="beauty", y="eval", data=ratings_df)
scipy.stats.pearsonr(ratings_df['beauty'], ratings_df['eval']))
Text(0.5, 1.0, 'Nitric oxide concentrations vs non-retail business acres per town')

The nitrox oxcide concentrations plotted agains the acres of non retail businesses per town

ratings_df["PTRATIO"].plot(kind="hist")
plt.title ("Pupil to Teacher ratio")
plt.show()

Explanation: The amount of towns with certain pupil to teacher ratios

f, ax = plt.subplots(figsize=(18, 3))
sns.countplot(x="PTRATIO", data=ratings_df).set_title('Count of pupil-teacher ratio by town')
Text(0.5, 1.0, 'Count of pupil-teacher ratio by town')


sns.boxplot(x="CHAS", y="MEDV", data=boston_df).set_title('Median value depending on river Charles boundness')
Text(0.5, 1.0, 'Median value depending on river Charles boundness')

T-test for independent samples
stats.ttest_ind(boston_df[ratings_df['CHAS'] == 0.0]['MEDV'], boston_df[ratings_df['CHAS'] == 1.0]['MEDV'], equal_var = False)
Ttest_indResult(statistic=-3.113291312794837, pvalue=0.003567170098137517)
Conclusion
The p-Value is much smaller than  α=0.05 . Hence we reject the hypothesis and conclude that there is a significant difference in the median values of houses depending on being bound to Charles river and not


ANOVA
sns.boxplot(x="AGE_group", y="MEDV", data=ratings_df).set_title('Median values for different age groups')
Text(0.5, 1.0, 'Median values for different age groups')

younger_thirtyfive=boston_df[ratings_df['AGE_group'] == '35 years and younger']['MEDV']
thirtyfive_to_seventy= ratings_df[ratings_df['AGE_group'] == 'between 35 and 70 years']['MEDV']
#up_to_seventy= boston_df[boston_df['AGE_group'] == 'younger than 70 years']['MEDV']
older_seventy= ratings_df[ratings_df['AGE_group'] == '70 years and older']['MEDV']
stats.levene(younger_thirtyfive, thirtyfive_to_seventy, older_seventy, center='mean')


# the p-value is greater than 0.05, the variance are equal
LeveneResult(statistic=2.7806200293748304, pvalue=0.06295337343259205)
f_statistic, p_value = stats.f_oneway(younger_thirtyfive, thirtyfive_to_seventy, older_seventy)
print("F_Statistic: {0}, P-Value: {1}".format(f_statistic,p_value))
F_Statistic: 36.40764999196599, P-Value: 1.7105011022702984e-15

sns.scatterplot(x='NOX', y='INDUS', data=ratings_df).set_title('Nitric oxide concentrations vs non-retail business acree per town')
Text(0.5, 1.0, 'Nitric oxide concentrations vs non-retail business acree per town')

Pearson Correlation
stats.pearsonr(ratings_df['NOX'], ratings_df['INDUS'])
(0.763651446920915, 7.913361061239593e-98)
Conclusion
Since the p-value is smaller than  α=0.05 , we reject the null hypothesis.


sns.scatterplot(x="DIS", y="MEDV", data=ratings_df).set_title('Distance to employment centres vs Median values')
Text(0.5, 1.0, 'Distance to employment centres vs Median values')

Regression analysis
## X is the input variables (or independent variables)
X = ratings_df['DIS']
## y is the target/dependent variable
y = ratings_df['MEDV']
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


