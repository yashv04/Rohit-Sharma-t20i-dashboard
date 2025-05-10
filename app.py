import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

# Setting page configuration
st.set_page_config(layout="wide", page_title="Rohit Sharma T20I Career Analysis")

# Title and description
st.title("Rohit Sharma: T20I Career Analysis")
st.markdown("An interactive analysis of Rohit Sharma's T20I career statistics (2007-2024)")

# Define the data based on the PDF
# Career Phase Data
phase_data = pd.DataFrame({
    'Phase': ['2007-2010', '2011-2015', '2016-2020', '2021-2024'],
    'Matches': [22, 49, 46, 34],
    'Innings': [19, 46, 44, 34],
    'Runs': [325, 1136, 1596, 1174],
    'Average': [21.67, 31.55, 39.90, 36.68],
    'Strike_Rate': [116.07, 130.12, 145.09, 152.47],
    'Fifties': [1, 7, 12, 9],
    'Hundreds': [0, 1, 2, 2]
})

# Opposition data
opposition_data = pd.DataFrame({
    'Opposition': ['Australia', 'Bangladesh', 'England', 'New Zealand', 
                   'Pakistan', 'South Africa', 'Sri Lanka', 'West Indies'],
    'Matches': [25, 12, 16, 21, 10, 19, 29, 15],
    'Innings': [24, 11, 16, 19, 10, 19, 27, 13],
    'Runs': [623, 452, 482, 576, 388, 571, 728, 341],
    'Average': [31.15, 56.50, 32.13, 36.00, 38.80, 35.69, 34.67, 28.42],
    'Strike_Rate': [142.98, 144.40, 139.88, 136.82, 142.65, 141.73, 146.38, 127.24],
    'High_Score': [71, 89, 100, 111, 78, 106, 118, 67],
    'Fifties': [6, 5, 3, 3, 4, 3, 3, 2],
    'Hundreds': [0, 0, 1, 1, 0, 2, 1, 0]
})

# World Cup data
worldcup_data = pd.DataFrame({
    'Tournament': ['2007', '2009', '2010', '2012', '2014', '2016', '2021', '2022', '2024'],
    'Matches': [3, 5, 5, 5, 6, 5, 5, 6, 7],
    'Runs': [88, 88, 79, 107, 200, 89, 174, 116, 257],
    'Average': [29.33, 17.60, 19.75, 26.75, 40.00, 22.25, 34.80, 19.33, 36.71],
    'Strike_Rate': [113.55, 109.37, 106.85, 127.38, 132.45, 116.11, 151.30, 106.42, 156.70],
    'High_Score': [50, 36, 33, 55, 74, 43, 74, 53, 92],
    'Fifties': [1, 0, 0, 1, 2, 0, 2, 1, 3],
    'Hundreds': [0, 0, 0, 0, 0, 0, 0, 0, 0]
})

# Venue data
venue_data = pd.DataFrame({
    'Venue_Type': ['Home', 'Away', 'Neutral'],
    'Matches': [50, 53, 48],
    'Innings': [47, 51, 45],
    'Runs': [1587, 1368, 1276],
    'Average': [38.71, 29.74, 29.67],
    'Strike_Rate': [143.91, 134.38, 139.47],
    'Fifties': [11, 10, 8],
    'Hundreds': [2, 1, 2]
})

# Captain vs Player data
captain_data = pd.DataFrame({
    'Role': ['As Captain', 'As Player'],
    'Matches': [51, 100],
    'Innings': [50, 93],
    'Runs': [1782, 2449],
    'Average': [38.74, 29.17],
    'Strike_Rate': [149.37, 133.58],
    'Fifties': [14, 15],
    'Hundreds': [3, 2]
})

# Shot distribution data
shot_data = pd.DataFrame({
    'Shot_Type': ['Front Foot Drive', 'Pull/Hook', 'Cut', 'Flick/Glance', 
                  'Square Drive', 'Lofted Drive', 'Sweep/Reverse Sweep', 'Defensive Stroke'],
    'Frequency': [19.3, 15.8, 12.6, 11.9, 10.4, 9.2, 7.8, 13.0],
    'Runs_Scored': [892, 847, 621, 528, 486, 594, 386, 110],
    'Average': [55.75, 67.76, 51.75, 48.00, 44.18, 42.43, 35.09, 0],
    'Dismissal_Rate': [5.6, 4.3, 5.2, 4.9, 6.3, 8.3, 9.2, 2.8]
})

