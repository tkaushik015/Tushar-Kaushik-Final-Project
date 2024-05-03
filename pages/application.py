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

# Visualization and analysis upon button press
if st.sidebar.button('Submit'):
    if analysis_option == 'Bowling Stats':
        filtered_bowling_df = filter_data(bowling_df, country)
        filtered_bowling_df.index.name = 'Position in Purple Cap List'
        st.write(filtered_bowling_df)

        # Visualizations for Bowling Stats
        st.markdown('### Bowling Statistics Visualizations')

        # Pie chart of Wickets distribution by Country
        wickets_by_country = filtered_bowling_df.groupby("Country")["Wickets"].sum().reset_index()
        fig = px.pie(wickets_by_country, values='Wickets', names='Country', title='Wickets Distribution by Country')
        st.plotly_chart(fig, use_container_width=True)

        # Pie chart of Wickets distribution by Bowler
        wickets_by_bowler = filtered_bowling_df.groupby("Name")["Wickets"].sum().reset_index()
        fig = px.pie(wickets_by_bowler, values='Wickets', names='Name', title='Wickets Distribution by Bowler')
        st.plotly_chart(fig, use_container_width=True)

        # Bar plot Showing Wickets Taken by Players
        fig_bar = px.bar(filtered_bowling_df, x='Name', y='Wickets', title='Wickets Taken by Players')
        st.plotly_chart(fig_bar, use_container_width=True)

        # Best Bowling Average bar plot
        best_bowling_average = filtered_bowling_df[['Name', 'Average']].copy()
        best_bowling_average = best_bowling_average[best_bowling_average['Average'] != 0]  # Filter non-zero averages
        best_bowling_average = best_bowling_average.sort_values(by='Average').reset_index(drop=True)
        best_bowling_average.index += 1  # Start numbering from 1
        fig_best_avg = px.bar(best_bowling_average, x='Name', y='Average', title='Bowling Averages')
        st.plotly_chart(fig_best_avg, use_container_width=True)

    elif analysis_option == 'Batting Stats':
        filtered_batting_df = filter_data(batting_df, country)
        filtered_batting_df.index.name = 'Position in Orange Cap List'
        st.write(filtered_batting_df)

        # Visualizations for Batting Stats
        st.markdown('### Batting Statistics Visualizations')

        # Pie chart of Runs distribution by Player
        runs_by_player = filtered_batting_df.groupby("Name")["Runs"].sum().reset_index()
        fig = px.pie(runs_by_player, values='Runs', names='Name', title='Runs Distribution by Player')
        st.plotly_chart(fig, use_container_width=True)


        # Bar plot of Bar Plot Showing Runs Scored by Players
        st.subheader('**Bar Plot Showing Runs Scored by Players**')
        runs_by_player = filtered_batting_df.groupby("Name")["Runs"].sum().reset_index()
        fig = px.bar(runs_by_player, x='Name', y='Runs', title='Runs Scored')
        st.plotly_chart(fig, use_container_width=True)

        # Pie chart of Hundred's distribution by Country
        st.subheader('**Hundred\'s distribution by Country**')
        hundreds_by_country = batting_df.groupby("Country")["Hundreds"].sum().reset_index()
        fig = px.pie(hundreds_by_country, values='Hundreds', names='Country', title='Hundred\'s distribution')
        st.plotly_chart(fig, use_container_width=True)

        # Pie chart of Fifties distribution by Country for all countries
        st.subheader('**Fifties distribution by Country**')
        fifties_by_country_all = batting_df.groupby("Country")["Fifties"].sum().reset_index()
        fig = px.pie(fifties_by_country_all, values='Fifties', names='Country', title='Fifties distribution')
        st.plotly_chart(fig, use_container_width=True)

        # Bar plot of Batting Averages by Player
        st.subheader('**Batting Averages of Players**')
        fig_avg = px.bar(filtered_batting_df, x='Name', y='Average', title='Batting Averages')
        st.plotly_chart(fig_avg, use_container_width=True)

        # Best Batting Average table
        st.subheader('**Best Batting Average**')
        best_batting_average = filtered_batting_df[['Name', 'Average']].copy()
        best_batting_average = best_batting_average[best_batting_average['Average'] != 0]  # Filter non-zero averages
        best_batting_average = best_batting_average.sort_values(by='Average', ascending=False).reset_index(drop=True)
        best_batting_average.index += 1  # Start numbering from 1
        st.write(best_batting_average)

        # Table of Top Power hitters
        st.subheader('**Top Power hitters**')
        top_power_hitters = filtered_batting_df[filtered_batting_df['Strike_rate'] >= 150].reset_index(drop=True)
        top_power_hitters.index += 1  # Start numbering from 1
        st.write(top_power_hitters)

        # Table of Number Of Fifties By Each Player
        st.subheader('**Number Of Fifties By Each Player**')
        fifties_by_player = filtered_batting_df[['Name', 'Fifties']].copy()
        fifties_by_player = fifties_by_player[fifties_by_player['Fifties'] != 0]  # Filter non-zero fifties
        fifties_by_player.index += 1  # Start numbering from 1
        st.write(fifties_by_player)

        # Table of Number Of Hundreds By Each Player
        st.subheader('**Number Of Hundreds By Each Player**')
        hundreds_by_player = filtered_batting_df[['Name', 'Hundreds']].copy()
        hundreds_by_player = hundreds_by_player[hundreds_by_player['Hundreds'] != 0]  # Filter non-zero hundreds
        hundreds_by_player.index += 1  # Start numbering from 1
        st.write(hundreds_by_player)

        # Table of Most Boundaries
        st.subheader('**Most Boundaries**')
        most_boundaries = filtered_batting_df[['Name', 'Fours']].copy()
        most_boundaries = most_boundaries[most_boundaries['Fours'] != 0]  # Filter non-zero boundaries
        most_boundaries.index += 1  # Start numbering from 1
        st.write(most_boundaries)

        # Table of Most Sixes
        st.subheader('**Most Sixes**')
        most_sixes = filtered_batting_df[['Name', 'Sixes']].copy()
        most_sixes = most_sixes[most_sixes['Sixes'] != 0]  # Filter non-zero sixes
        most_sixes.index += 1  # Start numbering from 1
        st.write(most_sixes)

        # Correlation Matrix for Batting Stats
        st.subheader('**Correlation Matrix for Batting Stats:**')
        batting_heatmap = filtered_batting_df.select_dtypes(include=['float64', 'int64']).corr()
        st.write(batting_heatmap)

