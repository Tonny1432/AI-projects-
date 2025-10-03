## 🌿 Terra Mind: Smart Soil Sensing Platform

An AI-powered system for **real-time soil health monitoring and prediction**, designed to promote sustainable and precision farming.

-----

### 🌟 Overview

Modern agriculture often suffers from the indiscriminate use of fertilizers and pesticides, compounded by a lack of real-time soil data. This leads to reduced productivity and land degradation. **Terra Mind** addresses this by providing farmers with a clear, instant assessment of their soil health, classified into actionable states, along with personalized remedies.

This project was developed as a college demonstration of the role of **Artificial Intelligence (AI)** and **data-driven decision-making** in precision agriculture.

-----

### 🎯 Features

  * **Comprehensive Soil Parameter Monitoring:** Collects and analyzes key soil health indicators: **pH, Moisture, Temperature, Electrical Conductivity (EC), Nitrogen (N), Phosphorus (P), and Potassium (K)**.
  * **5-State Soil Health Classification:** Classifies the soil's condition into one of five easy-to-understand states using a threshold-based rule engine:
      * 🟢 **Optimal**
      * 🔵 **Stable**
      * 🟡 **Alert**
      * 🟠 **Warning**
      * 🔴 **Critical**
  * **Actionable Remedies:** Provides specific, tailored recommendations to correct imbalances and improve soil health.
  * **User-Friendly Dashboard:** Displays current soil status, history, and remedies via an intuitive web interface.
  * **Flexible Data Input:** Supports both **manual data entry** and **file upload** for soil parameter values.

-----

### ⚙️ How It Works

The system operates on a simple, efficient logic flow:

1.  **Data Collection (Step 1):** The user inputs the soil parameter values (pH, N, P, K, EC, Moisture, Temperature) via the frontend.
2.  **Data Transmission:** The frontend sends the data to the **Python Flask backend**.
3.  **Threshold Classification (Step 2 & 3):** The backend employs a **threshold classifier (a Scikit-learn based or custom rule-based system)** to evaluate each parameter against predefined optimal ranges. The combined results determine the overall soil state (Optimal $\rightarrow$ Critical).
4.  **Remedy Generation (Step 4):** Based on the identified state and specific parameter deviations, the system generates relevant remedies.
5.  **Result Display:** The classified state, specific parameter issues, and personalized remedies are returned to the frontend and displayed on the user dashboard.

#### 📝 Classification Logic Examples

| Soil State | Classification Criteria (Example) |
| :--- | :--- |
| **Optimal** | All parameters within ideal ranges. |
| **Alert** | One or two parameters slightly outside the ideal range. |
| **Critical** | Multiple critical parameter deviations (e.g., pH too low and high salinity). |

-----

### 🛠️ Technology Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend** | HTML, CSS, JavaScript | Building the interactive and responsive user dashboard. |
| **Backend** | Python Flask | Lightweight web framework for handling data processing and logic. |
| **Machine Learning / Logic** | Scikit-learn / Custom Threshold Classifier | Core engine for classifying soil state based on predefined rules. |
| **Data Storage** | LocalStorage | Used in the browser to maintain a history of past soil health assessments. |

-----

### 💊 Remedy Logic Examples

The system provides targeted solutions for identified problems:

| Problem Identified | Suggested Remedy |
| :--- | :--- |
| **pH Too Low (Acidic)** | Add lime, dolomite, or organic compost. |
| **pH Too High (Alkaline)** | Add sulfur or incorporate acidic organic matter (e.g., peat moss). |
| **Moisture Imbalance** | Implement controlled irrigation or improve drainage/aeration of the soil. |
| **N/P/K Deficiency** | Apply targeted synthetic fertilizers or organic manure sources. |
| **High Salinity (EC)** | Leach the soil with good quality water or consider planting salt-tolerant crops. |

-----

