#!/usr/bin/env python
"""
SpaceX Falcon 9 Landing Prediction - Dash Interactive Dashboard
"""

import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('/root/spacex_capstone/data/spacex_launches_processed.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Initialize Dash app
app = dash.Dash(__name__)
app.title = 'SpaceX Falcon 9 Launch Analysis Dashboard'

# Define colors
colors = {
    'background': '#f8f9fa',
    'text': '#212529',
    'success': '#2ecc71',
    'failure': '#e74c3c'
}

# Calculate statistics
success_by_site = df.groupby('Launch_Site')['Class'].agg(['sum', 'count'])
success_by_site['rate'] = (success_by_site['sum'] / success_by_site['count'] * 100)

overall_success = df['Class'].mean() * 100
total_launches = len(df)
successful_launches = df['Class'].sum()

# App layout
app.layout = html.Div(
    style={'backgroundColor': colors['background']},
    children=[
        html.Div(
            className='header',
            style={
                'backgroundColor': '#1e3a8a',
                'color': 'white',
                'padding': '20px',
                'marginBottom': '30px',
                'textAlign': 'center'
            },
            children=[
                html.H1('SpaceX Falcon 9 First-Stage Landing Prediction',
                       style={'margin': '0', 'fontSize': '32px', 'fontWeight': 'bold'}),
                html.P('Interactive Dashboard for Launch Analysis',
                      style={'margin': '10px 0 0 0', 'fontSize': '16px', 'opacity': '0.9'})
            ]
        ),

        # Key metrics
        html.Div(
            style={'display': 'flex', 'justifyContent': 'space-around', 'marginBottom': '30px', 'padding': '20px'},
            children=[
                html.Div(
                    style={
                        'backgroundColor': 'white',
                        'padding': '20px',
                        'borderRadius': '8px',
                        'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
                        'textAlign': 'center',
                        'flex': '1',
                        'margin': '0 10px'
                    },
                    children=[
                        html.H3(f'{total_launches}', style={'color': '#1e3a8a', 'margin': '0'}),
                        html.P('Total Launches', style={'margin': '5px 0 0 0', 'color': '#666'})
                    ]
                ),
                html.Div(
                    style={
                        'backgroundColor': 'white',
                        'padding': '20px',
                        'borderRadius': '8px',
                        'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
                        'textAlign': 'center',
                        'flex': '1',
                        'margin': '0 10px'
                    },
                    children=[
                        html.H3(f'{successful_launches}', style={'color': colors['success'], 'margin': '0'}),
                        html.P('Successful Landings', style={'margin': '5px 0 0 0', 'color': '#666'})
                    ]
                ),
                html.Div(
                    style={
                        'backgroundColor': 'white',
                        'padding': '20px',
                        'borderRadius': '8px',
                        'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
                        'textAlign': 'center',
                        'flex': '1',
                        'margin': '0 10px'
                    },
                    children=[
                        html.H3(f'{overall_success:.1f}%', style={'color': '#3498db', 'margin': '0'}),
                        html.P('Success Rate', style={'margin': '5px 0 0 0', 'color': '#666'})
                    ]
                )
            ]
        ),

        # Controls and charts
        html.Div(
            style={'padding': '20px'},
            children=[
                # Payload range slider
                html.Div(
                    style={'marginBottom': '30px', 'backgroundColor': 'white', 'padding': '20px', 'borderRadius': '8px'},
                    children=[
                        html.Label('Filter by Payload Mass (kg):', style={'fontWeight': 'bold', 'marginBottom': '10px'}),
                        dcc.RangeSlider(
                            id='payload-slider',
                            min=df['Payload_Mass_kg'].min(),
                            max=df['Payload_Mass_kg'].max(),
                            value=[df['Payload_Mass_kg'].min(), df['Payload_Mass_kg'].max()],
                            marks={
                                int(df['Payload_Mass_kg'].min()): f'{int(df["Payload_Mass_kg"].min())} kg',
                                int(df['Payload_Mass_kg'].max()): f'{int(df["Payload_Mass_kg"].max())} kg'
                            },
                            tooltip={'placement': 'bottom', 'always_visible': True},
                            style={'marginTop': '20px'}
                        )
                    ]
                ),

                # Charts grid
                html.Div(
                    style={'display': 'grid', 'gridTemplateColumns': '1fr 1fr', 'gap': '20px', 'marginBottom': '20px'},
                    children=[
                        html.Div(
                            style={'backgroundColor': 'white', 'padding': '20px', 'borderRadius': '8px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'},
                            children=[dcc.Graph(id='success-by-site')]
                        ),
                        html.Div(
                            style={'backgroundColor': 'white', 'padding': '20px', 'borderRadius': '8px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'},
                            children=[dcc.Graph(id='success-rate-site')]
                        ),
                        html.Div(
                            style={'backgroundColor': 'white', 'padding': '20px', 'borderRadius': '8px', 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)', 'gridColumn': '1 / -1'},
                            children=[dcc.Graph(id='payload-scatter')]
                        )
                    ]
                )
            ]
        )
    ]
)


# Callbacks
@app.callback(
    [Output('success-by-site', 'figure'),
     Output('success-rate-site', 'figure'),
     Output('payload-scatter', 'figure')],
    [Input('payload-slider', 'value')]
)
def update_charts(payload_range):
    # Filter data by payload range
    filtered_df = df[(df['Payload_Mass_kg'] >= payload_range[0]) &
                     (df['Payload_Mass_kg'] <= payload_range[1])]

    # Chart 1: Successful launches by site (pie)
    success_counts = filtered_df[filtered_df['Class'] == 1].groupby('Launch_Site').size()
    fig1 = go.Figure(data=[go.Pie(
        labels=success_counts.index,
        values=success_counts.values,
        marker=dict(colors=['#2ecc71', '#3498db', '#f39c12']),
        textposition='inside',
        textinfo='label+percent'
    )])
    fig1.update_layout(
        title='Successful Launches by Site',
        height=400,
        showlegend=True
    )

    # Chart 2: Success rate by site (pie)
    site_stats = filtered_df.groupby('Launch_Site')['Class'].agg(['sum', 'count'])
    site_stats['rate'] = (site_stats['sum'] / site_stats['count'] * 100).round(1)

    fig2 = go.Figure(data=[go.Pie(
        labels=[f"{site}<br>({rate:.1f}%)" for site, rate in zip(site_stats.index, site_stats['rate'])],
        values=site_stats['count'],
        marker=dict(colors=['#1e3a8a', '#0ea5e9']),
        textposition='inside',
        textinfo='label'
    )])
    fig2.update_layout(
        title='Launch Distribution by Site (Success Rate %)',
        height=400,
        showlegend=False
    )

    # Chart 3: Payload vs Landing Outcome (scatter)
    fig3 = px.scatter(
        filtered_df,
        x='Payload_Mass_kg',
        y='Flight_Number',
        color='Class',
        size='Payload_Mass_kg',
        hover_data=['Date', 'Launch_Site', 'Orbit'],
        color_discrete_map={1: colors['success'], 0: colors['failure']},
        labels={'Class': 'Outcome', 'Payload_Mass_kg': 'Payload Mass (kg)', 'Flight_Number': 'Flight Number'},
        title='Payload Mass vs Flight Number (Colored by Success)'
    )
    fig3.update_layout(height=400)

    return fig1, fig2, fig3


if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=8050)