# Add a section to compare batting statistics of selected players
if analysis_option == 'Batting Stats':
    st.sidebar.header('Compare Batsmen')
    players_to_compare = st.sidebar.multiselect('Select Batsmen', batting_df['Name'].unique())

    if st.sidebar.button('Compare'):
        comparison_df = batting_df[batting_df['Name'].isin(players_to_compare)].reset_index(drop=True)
        comparison_df.index += 1  # Start numbering from 1
        comparison_df.rename(columns={'Unnamed: 0': 'Index no.'}, inplace=True)  # Rename index column
        st.subheader('**Comparison of Batting Statistics**')
        st.write(comparison_df)

# Add a section to compare bowling statistics of selected players
if analysis_option == 'Bowling Stats':
    st.sidebar.header('Compare Bowlers')
    bowlers_to_compare = st.sidebar.multiselect('Select Bowlers', bowling_df['Name'].unique())

    if st.sidebar.button('Compare'):
        comparison_bowlers_df = bowling_df[bowling_df['Name'].isin(bowlers_to_compare)].reset_index(drop=True)
        comparison_bowlers_df.index += 1  # Start numbering from 1
        st.subheader('**Comparison of Bowling Statistics**')
        st.write(comparison_bowlers_df)

# Set background color
def set_background_color(color):
    st.markdown(f"""
        <style>
            .reportview-container {{
                background-color: {color};
            }}
            h1, h2, h3, h4, h5, h6 {{
                font-size: 18px;
            }}
        </style>
    """, unsafe_allow_html=True)

set_background_color("#000000")
