def optimize_schedule(df):
    # Priority trains first
    df = df.sort_values(
        by=["priority", "arrival_time"],
        ascending=[False, True]
    ).copy()

    return df
