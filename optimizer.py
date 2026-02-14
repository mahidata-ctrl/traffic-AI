def optimize_schedule(df):
    # Priority trains first, then by arrival time
    optimized_df = df.sort_values(
        by=["priority", "arrival_time"],
        ascending=[False, True]
    ).copy()

    return optimized_df
