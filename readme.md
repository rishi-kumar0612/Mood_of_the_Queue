# Mood of the Queue

A simple Streamlit app for logging and visualizing the mood of a support ticket queue using Google Sheets as storage.

## Features

- Log a mood (😊 😠 😕 🎉) with an optional note
- Store entries in a Google Sheet
- Select a date to view mood counts for that day
- Interactive bar chart powered by Plotly

## Requirements

- Python 3.8+
- Streamlit
- pandas
- gspread
- google-auth
- plotly

## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/rishi-kumar0612/Mood_of_the_Queue.git
   cd Mood_of_the_Queue

2. Install dependencies:

    ```bash
    pip install -r requirements.txt

3. Add your Google service account JSON and sheet ID to Streamlit secrets:
    ```bash
    [google]
    Cred_JSON = """
    { ... your service account JSON ... }
    """
    sheet_id = "YOUR_SHEET_ID"

# Run
    streamlit run main.py

Open the URL shown in your browser to use the app.
