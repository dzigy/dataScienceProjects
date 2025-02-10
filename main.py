import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

originalData = pd.read_excel('D598 Data Set.xlsx')
# Import the data file into a data frame
df = pd.DataFrame(originalData)
print('Print data')
print(df)

# Identify any duplicate rows in the data set.
print('Check for duplicates')
print(df.duplicated())

print('Check data types')
print(df.dtypes)

numericColumns = ['Total Long-term Debt', 'Total Equity', 'Debt to Equity',
                  'Total Liabilities', 'Total Revenue', 'Profit Margin']

# Group all IDs by state, then run descriptive statistics (mean, median, min, & max) for all numeric variables by state
descriptiveStats = df.groupby('Business State')[numericColumns].describe()
print('Descriptive Statistics print by State:')
print(descriptiveStats)

# store the result as a new data frame
descriptiveStats_df = descriptiveStats.reset_index()
print('Descriptive Statistics print by State:')
print(descriptiveStats_df)

# Filter the data frame to identify all businesses with debt-to-equity ratios that are negative.
negativeDebtToEquity = df[df['Debt to Equity'] < 0]
print('Print Businesses with debt-to-equity ratios that are negative.')
print(negativeDebtToEquity)

# Create a new data frame that provides the debt-to-income ratio for every business in the data set.
# Debt-to-income ratio is defined as long-term debt divided by revenue.
debtToIncomeRatio_df = df['Total Long-term Debt'] / df['Total Revenue']
print('debt-to-income ratio for every business')
print(debtToIncomeRatio_df)

# Concatenate the debt-to-income ratio data frame created with the original data frame.
concatenated_df = pd.concat([df, debtToIncomeRatio_df], axis=1)
print('Concatenated Data Frame')
print(concatenated_df)

# Bar plot - average Debt-to-Equity ratio by state
plt.figure(figsize=(10, 6))
avg_debt_to_equity = df.groupby('Business State')['Debt to Equity'].mean()
avg_debt_to_equity.plot(kind='bar', color='green')
plt.title('Average Debt to Equity Ratio by State')
plt.xlabel('State')
plt.ylabel('Average Debt to Equity')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Box plot - Debt to Equity ratio
plt.figure(figsize=(10, 6))
sns.boxplot(x='Business State', y='Debt to Equity', data=df, palette='Set2')
plt.title('Debt to Equity Ratio by State')
plt.xlabel('State')
plt.ylabel('Debt to Equity')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Scatter plot - Total Long-term Debt and Total Revenue
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Total Long-term Debt', y='Total Revenue', data=df, hue='Business State', palette='Set1')
plt.title('Scatter Plot: Total Long-term Debt vs Total Revenue')
plt.xlabel('Total Long-term Debt')
plt.ylabel('Total Revenue')
plt.tight_layout()
plt.show()

# Bar Chart - Sum of Total Revenue by State
plt.figure(figsize=(10, 6))
revenue_by_state = df.groupby('Business State')['Total Revenue'].sum()
revenue_by_state.plot(kind='bar', color='lightgreen')
plt.title('Sum of Total Revenue by State')
plt.xlabel('State')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
