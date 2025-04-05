import streamlit as st
import pandas as pd
import os
import datetime
import csv

# File path
MOOD_FILE = "mood_log.csv"

# Initialize file with headers if it's missing or empty
if not os.path.exists(MOOD_FILE) or os.path.getsize(MOOD_FILE) == 0:
    with open(MOOD_FILE, "w") as f:
        f.write("Date,Mood\n")

# Load data from CSV
def load_mood_data():
    if not os.path.exists(MOOD_FILE) or os.path.getsize(MOOD_FILE) == 0:
        return pd.DataFrame(columns=["Date", "Mood"])
    return pd.read_csv(MOOD_FILE)

# Save mood entry
def save_mood_data(date, mood):
    with open(MOOD_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, mood])

# Streamlit UI
st.title("Mood Tracker App")

today = datetime.date.today()

st.subheader("How are you feeling today?")

mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Excited", "Bored", "Anxious"])

if st.button("Log Mood"):
    save_mood_data(today, mood)
    st.success("Mood logged successfully!")

# Load and display mood data
data = load_mood_data()

if not data.empty:
    st.subheader("Mood changes over time")

    data["Date"] = pd.to_datetime(data["Date"])

    mood_counts = data.groupby("Mood").count()["Date"]

    st.bar_chart(mood_counts)
else:
    st.info("No mood data available yet. Log your mood to see progress!")
