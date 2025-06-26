import pandas as pd
df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'value1': ['A', 'B', 'C']
})
df2 = pd.DataFrame({
    'id': [4, 5, 6],
    'value1': ['D', 'E', 'F']
})
df3 = pd.DataFrame({
    'id': [2, 3, 5, 6],
    'value2': ['W', 'X', 'Y', 'Z']
})
print("df1:")
print(df1)
print("\ndf2:")
print(df2)
print("\ndf3:")
print(df3)
concat_df = pd.concat([df1, df2], ignore_index=True)
print("\nConcatenated DataFrame (df1 + df2):")
print(concat_df)
merged_df = pd.merge(concat_df, df3, on='id', how='inner')
print("\nMerged DataFrame (concat_df merged with df3 on 'id'):")
print(merged_df)