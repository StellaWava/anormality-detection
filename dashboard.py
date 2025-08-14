import warnings
import pandas as pd
import streamlit as st
from pandas.errors import DtypeWarning
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore", category=DtypeWarning)

# --- App Title and Project Goal ---
st.set_page_config(page_title="Gas Pipeline Anomaly Detection Dashboard", layout="wide")
st.title("Gas Pipeline Anomaly Detection Dashboard")

with st.expander("ℹ️ Project Goal and Motivation", expanded=True):
    st.markdown("""
    **Gas pipelines are critical infrastructure for energy transport, and their safe, efficient operation is essential for modern society.**
    
    The United States alone has over 2.2 million miles of natural gas pipelines, consisting of both transmission and distribution pipes. Distribution pipes are largely located within cities and towns to serve homes and businesses. Pipeline failures can lead to catastrophic consequences, including explosions, environmental damage, and service disruptions.
    
    This dashboard demonstrates the use of artificial intelligence (AI) for real-time anomaly detection in gas pipeline sensor networks, supporting safer and more efficient pipeline operations.
    """)

# --- About the Data Block ---
with st.expander("📊 About the Data", expanded=False):
    st.markdown("""
    - **Sensor Data:** 16 sensors monitoring various physical parameters along a gas pipeline.
    - **Fusion Results:** AI-generated ensemble anomaly scores and alert flags.
    - **Time Alignment:** All plots are aligned to the pipeline's operational timeline for live monitoring.
    """)

# --- How to Use the Dashboard Block ---
with st.expander("🛠️ How to Use This Dashboard", expanded=False):
    st.markdown("""
    1. **Live Anomaly Detection Overview:**
        - View the ensemble anomaly score and detected anomaly flags over time.
    2. **Sensor Explorer:**
        - Select any sensor to visualize its readings alongside detected anomalies.
    3. **Data Table:**
        - Preview the merged sensor and anomaly data.
    """)

# --- Load and Merge Data ---
def load_data():
    try:
        fusion = pd.read_csv('fusion_results.csv', low_memory=False)
        sensors = pd.read_csv('ethylene_CO.csv', low_memory=False)
        fusion = fusion.reset_index(drop=True)
        sensors = sensors.reset_index(drop=True)
        merged = pd.concat([sensors, fusion], axis=1)
        return merged
    except Exception as e:
        st.error(f"Error loading or merging CSVs: {e}")
        return pd.DataFrame()

data = load_data()

if not data.empty:
    st.header("Live Anomaly Detection Overview")
    time_col = None
    for col in data.columns:
        if 'time' in col.lower():
            time_col = col
            break
    if 'ensemble_score' in data.columns:
        fig, ax = plt.subplots(figsize=(12, 5))
        x = data[time_col] if time_col else data.index
        ax.plot(x, data['ensemble_score'], label='Ensemble Score', color='blue')
        if 'alerts' in data.columns:
            alert_mask = data['alerts'].notna() & (data['alerts'] != 0)
            ax.scatter(x[alert_mask], data['ensemble_score'][alert_mask], color='red', label='Anomaly Flags', zorder=5)
        ax.set_xlabel(time_col if time_col else 'Index')
        ax.set_ylabel('Ensemble Score')
        ax.set_title('Ensemble Score and Detected Anomalies Over Time')
        ax.legend()
        st.pyplot(fig)
    sensor_cols = [col for col in data.columns if 'Sensor' in col]
    if sensor_cols:
        sensor = st.selectbox('Select a sensor to plot:', sensor_cols)
        fig2, ax2 = plt.subplots(figsize=(12, 4))
        ax2.plot(x, data[sensor], label=sensor, color='gray', alpha=0.7)
        if 'alerts' in data.columns:
            alert_mask = data['alerts'].notna() & (data['alerts'] != 0)
            ax2.scatter(x[alert_mask], data[sensor][alert_mask], color='red', label='Anomaly Flags', zorder=5)
        ax2.set_xlabel(time_col if time_col else 'Index')
        ax2.set_ylabel('Sensor Value')
        ax2.set_title(f'{sensor} with Anomaly Flags')
        ax2.legend()
        st.pyplot(fig2)
    st.dataframe(data.head())
else:
    st.warning("No merged data available for plotting.")

# --- Footer ---
st.markdown("""
---
*This dashboard is for demonstration and research purposes. For more information, contact the project team. @ stellamarisus16@gmail.com*
""")