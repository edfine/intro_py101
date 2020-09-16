import pandas as pd

stocks = pd.read_csv('stocks_5yr.csv')
print(stocks.columns)
stocks.info()

#What is unusual about the first row? 
print('They are the column names!')
print(stocks.columns)

# How many dates are there? 
print(f"There are {len(stocks['date'].unique())} dates.")

# How many stocks? 
print(f'There are {len(stocks["Name"].unique())} stocks.')

# For each stock, what is the max volume? 
print('For each stock the max volume is:')
print(stocks.groupby(["Name"])["volume"].max())

# What is the date of the max close price, and what was the close on that date?
def find_max(grp):
    # find max value per row, then find index of row with max val
    max_row_idx = grp[["close"]].max(axis=1).idxmax()
    return grp.loc[max_row_idx]

print(stocks.groupby(['Name'])['date', 'close'].apply(find_max))
