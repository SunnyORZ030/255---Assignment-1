def describe_frame(df):
    return {
        'shape': df.shape,
        'dtypes': df.dtypes.astype(str).to_dict(),
        'null_counts': df.isna().sum().to_dict(),
    }
