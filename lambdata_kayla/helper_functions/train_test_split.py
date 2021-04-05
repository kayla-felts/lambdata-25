def train_test_split(df, frac):
    import sklearn.model_selection.train_test_split
    split_data = train_test_split(df=df, test_size=frac)
    return split_data