# Six direction data
six_data = pd.DataFrame({
    'Direction': ['Long-on/Mid-wicket', 'Square-leg/Fine-leg', 'Straight/Long-off', 
                  'Cover/Extra-cover', 'Third-man/Fine-leg'],
    'Number_of_Sixes': [78, 37, 32, 23, 12],
    'Percentage': [42.9, 20.3, 17.6, 12.6, 6.6],
    'Average_Distance': [82, 79, 84, 77, 75]
})

# Scoring zones data
zone_data = pd.DataFrame({
    'Zone': ['Mid-wicket/Square-leg', 'Cover/Extra-cover', 'Long-on/Long-off', 
             'Point/Third-man', 'Fine-leg/Square-fine', 'Other'],
    'Runs': [1211, 957, 673, 628, 492, 270],
    'Percentage': [28.6, 22.6, 15.9, 14.8, 11.6, 6.5],
    'Strike_Rate': [158.47, 142.83, 151.24, 127.37, 138.59, 98.18],
    'Boundary_Percentage': [24.5, 20.8, 22.3, 17.6, 19.2, 2.1]
})

# Career summary data
career_summary = {
    'Matches': 151,
    'Innings': 143,
    'Runs': 4231,
    'Average': 32.54,
    'Strike_Rate': 139.65,
    'Highest_Score': '121*',
    'Centuries': 5,
    'Half_centuries': 29,
    'Fours': 395,
    'Sixes': 182,
    'Captain_Matches': 51,
    'Captain_Wins': 39,
    'Captain_Win_Percentage': 76.47
}

# Creating tabs for different sections
tab1, tab2, tab3, tab4 = st.tabs(["Career Overview", "Performance Analysis", "Shot Analytics", "Comparison"])

