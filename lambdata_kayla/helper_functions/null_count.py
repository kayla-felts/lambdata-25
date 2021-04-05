def null_count(df):
    return df.isnull().sum().sum()