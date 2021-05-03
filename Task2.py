import pandas as pd

# Boilerplate to simulate the author initial condition
# Creating a sample CSV file with a 1Hz resolution
df = pd.DataFrame()
df['time'] = pd.date_range(start='2020-01-08', periods=3000, freq='s')
df.to_csv(path_or_buf="input.csv",index=False)

# Read the file
df = pd.read_csv('input.csv')
# Convert to datetime
df['time'] = pd.to_datetime(df['time'])
# Resampling down to 0.1Hz
df = df.resample('10s', on='time').first()
df.to_csv(path_or_buf="output.csv",index=False)