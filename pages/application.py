import streamlit as st
import pandas as pd
import plotly.express as px

# Set page width
st.set_page_config(layout="wide")

# Load data
@st.cache
def load_bowling_data():
    df = pd.read_csv('2023_bowling.csv')
    df.index += 1  # Adjust index to start from 1
    return df

@st.cache
def load_batting_data():
    df = pd.read_csv('2023_batting.csv')
    df.index += 1  # Adjust index to start from 1
    return df

bowling_df = load_bowling_data()
batting_df = load_batting_data()

# Sidebar filters
st.sidebar.header('Filters')
analysis_option = st.sidebar.selectbox('Analysis Option', ['Bowling Stats', 'Batting Stats'])
country_list = list(bowling_df['Country'].unique())
country = st.sidebar.selectbox("Select Country", country_list)

# Function to filter data based on country and case sensitivity
def filter_data(df, country):
    return df[df['Country'].str.contains(country, case=False)] if country else df

# Submit button action
if st.sidebar.button('Submit'):
    if analysis_option == 'Bowling Stats':
        filtered_bowling_df = filter_data(bowling_df, country)
        st.write(filtered_bowling_df)

        # Visualizations for Bowling Stats
        st.markdown('### Bowling Statistics Visualizations')

        # Pie chart of Wickets distribution by Country
        wickets_by_country = filtered_bowling_df.groupby("Country")["Wickets"].sum().reset_index()
        fig = px.pie(wickets_by_country, values='Wickets', names='Country', title='Wickets Distribution by Country')
        st.plotly_chart(fig, use_container_width=True)

        # Bar plot showing Wickets taken by players
        fig_bar = px.bar(filtered_bowling_df, x='Name', y='Wickets', title='Wickets Taken by Players')
        st.plotly_chart(fig_bar, use_container_width=True)

        # Best Bowling Average bar plot
        best_bowling_average = filtered_bowling_df[filtered_bowling_df['Average'] != 0].sort_values(by='Average')
        fig_best_avg = px.bar(best_bowling_average, x='Name', y='Average', title='Bowling Averages')
        st.plotly_chart(fig_best_avg, use_container_width=True)

    elif analysis_option == 'Batting Stats':
        filtered_batting_df = filter_data(batting_df, country)
        st.write(filtered_batting_df)

        # Orange Cap Pie Chart
        st.markdown('### Orange Cap Pie Chart')
        runs_by_player = filtered_batting_df.groupby("Name")["Runs"].sum().reset_index()
        fig = px.pie(runs_by_player, values='Runs', names='Name', title='Runs Distribution by Player')
        st.plotly_chart(fig, use_container_width=True)

        # Bar plot showing Runs scored by players
        st.markdown('### Runs Scored by Players')
        fig = px.bar(filtered_batting_df, x='Name', y='Runs', title='Runs Scored')
        st.plotly_chart(fig, use_container_width=True)

# Compare Players functionality
if analysis_option == 'Batting Stats':
    st.sidebar.header('Compare Batsmen')
    players_to_compare = st.sidebar.multiselect('Select Batsmen', batting_df['Name'].unique())

    if st.sidebar.button('Compare Batsmen'):
        comparison_df = batting_df[batting_df['Name'].isin(players_to_compare)].reset_index(drop=True)
        comparison_df.index += 1  # Start numbering from 1
        st.markdown('### Comparison of Batting Statistics')
        st.write(comparison_df)

if analysis_option == 'Bowling Stats':
    st.sidebar.header('Compare Bowlers')
    bowlers_to_compare = st.sidebar.multiselect('Select Bowlers', bowling_df['Name'].unique())

    if st.sidebar.button('Compare Bowlers'):
        comparison_bowlers_df = bowling_df[bowling_df['Name'].isin(bowlers_to_compare)].reset_index(drop=True)
        comparison_bowlers_df.index += 1  # Start numbering from 1
        st.markdown('### Comparison of Bowling Statistics')
        st.write(comparison_bowlers_df)

# Set consistent title size for all graphs and markdown headers
def set_styles():
    st.markdown("""
        <style>
        .reportview-container .markdown-text-container h1, h2, h3, h4, h5, h6 {font-size:24px;}
        .dashboard-root .block-container .element-container .stMarkdown {font-size: 24px;}
        .css-10trblm {font-size:24px;}
        .css-1d391kg {font-size:24px;}
        </style>
        """, unsafe_allow_html=True)

set_styles()
