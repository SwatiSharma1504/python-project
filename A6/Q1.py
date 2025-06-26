import pandas as pd
date_strings = ['2023-01-01', '2023-01-02', '2023-01-03']
dates = pd.to_datetime(date_strings)
data = [10, 20, 15]
timeseries = pd.Series(data, index=dates)
print(timeseries)
