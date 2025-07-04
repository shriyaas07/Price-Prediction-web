# ✈️ Flight Price Predictor – Dynamic Pricing Strategy Model

A dynamic web-based application that predicts flight ticket prices using machine learning. It also visualizes pricing trends through live charts, simulates competitor pricing, and assists in pricing decisions with interactive dashboards.

##  Features

-  **Real-time Price Prediction** using trained ML model
- **Live Dashboard Visualizations** (Airline, Duration, Booking Slot)
- **Interactive User Inputs** with smart suggestions
- Airline-themed responsive UI with background image support
- Competitor price simulation and visual price positioning
- Built with Flask, Seaborn, Pandas, Scikit-learn, and Bootstrap



##  User Inputs

- Airline (Dropdown)
- From City (with auto-suggestion)
- To City (with auto-suggestion)
- Number of Stops
- Duration (in minutes)
- Lead Time (days before journey)
- Booking Slot (Dropdown: Morning, Afternoon, Evening, Night)


## Backend Model Features (Handled Automatically)

- `Booking_Hour`: Derived from selected slot
- `Competitor_Price`: Randomized for simulation
- `Price_Diff_vs_Competitor`: Model-internal calculation


## Live Dashboard Visuals

The app includes interactive charts:

- **Airline vs Avg Price** – to compare pricing across airlines
- **Duration vs Price** – shows relation of trip duration and fare
- **Booking Slot vs Price** – shows average fare for different booking times

*Charts update on prediction submission.*



## Machine Learning Model

- Model: Random Forest Regressor
- Pipeline includes OneHotEncoding + Feature Engineering
- Trained with custom dataset using flight pricing factors


## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, Bootstrap
- **ML Libraries**: Pandas, Scikit-learn, Seaborn
- **Visualization**: Matplotlib + Seaborn (Live Updates)