with tab1:
    # Career Summary
    st.header("Career Summary")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Matches", career_summary['Matches'])
        st.metric("Runs", career_summary['Runs'])
        st.metric("Centuries", career_summary['Centuries'])
        st.metric("Fours", career_summary['Fours'])
        
    with col2:
        st.metric("Innings", career_summary['Innings'])
        st.metric("Average", f"{career_summary['Average']:.2f}")
        st.metric("Half-centuries", career_summary['Half_centuries'])
        st.metric("Sixes", career_summary['Sixes'])
        
    with col3:
        st.metric("Highest Score", career_summary['Highest_Score'])
        st.metric("Strike Rate", f"{career_summary['Strike_Rate']:.2f}")
        st.metric("Captain Win %", f"{career_summary['Captain_Win_Percentage']:.1f}%")
    
    # Career progression chart
    st.subheader("Career Progression (2007-2024)")
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Bar(x=phase_data['Phase'], y=phase_data['Runs'], name="Runs", marker_color='royalblue'),
        secondary_y=False
    )
    
    fig.add_trace(
        go.Scatter(x=phase_data['Phase'], y=phase_data['Average'], name="Average", marker_color='red'),
        secondary_y=True
    )
    
    fig.add_trace(
        go.Scatter(x=phase_data['Phase'], y=phase_data['Strike_Rate'], name="Strike Rate", marker_color='green'),
        secondary_y=True
    )
    
    fig.update_layout(
        title_text="Runs, Average, and Strike Rate by Career Phase",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    fig.update_xaxes(title_text="Career Phase")
    fig.update_yaxes(title_text="Runs", secondary_y=False)
    fig.update_yaxes(title_text="Average / Strike Rate", secondary_y=True)
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Display milestone timeline
    st.subheader("Key Milestones")
    milestones = [
        {"year": "2007", "event": "T20I debut in the inaugural T20 World Cup"},
        {"year": "2015", "event": "First T20I century (106 vs South Africa)"},
        {"year": "2017", "event": "Joint-fastest T20I century (35 balls vs Sri Lanka)"},
        {"year": "2018", "event": "Second T20I century (100* vs England)"},
        {"year": "2018", "event": "Became India T20I captain"},
        {"year": "2022", "event": "Third T20I century (111* vs New Zealand)"},
        {"year": "2022", "event": "Fourth T20I century (104 vs South Africa)"},
        {"year": "2023", "event": "Fifth T20I century (121* vs Afghanistan)"},
        {"year": "2024", "event": "Crossed 4,000 T20I runs (second player after Virat Kohli)"}
    ]
    
    for milestone in milestones:
        st.markdown(f"**{milestone['year']}**: {milestone['event']}")

with tab2:
    st.header("Performance Analysis")
    
    # Performance by opposition
    st.subheader("Performance against Different Teams")
    
    fig = px.bar(opposition_data, x='Opposition', y='Average', color='Strike_Rate',
                 hover_data=['Runs', 'Matches', 'Hundreds', 'Fifties'],
                 color_continuous_scale='RdYlGn', height=500)
    
    fig.update_layout(title="Average and Strike Rate against Top Teams",
                     xaxis_title="Opposition", yaxis_title="Average")
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Home vs Away performance
    st.subheader("Home vs Away Performance")
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.bar(venue_data, x='Venue_Type', y=['Runs'], 
                    title="Runs by Venue Type", color='Venue_Type')
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        fig = px.bar(venue_data, x='Venue_Type', y=['Average', 'Strike_Rate'], 
                    title="Average & Strike Rate by Venue Type", barmode='group')
        st.plotly_chart(fig, use_container_width=True)
    
    # Performance in World Cup
    st.subheader("T20 World Cup Performance")
    
    fig = px.line(worldcup_data, x='Tournament', y=['Runs', 'Average', 'Strike_Rate'], 
                 title="Performance across T20 World Cups", markers=True)
    st.plotly_chart(fig, use_container_width=True)
    
    # Captain vs Player performance
    st.subheader("Performance as Captain vs Player")
    
    col1, col2 = st.columns(2)
    
    with col1:
        captain_comp = pd.melt(captain_data, id_vars=['Role'], value_vars=['Average', 'Strike_Rate'])
        fig = px.bar(captain_comp, x='Role', y='value', color='variable', barmode='group',
                    title="Average & Strike Rate Comparison")
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        # Calculate centuries per innings
        captain_data['100s_per_innings'] = captain_data['Hundreds'] / captain_data['Innings'] * 100
        captain_data['50s_per_innings'] = captain_data['Fifties'] / captain_data['Innings'] * 100
        
        milestone_comp = pd.melt(captain_data, id_vars=['Role'], 
                                value_vars=['100s_per_innings', '50s_per_innings'],
                                var_name='Milestone', value_name='Percentage')
        
        fig = px.bar(milestone_comp, x='Role', y='Percentage', color='Milestone', barmode='group',
                    title="Milestones per Innings (%)")
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.header("Shot Analytics")
    
    # Shot distribution
    st.subheader("Shot Distribution")
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.pie(shot_data, values='Frequency', names='Shot_Type', 
                    title="Shot Type Distribution (%)",
                    hover_data=['Runs_Scored', 'Average', 'Dismissal_Rate'])
        
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        fig = px.scatter(shot_data, x='Average', y='Dismissal_Rate', size='Runs_Scored', 
                        color='Shot_Type', hover_name='Shot_Type', size_max=60,
                        title="Shot Effectiveness (Average vs Dismissal Rate)")
        
        fig.update_layout(xaxis_title="Average per Shot", yaxis_title="Dismissal Rate (%)")
        st.plotly_chart(fig, use_container_width=True)
    
    # Scoring zones visualization
    st.subheader("Scoring Zones Analysis")
    
    # Create a cricket field visualization
    plt.figure(figsize=(10, 8))
    
    # Plot cricket field (simplified)
    circle = plt.Circle((0, 0), 1, fill=False, color='black')
    inner_circle = plt.Circle((0, 0), 0.3, fill=False, color='black')
    pitch = plt.Rectangle((-0.1, -0.6), 0.2, 1.2, fill=True, color='tan')
    
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.add_patch(circle)
    ax.add_patch(inner_circle)
    ax.add_patch(pitch)
    
    # Set equal aspect and limits
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_aspect('equal')
    
    # Define positions for zones (simplified)
    positions = {
        'Mid-wicket/Square-leg': (-0.6, 0.7),
        'Cover/Extra-cover': (0.6, 0.7),
        'Long-on/Long-off': (0, 1.0),
        'Point/Third-man': (0.8, 0.2),
        'Fine-leg/Square-fine': (-0.8, 0.2),
        'Other': (0, -0.8)
    }
    
    # Plot zones with size proportional to runs and color by strike rate
    for _, row in zone_data.iterrows():
        size = row['Percentage'] * 30  # Scale for visibility
        plt.scatter(positions[row['Zone']][0], positions[row['Zone']][1], 
                   s=size*100, alpha=0.6, 
                   color=plt.cm.RdYlGn(row['Strike_Rate']/180))
        plt.annotate(f"{row['Zone']}\n{row['Percentage']}%\nSR: {row['Strike_Rate']}", 
                    positions[row['Zone']], ha='center', va='center')
    
    plt.title("Rohit Sharma's Scoring Zones in T20Is")
    plt.axis('off')
    
    # Convert matplotlib plot to Streamlit
    st.pyplot(fig)
    
    # Six hitting analysis
    st.subheader("Six Hitting Analysis")
    
    fig = px.bar(six_data, x='Direction', y='Number_of_Sixes', text='Percentage',
                color='Average_Distance', color_continuous_scale='Viridis',
                title="Six Distribution by Direction")
    
    fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
    fig.update_layout(xaxis_title="Direction", yaxis_title="Number of Sixes")
    
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.header("Comparison with Contemporaries")
    
    # Create comparison data (from the PDF)
    comparison_data = pd.DataFrame({
        'Player': ['Rohit Sharma', 'Babar Azam', 'David Warner', 'Jos Buttler', 'Aaron Finch', 'KL Rahul'],
        'Matches': [148, 108, 99, 112, 103, 72],
        'Innings': [140, 104, 99, 106, 103, 70],
        'Runs': [4217, 3987, 2894, 3356, 3120, 2265],
        'Average': [32.95, 41.53, 32.15, 35.33, 31.52, 37.75],
        'Strike_Rate': [139.67, 128.76, 141.37, 144.68, 142.53, 139.12],
        'Fifties': [29, 33, 24, 24, 20, 22],
        'Hundreds': [5, 3, 1, 6, 2, 2]
    })
    
    comparison_data['Innings_per_50'] = comparison_data['Innings'] / (comparison_data['Fifties'] + comparison_data['Hundreds'])
    comparison_data['Boundary_Index'] = comparison_data['Average'] * comparison_data['Strike_Rate'] / 100
    
    # Player selection
    players = st.multiselect(
        'Select players to compare with Rohit Sharma',
        ['Babar Azam', 'David Warner', 'Jos Buttler', 'Aaron Finch', 'KL Rahul'],
        ['Babar Azam', 'Jos Buttler', 'KL Rahul'])
    
    # Filter data based on selection and always include Rohit
    filtered_data = comparison_data[comparison_data['Player'].isin(['Rohit Sharma'] + players)]
    
    # Key metrics comparison
    st.subheader("Key Metrics Comparison")
    
    metrics = ['Average', 'Strike_Rate', 'Boundary_Index', 'Innings_per_50']
    comparison_melted = pd.melt(filtered_data, id_vars=['Player'], value_vars=metrics)
    
    fig = px.bar(comparison_melted, x='Player', y='value', color='variable', barmode='group',
                title="Performance Metrics Comparison", facet_col='variable', facet_col_wrap=2)
    
    fig.update_layout(height=600)
    st.plotly_chart(fig, use_container_width=True)
    
    # Radar chart for comprehensive comparison
    st.subheader("Player Comparison - Radar Chart")
    
    # Normalize data for radar chart
    radar_metrics = ['Average', 'Strike_Rate', 'Runs', 'Fifties', 'Hundreds', 'Innings_per_50']
    radar_data = filtered_data[['Player'] + radar_metrics].copy()
    
    for metric in radar_metrics:
        if metric == 'Innings_per_50':  # Lower is better
            radar_data[metric] = 1 - (radar_data[metric] - radar_data[metric].min()) / (radar_data[metric].max() - radar_data[metric].min())
        else:  # Higher is better
            radar_data[metric] = (radar_data[metric] - radar_data[metric].min()) / (radar_data[metric].max() - radar_data[metric].min())
    
    # Create radar chart
    fig = go.Figure()
    
    for player in radar_data['Player']:
        player_data = radar_data[radar_data['Player'] == player]
        fig.add_trace(go.Scatterpolar(
            r=[player_data[metric].values[0] for metric in radar_metrics],
            theta=radar_metrics,
            fill='toself',
            name=player
        ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1]
            )),
        showlegend=True,
        title="Player Attribute Comparison"
    )
    
    st.plotly_chart(fig, use_container_width=True)

st.sidebar.header("About This Dashboard")
st.sidebar.info(
    "This interactive dashboard presents a comprehensive analysis of Rohit Sharma's T20I career statistics. "
    "Navigate through the tabs to explore different aspects of his performance."
)

st.sidebar.header("Career Highlights")
st.sidebar.markdown("""
- **5 T20I centuries** - Most by any batsman in T20Is
- **4,231 runs** - Second highest run-scorer in T20Is
- **182 sixes** - Second most sixes in T20I cricket
- **76.47% win rate as captain** - One of the most successful T20I captains
""")

st.sidebar.markdown("---")
st.sidebar.markdown("Data Source: Comprehensive Statistical Analysis of Rohit Sharma's Cricket Career (October 2024)")
