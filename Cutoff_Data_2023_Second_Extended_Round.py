import streamlit as st
import pandas as pd
import sqlite3
import base64

# Function to display PDF
def display_pdf(file_path, height=600):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="{height}" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# Connect to SQLite database
conn = sqlite3.connect('engineering_cutoff.db')
cursor = conn.cursor()

# Query the data
query = "SELECT * FROM engineering_cutoff"
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Streamlit app
st.title('Engineering Cutoff Ranks 2023-KCET-Second Extended Round')
st.write("This Information is upto-date as per KIA's official Website's PDF")
st.write('This app displays the cutoff ranks for various branches in different colleges.')

# Add a side note
st.sidebar.title("Note")
st.sidebar.write("Rank -> 0 indicates that there was no seat allocated to that branch for GM category in the second extended round.")

# Add the PDF link to the sidebar
st.sidebar.write("### Official PDF Document")
st.sidebar.markdown('View the official PDF document online, attached')

# Set the column width to be wider
st.dataframe(df.style.set_properties(**{'width': '200px'}))

# Filter by college
college = st.selectbox('Select College', df['college_name'].unique())

# Filter the dataframe by selected college
college_df = df[df['college_name'] == college]

# Display the filtered data for the selected college
st.write(f'Cutoff ranks for all branches in {college}')
st.dataframe(college_df.style.set_properties(**{'width': '200px'}))

# Filter by branch within the selected college
branch = st.selectbox('Select Branch', college_df['branch'].unique())

# Display the filtered data for the selected branch within the selected college
filtered_df = college_df[college_df['branch'] == branch]
st.write(f'Cutoff ranks for {branch} in {college}')
st.dataframe(filtered_df.style.set_properties(**{'width': '200px'}))

# Display the PDF with a reduced height
st.write("### Official PDF Document")
display_pdf_from_url("https://raw.githubusercontent.com/QuantumGuy1/Kcet-streamlit-application/main/Second%20Extended%20Round.pdf", height=400)
