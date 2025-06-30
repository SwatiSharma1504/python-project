import pandas as pd
data_2d_list = [
    [1, 'Alice', 25],
    [2, 'Bob', 30],
    [3, 'Charlie', 22]
]
df_2d_list = pd.DataFrame(data_2d_list, columns=['ID', 'Name', 'Age'])
print("DataFrame from 2D list:")
print(df_2d_list)
data_dict = {
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22]
}
df_dict = pd.DataFrame(data_dict)
print("\nDataFrame from dictionary:")
print(df_dict)
list_of_lists = [
    [1, 'Alice', 25],
    [2, 'Bob', 30],
    [3, 'Charlie', 22]
]
df_list_of_lists = pd.DataFrame(list_of_lists, columns=['ID', 'Name', 'Age'])
print("\nDataFrame from list of lists:")
print(df_list_of_lists)
list_of_tuples = [
    (1, 'Alice', 25),
    (2, 'Bob', 30),
    (3, 'Charlie', 22)
]
df_list_of_tuples = pd.DataFrame(list_of_tuples, columns=['ID', 'Name', 'Age'])
print("\nDataFrame from list of tuples:")
print(df_list_of_tuples)
list_of_dicts = [
    {'ID': 1, 'Name': 'Alice', 'Age': 25},
    {'ID': 2, 'Name': 'Bob', 'Age': 30},
    {'ID': 3, 'Name': 'Charlie', 'Age': 22}
]
df_list_of_dicts = pd.DataFrame(list_of_dicts)
print("\nDataFrame from list of dictionaries:")
print(df_list_of_dicts)