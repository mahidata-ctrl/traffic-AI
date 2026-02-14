import pandas as pd
import numpy as np

def generate_train_data(num_trains=50):
    np.random.seed(42)

    data = []
    for i in range(num_trains):
        arrival = np.random.randint(0, 300)
        departure = arrival + np.random.randint(5, 20)
        speed = np.random.randint(40, 120)
        priority = np.random.choice([0, 1])  # 1 = Express

        data.append([
            i,
            arrival,
            departure,
            speed,
            priority
        ])

    df = pd.DataFrame(data, columns=[
        "train_id",
        "arrival_time",
        "departure_time",
        "speed",
        "priority"
    ])

    return df
