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
    with open(MOOD_FILE, "a") as file

    writer = csv.writer(file)

    writer.writerow([date, mood])