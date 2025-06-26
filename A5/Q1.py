import pandas as pd
data_dict = {'a': 10, 'b': 20, 'c': 30}
series_from_dict = pd.Series(data_dict)
print("Series from dictionary:")
print(series_from_dict)
data_list = [100, 200, 300, 400]
series_from_list = pd.Series(data_list)
print("\nSeries from list:")
print(series_from_list)
print("\nAccess element with index 'b' in series_from_dict:")
print(series_from_dict['b'])
print("\nAccess element at position 2 in series_from_list:")
print(series_from_list.iloc[2])
print("\nSlice elements from index 'a' to 'c' in series_from_dict:")
print(series_from_dict['a':'c'])
print("\nSlice first two elements by position in series_from_list:")
print(series_from_list.iloc[0:2])
