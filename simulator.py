SECTION_CAPACITY = 5  # Max trains allowed at once

def simulate_section(df):
    df = df.sort_values(by="arrival_time").copy()
    active_trains = []
    delays = []

    for _, row in df.iterrows():
        current_time = row["arrival_time"]

        # Remove trains that already left
        active_trains = [t for t in active_trains if t > current_time]

        if len(active_trains) >= SECTION_CAPACITY:
            delay = 10
        else:
            delay = 0

        delays.append(delay)
        active_trains.append(row["departure_time"] + delay)

    df["delay"] = delays
    return df
