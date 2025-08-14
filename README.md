# Gas Pipeline Anomaly Detection Dashboard

## Project Overview
Gas pipelines are critical infrastructure for energy transport, and their safe, efficient operation is essential for modern society. This project demonstrates the use of artificial intelligence (AI) for real-time anomaly detection in gas pipeline sensor networks, supporting safer and more efficient pipeline operations.

Access App: https://anormality-detection-gas.streamlit.app/ 

## Features
- Live anomaly detection using ensemble AI models
- Interactive dashboard built with Streamlit
- Sensor data visualization and anomaly flag overlays
- Project motivation, data description, and usage guide included in the app

## Data
- `ethylene_CO.csv`: Raw sensor data from 16 gas pipeline sensors
- `fusion_results.csv`: AI-generated ensemble anomaly scores and alert flags

## How to Run the Dashboard
1. Ensure you have Python 3.8+ installed.
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Place `ethylene_CO.csv` and `fusion_results.csv` in the project folder.
4. Run the dashboard:
   ```bash
   streamlit run dashboard.py
   ```
5. Open the provided local URL in your browser to interact with the dashboard.

## Project Motivation
The United States alone has over 2.2 million miles of natural gas pipelines, consisting of both transmission and distribution pipes. Distribution pipes are largely located within cities and towns to serve homes and businesses. Pipeline failures can lead to catastrophic consequences, including explosions, environmental damage, and service disruptions. This project aims to demonstrate how AI can help monitor and protect this vital infrastructure.

## Contact
For questions or collaboration, please contact the project team.
@stellamarisus16@gmail.com 
---
*This project is for demonstration and research purposes only.*
