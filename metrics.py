def calculate_metrics(df):
    total_trains = len(df)
    total_delay = df["delay"].sum()
    avg_delay = df["delay"].mean()

    throughput = total_trains / 300

    return {
        "Total Trains": total_trains,
        "Total Delay": float(total_delay),
        "Average Delay": float(avg_delay),
        "Section Throughput": float(throughput)
    }
