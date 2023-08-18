# You have to delete some rows first after you download the csv from Interactive Brockers 
import pandas as pd

df = pd.read_csv('jesse_stocks.csv')
df.drop(columns=['Open Position Summary', 'Header', 'Date', 'FinancialInstrument', 'Currency',
                 'Quantity', 'ClosePrice', 'Value', 'FXRateToBase'], inplace=True)

df.loc[df['Symbol'] == 'ECH', 'Sector'] = 'Country'
df.loc[df['Symbol'] == 'ECNS', 'Sector'] = 'Country'
df.loc[df['Symbol'] == 'EIDO', 'Sector'] = 'Country'
df.loc[df['Symbol'] == 'EPHE', 'Sector'] = 'Country'
df.loc[df['Symbol'] == 'EWA', 'Sector'] = 'Country'
df.loc[df['Symbol'] == 'EWW', 'Sector'] = 'Country'
df.loc[df['Symbol'] == 'EWZ', 'Sector'] = 'Country'
df.loc[df['Symbol'] == 'EZA', 'Sector'] = 'Country'
df.loc[df['Symbol'] == 'FXI', 'Sector'] = 'Country'
df.loc[df['Symbol'] == 'INDA', 'Sector'] = 'Country'
df.loc[df['Symbol'] == 'NGE', 'Sector'] = 'Country'
df.loc[df['Symbol'] == 'TUR', 'Sector'] = 'Country'
df.loc[df['Symbol'] == 'VNAM', 'Sector'] = 'Country'
df.loc[df['Symbol'] == 'VNAM', 'Sector'] = 'Country'
df.loc[df['Symbol'] == 'VOO', 'Sector'] = 'Country'

df.rename(columns={'Symbol': 'symbol', 'Description': 'description', 'Sector': 'sector', 'Cost Basis': 'value', 'UnrealizedP&L': 'profit_loss'}, inplace=True)

# if I want to scale money by 10000
# total_value = df['value'].sum()
# scaling_factor = 10000 / total_value
# df['value'] = df['value'] * scaling_factor 
# df['profit_loss'] = df['profit_loss'] * scaling_factor
# df['percent_change'] = df['profit_loss'] / df['value'] * 100

df['percent_change'] = df['profit_loss'] / df['value'] * 100

df.to_csv('jesse_stocks_cleaned.csv', index=False)