import pandas as pd

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

# Concatenate the debt-to-income ratio data frame you created with the original data frame.
concatenated_df = pd.concat([df, debtToIncomeRatio_df], axis=1)
print('Concatenated Data Frame')
print(concatenated_df)
