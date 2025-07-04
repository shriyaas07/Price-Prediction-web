from flask import Flask, render_template, request
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

app = Flask(__name__)
model = joblib.load("flight_price_model.pkl")  # Your trained pipeline model
city_list = open("city_list.txt", encoding='utf-8').read().splitlines()

# Default data for chart initialization
df_dash = pd.DataFrame([
    {"Airline": "IndiGo", "From": "Delhi", "To": "Mumbai", "Stops_num": 0, "Duration_mins": 120, "Lead_Time_Days": 15, "Booking_Slot": "Morning", "Price": 5000},
    {"Airline": "Air India", "From": "Delhi", "To": "Chennai", "Stops_num": 1, "Duration_mins": 180, "Lead_Time_Days": 10, "Booking_Slot": "Evening", "Price": 6200},
    {"Airline": "SpiceJet", "From": "Mumbai", "To": "Kolkata", "Stops_num": 0, "Duration_mins": 150, "Lead_Time_Days": 20, "Booking_Slot": "Afternoon", "Price": 5800}
])

def update_charts(df):
    # Chart 1: Booking Slot vs Price
    plt.figure(figsize=(7, 3))
    sns.barplot(data=df, x="Booking_Slot", y="Price", palette="coolwarm")
    plt.title("Booking Slot vs Price")
    plt.tight_layout()
    plt.savefig("static/chart1.png")
    plt.close()

    # Chart 2: Airline vs Avg Price
    plt.figure(figsize=(7, 3))
    sns.barplot(data=df, x="Airline", y="Price", estimator=np.mean, palette="pastel")
    plt.title("Airline vs Avg Price")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig("static/chart2.png")
    plt.close()

    # Chart 3: Duration vs Price (Scatter)
    plt.figure(figsize=(7, 3))
    sns.scatterplot(data=df, x="Duration_mins", y="Price", hue="Booking_Slot", palette="Set2")
    plt.title("Duration vs Price")
    plt.tight_layout()
    plt.savefig("static/chart3.png")
    plt.close()

# Update initial charts
update_charts(df_dash)

@app.route("/", methods=["GET", "POST"])
def home():
    global df_dash
    prediction = None

    if request.method == "POST":
        airline = request.form["airline"]
        source = request.form["source"]
        destination = request.form["destination"]
        stops = int(request.form["stops"])
        duration = int(request.form["duration"])
        lead_time = int(request.form["lead_time"])
        booking_slot = request.form["booking_slot"]

        booking_hour_map = {"Morning": 9, "Afternoon": 15, "Evening": 18, "Night": 22}
        booking_hour = booking_hour_map.get(booking_slot, 12)
        competitor_price = np.random.randint(2000, 11000)
        price_diff = np.random.randint(-700, 700)

        input_data = pd.DataFrame([{
            "Airline": airline,
            "From": source,
            "To": destination,
            "Stops_num": stops,
            "Duration_mins": duration,
            "Lead_Time_Days": lead_time,
            "Booking_Slot": booking_slot,
            "Booking_Hour": booking_hour,
            "Competitor_Price": competitor_price,
            "Price_Diff_vs_Competitor": price_diff
        }])

        prediction = model.predict(input_data)[0]

        # Append new data
        df_dash = pd.concat([df_dash, pd.DataFrame([{
            'Airline': airline,
            'From': source,
            'To': destination,
            'Stops_num': stops,
            'Duration_mins': duration,
            'Lead_Time_Days': lead_time,
            'Booking_Slot': booking_slot,
            'Price': prediction
        }])], ignore_index=True)

        # Update charts
        update_charts(df_dash)

    return render_template("index.html",
                           city_list=city_list,
                           prediction=prediction)
if __name__ == "__main__":
    app.run(debug=True)