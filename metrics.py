def calculate_metrics(df):
    total_trains = len(df)
    total_delay = df["delay"].sum()
    avg_delay = df["delay"].mean()

    throughput = total_trains / 300  # trains per time unit

    return {
        "Total Trains": total_trains,
        "Total Delay": total_delay,
        "Average Delay": avg_delay,
        "Section Throughput": throughput
    }
