import streamlit as st
import pandas as pd
import os
import datetime
import csv

MOOD_FILE = "mood_log.csv"

def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date", "Mood"])
    return pd.read_csv(MOOD_FILE)

def save_mode_data(mood,date):
    with open(MOOD_FILE, "a") as file:
        writer = csv.writer(file)
        writer.writerow([date, mood])


st.title("Mood Tracker App")

today = datetime.date.today()

st.subheader("How are you feeling today?")

mood = st.selectbox("Select you mood", ["Happy", "Sad", "Angry", "Excited", "Bored", "Anxious"])

if st.button("Log Mood"):
    save_mode_data(today, mood)
    st.success("mood logged successfully!")
    

data = load_mood_data()


if not data.empty:
    st.subheader("Mood changes over time")

    data["Date"] = pd.to_datetime(data["Date"])

    mood_counts = data.groupby("Mood").count()["Date"]

    st.bar_chart(mood_counts)
