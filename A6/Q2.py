import pandas as pd
df1 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'value_df1': ['A', 'B', 'C', 'D']
})
df2 = pd.DataFrame({
    'id': [3, 4, 5, 6],
    'value_df2': ['W', 'X', 'Y', 'Z']
})
print("df1:")
print(df1)
print("\ndf2:")
print(df2)
inner_merge = pd.merge(df1, df2, on='id', how='inner')
print("\nInner Merge Result:")
print(inner_merge)
left_join = pd.merge(df1, df2, on='id', how='left')
print("\nLeft Join Result:")
print(left_join)
right_join = pd.merge(df1, df2, on='id', how='right')
print("\nRight Join Result:")
print(right_join)
df1_indexed = df1.set_index('id')
df2_indexed = df2.set_index('id')
join_result = df1_indexed.join(df2_indexed, how='inner')
print("\nJoin based on index (inner):")
print(join_result)
df1_multi = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'key': ['A', 'B', 'A', 'B'],
    'value_df1': [10, 20, 30, 40]
})
df2_multi = pd.DataFrame({
    'id': [3, 4, 3, 4],
    'key': ['A', 'B', 'B', 'A'],
    'value_df2': [100, 200, 300, 400]
})
multi_merge = pd.merge(df1_multi, df2_multi, on=['id', 'key'], how='inner')
print("\nMerge on multiple keys:")
print(multi_merge)