import pandas as pd

SECTION_CAPACITY = 5  # max trains at a time

def simulate_section(df):
    df = df.sort_values(by="arrival_time").copy()
    active_trains = []
    delays = []

    for index, row in df.iterrows():
        current_time = row["arrival_time"]

        # remove trains that already left
        active_trains = [
            t for t in active_trains if t > current_time
        ]

        if len(active_trains) >= SECTION_CAPACITY:
            delay = 10  # fixed delay
        else:
            delay = 0

        delays.append(delay)

        active_trains.append(row["departure_time"] + delay)

    df["delay"] = delays
    return df
