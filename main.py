import os
from datetime import datetime, date
import streamlit as st
import pandas as pd
import plotly.express as px
import gspread
from google.oauth2.service_account import Credentials

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json",scopes=scopes)
client = gspread.authorize(creds)\

sheet_id = "1Qh7dKXTHheC3J8Q_YUTa8d6GPeh08s482utg8qCNNyo"


@st.cache_resource
def get_sheet():
    creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
    client = gspread.authorize(creds)
    # open by key instead of name
    return client.open_by_key(sheet_id).sheet1

sheet = get_sheet()

st.title("Mood of the Queue")

with st.form("log_mood", clear_on_submit=True):
    Mood = st.selectbox("How’s the vibe?", ["😊", "😠", "😕", "🎉"])
    Note = st.text_input("Optional note")
    if st.form_submit_button("Log it"):
        TimeStamp = datetime.now().isoformat() 
        sheet.append_row([TimeStamp, Mood, Note])
        st.success(f"Logged {Mood} at {TimeStamp}")


rows = sheet.get_all_values()
if len(rows) <= 1:
    st.info("No entries yet.")
    st.stop()

df = pd.DataFrame(rows[1:], columns=rows[0])
df["TimeStamp"] = pd.to_datetime(df["TimeStamp"])


selected_date = st.date_input(
    "Select a day to view moods for",
    value=date.today()
)

day_df = df[df["TimeStamp"].dt.date == selected_date]

st.subheader(f"Mood counts for {selected_date.isoformat()}")

counts = (
    day_df["Mood"]
    .value_counts()
    .reindex(["😊", "😠", "😕", "🎉"], fill_value=0)
)

fig = px.bar(
    x=counts.index,
    y=counts.values,
    labels={"x": "Mood", "y": "Count"},
    title=""  
)

st.plotly_chart(fig, use_container_width=True)