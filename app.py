import streamlit as st
import matplotlib.pyplot as plt

from data_generator import generate_train_data
from simulator import simulate_section
from ai_model import train_delay_model
from optimizer import optimize_schedule
from metrics import calculate_metrics

st.set_page_config(page_title="AI Train Traffic Control", layout="wide")

st.title("🚆 AI-Powered Train Traffic Control System")
st.markdown("Maximizing Section Throughput using Intelligent Scheduling")

num_trains = st.slider("Select Number of Trains", 10, 100, 50)

if st.button("Run Simulation"):

    # Generate Data
    df = generate_train_data(num_trains)

    # Simulate before optimization
    simulated_df = simulate_section(df)
    metrics_before = calculate_metrics(simulated_df)

    # Train AI model
    model, error = train_delay_model(simulated_df)

    # Optimize schedule
    optimized_df = optimize_schedule(df)
    optimized_sim = simulate_section(optimized_df)
    metrics_after = calculate_metrics(optimized_sim)

    # Calculate improvement
    improvement = (
        (metrics_after["Section Throughput"] - metrics_before["Section Throughput"])
        / metrics_before["Section Throughput"]
    ) * 100

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Before Optimization")
        st.write(metrics_before)

    with col2:
        st.subheader("🚀 After Optimization")
        st.write(metrics_after)

    st.subheader("📈 Throughput Improvement")
    st.success(f"{improvement:.2f}% improvement")

    st.subheader("🧠 AI Model Error (MAE)")
    st.write(f"{error:.2f}")

    # Plot comparison
    labels = ["Average Delay Before", "Average Delay After"]
    values = [
        metrics_before["Average Delay"],
        metrics_after["Average Delay"]
    ]

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_ylabel("Delay")
    st.pyplot(fig)
