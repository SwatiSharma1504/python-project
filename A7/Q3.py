import pandas as pd
file_path = 'your_file.csv'
df = pd.read_csv(file_path)
print("First 5 rows:")
print(df.head())
print("\nData summary:")
print(df.info())
print("\nBasic statistics:")
print(df.describe())
print("\nMissing values per column:")
print(df.isnull().sum())
for col in df.select_dtypes(include=['float64', 'int64']).columns:
    df[col].fillna(df[col].mean(), inplace=True)
for col in df.select_dtypes(include=['object']).columns:
    df[col].fillna(df[col].mode()[0], inplace=True)
df_cleaned = df.drop_duplicates()
print("\nAfter cleaning:")
print(df_cleaned.info())
print("\nSummary statistics after cleaning:")
print(df_cleaned.describe())
print("\nCorrelation matrix:")
print(df_cleaned.corr())
if 'Category' in df_cleaned.columns:
    print("\nGroup by 'Category':")
    print(df_cleaned.groupby('Category').mean())
df_cleaned.to_csv('cleaned_data.csv', index=False)
print("\nCleaned data saved to 'cleaned_data.csv'")