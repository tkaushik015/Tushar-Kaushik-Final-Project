import streamlit as st





st.markdown("**1. Name: Tushar Kaushik**")




st.markdown("**2. An explanation of how to use your webapp: what interactivity there is, what the plots/charts mean, what your conclusions were, etc:**")
st.write("Ans: The web app focuses on IPL, a T20 cricket league in India, specifically analyzing data for the 2023 season. It provides insights into player performance, including the Orange Cap for most runs and the Purple Cap for most wickets. Users can select between Batting Stats and Bowling Stats, filter data by country, and visualize statistics through pie charts, box plots, tables, and correlation matrices. After selecting options and submitting, users can explore player statistics and compare multiple players using a dropdown menu. To access the webapp, select Batting Stats/ Bowling Stats and then click Submit button. To compare players, select player names in the dropdown and then click on Compare button.")



st.markdown("**3. Any major 'gotchas' (i.e. things that don’t work, go slowly, could be improved, etc.):**")
st.write("Ans: One potential issue is that when changing filter options after selecting players for comparison, the selected players are not automatically cleared. This functionality could be improved in future iterations. When we get the tables after clicking 'Submit', we can get the first column in coronological order, we can also add the name for the first column. When we click on the column name of the table, it is arranged in ascending or descending order. However if the column i highest score, it does not happen as highest score is a numeric value but it ends with '*' if the player is not out, so it is not stored as an integer.")



st.markdown("**4. What did you set out to study? (i.e. what was the point of your project? This should be close to your Milestone 1 assignment, but if you switched gears or changed things, note it here.)**")
st.write("Ans: Initially, the project aimed to study the correlation between player auction prices and their performance metrics. However, due to limited data availability, the focus shifted to analyzing batting and bowling statistics for the 2023 IPL season. Data from sources such as API calls, web scrapping of ESPN Cricinfo website and Kaggle 2023 IPL Auction Dataset were consolidated, and insights were drawn from player performances and comparisons.")



st.markdown("**5. What did you Discover/what were your conclusions (i.e. what were your findings? Were your original assumptions confirmed, etc.?)**")
st.write("Ans: The Streamlit app provides a user-friendly platform for cricket enthusiasts to analyze batting and bowling statistics from the 2023 IPL season. Key findings include insights into wickets distribution, batting averages, and player comparisons. Notably, the updated code ensures better readability by starting the table index from 1, enhancing the overall user experience and facilitating comprehensive cricket analysis.")



st.markdown("**6. What difficulties did you have in completing the project?**")
st.write("Ans: Challenges during project completion included efficiently managing and visualizing large datasets within the Streamlit app, ensuring smooth integration of statistical analyses, and addressing user interface design considerations. Despite these hurdles, careful planning, testing, and iterative development enabled successful project completion.")



st.markdown("**7. What skills did you wish you had while you were doing the project?**")
st.write("Ans: Enhanced proficiency in Streamlit and advanced data visualization techniques, particularly with tools like Plotly, would have been beneficial for smoother project execution.")



st.markdown("**8. What would you do 'next' to expand or augment the project?**")
st.write("Ans: Future project expansions could include in-depth analysis of player performance based on age, comparison of players' IPL performance over multiple seasons, and integration of international cricket performance data. Additionally, incorporating historical player records and exploring correlations between various performance metrics could provide deeper insights into player performance trends.")

