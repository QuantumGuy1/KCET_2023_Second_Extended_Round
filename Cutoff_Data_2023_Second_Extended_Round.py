import streamlit as st
import pandas as pd
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('engineering_cutoff.db')
cursor = conn.cursor()

# Query the data
query = "SELECT * FROM engineering_cutoff"
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Streamlit app
st.set_page_config(page_title='Engineering Cutoff Ranks 2023-KCET-Second Extended Round', layout='wide')

st.title('Engineering Cutoff Ranks 2023-KCET-Second Extended Round')
st.write("This Information is up-to-date as per KEA's official Website's PDF")
st.write('This app displays the cutoff ranks for various branches in different colleges.')

# Add a side note
st.sidebar.title("Note")
st.sidebar.write("Rank -> 0 indicates that there was no seat allocated to that branch for GM category in the second extended round.")

# Add the PDF link to the sidebar
st.sidebar.write("### Official PDF Document")
st.sidebar.write("Click on the link below to download/view the official PDF from the KEA website")
pdf_url = "https://cetonline.karnataka.gov.in/keawebentry456/cet2023/ENR2_CUTGENenglish.pdf"
st.sidebar.markdown(f'View the official PDF document online')

# Set the column width to be wider
st.dataframe(df.style.set_properties(**{'width': '200px'}))

# Filter by college
st.markdown("<h2 style='font-size:28px;'>View your desired college</h2>", unsafe_allow_html=True)
college = st.selectbox('List of Colleges', df['college_name'].unique())

# Filter the dataframe by selected college
college_df = df[df['college_name'] == college]

# Display the filtered data for the selected college
st.write(f'Cutoff ranks for all branches in {college}')
st.dataframe(college_df.style.set_properties(**{'width': '200px'}))

# Filter by branch within the selected college
st.markdown("<h2 style='font-size:28px;'>View your desired branch</h2>", unsafe_allow_html=True)
branch = st.selectbox('List of Branches', college_df['branch'].unique())

# Display the filtered data for the selected branch within the selected college
filtered_df = college_df[college_df['branch'] == branch]
st.write(f'Cutoff ranks for {branch} in {college}')
st.dataframe(filtered_df.style.set_properties(**{'width': '200px'}))

print("End")
