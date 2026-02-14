import streamlit as st
from data_generator import generate_train_data
from simulator import simulate_section
from ai_model import train_delay_model
from optimizer import optimize_schedule
from metrics import calculate_metrics

st.title("AI-Powered Train Traffic Control System")

num_trains = st.slider("Number of Trains", 10, 100, 50)

if st.button("Run Simulation"):
    df = generate_train_data(num_trains)

    st.subheader("Original Schedule")
    st.write(df)

    simulated_df = simulate_section(df)

    model, error = train_delay_model(simulated_df)

    metrics_before = calculate_metrics(simulated_df)

    optimized_df = optimize_schedule(df)
    optimized_sim = simulate_section(optimized_df)
    metrics_after = calculate_metrics(optimized_sim)

    st.subheader("Performance Before Optimization")
    st.write(metrics_before)

    st.subheader("Performance After Optimization")
    st.write(metrics_after)

    st.subheader("Model MAE Error")
    st.write(error)
