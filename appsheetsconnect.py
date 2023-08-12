import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Authenticate with Google Sheets API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('my-project-rtlsdrdata-a0aa9af92dd7.json', scope)
client = gspread.authorize(credentials)

# Open the Google Sheet by title
sheet = client.open('appsheetsconnect').sheet1

# Streamlit UI
st.title('Google Sheets Streamlit App')
name = st.text_input('Enter your name:')
email = st.text_input('Enter your email:')
submit_button = st.button('Submit')

if submit_button:
    # Write data to Google Sheet
    sheet.insert_row([name, email], index=2)
    st.success('Data submitted!')

# Display data from Google Sheet
st.write('Recent Data:')
data = sheet.get_all_records()
st.table(data)

