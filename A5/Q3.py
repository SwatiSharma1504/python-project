import pandas as pd
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'City': ['NY', 'LA', 'Chicago']
})
print("Using iterrows():")
for index, row in df.iterrows():
    print(index, row['Name'], row['Age'])
print("\nUsing itertuples():")
for row in df.itertuples():
    print(row.Index, row.Name, row.Age)
print("\nUsing apply():")
def print_name_age(row):
    print(row['Name'], row['Age'])
df.apply(print_name_age, axis=1)
selected_rows = df[df['Age'] > 23]
print("\nRows with Age > 23:")
print(selected_rows)
row = df[df['Age'] > 23].iloc[0]
print("\nFirst row where Age > 23:")
print(row)
print("\nFirst two rows using iloc:")
print(df.iloc[0:2])
print("\nFirst two rows, limited columns using iloc:")
print(df.iloc[0:2][['Name', 'City']])
df_dropped = df.drop(df[df['Age'] < 25].index)
print("\nDataFrame after dropping rows with Age < 25:")
print(df_dropped)
new_row = {'Name': 'David', 'Age': 28, 'City': 'Boston'}
pos = 1
df_upper = df.iloc[:pos]
df_lower = df.iloc[pos:]
df_new = pd.concat([df_upper, pd.DataFrame([new_row]), df_lower]).reset_index(drop=True)
print("\nDataFrame after inserting a row at position 1:")
print(df_new)
list_of_dicts = df.to_dict('records')
print("\nList of dictionaries (rows):")
print(list_of_dicts)
list_of_lists = df.values.tolist()
print("\nList of lists (rows):")
print(list_of_lists)