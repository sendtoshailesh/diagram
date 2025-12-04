"""
Plotly - Interactive Visualizations
Install: pip install plotly pandas
"""

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd

# Create sample data
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=100)
df = pd.DataFrame({
    'date': dates,
    'sales': np.cumsum(np.random.randn(100)) + 100,
    'costs': np.cumsum(np.random.randn(100)) + 80,
    'profit': np.random.randn(100) * 10 + 20
})

# Create subplots
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Line Chart', 'Scatter Plot', 'Bar Chart', '3D Surface'),
    specs=[[{'type': 'scatter'}, {'type': 'scatter'}],
           [{'type': 'bar'}, {'type': 'surface'}]]
)

# 1. Line Chart
fig.add_trace(
    go.Scatter(x=df['date'], y=df['sales'], name='Sales', line=dict(color='blue')),
    row=1, col=1
)
fig.add_trace(
    go.Scatter(x=df['date'], y=df['costs'], name='Costs', line=dict(color='red')),
    row=1, col=1
)

# 2. Scatter Plot
fig.add_trace(
    go.Scatter(
        x=df['sales'], 
        y=df['profit'],
        mode='markers',
        marker=dict(
            size=8,
            color=df['costs'],
            colorscale='Viridis',
            showscale=True
        ),
        name='Sales vs Profit'
    ),
    row=1, col=2
)

# 3. Bar Chart
categories = ['Q1', 'Q2', 'Q3', 'Q4']
values = [45, 67, 89, 102]
fig.add_trace(
    go.Bar(x=categories, y=values, name='Quarterly Revenue',
           marker_color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']),
    row=2, col=1
)

# 4. 3D Surface
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

fig.add_trace(
    go.Surface(x=X, y=Y, z=Z, colorscale='Viridis', name='3D Surface'),
    row=2, col=2
)

# Update layout
fig.update_layout(
    title_text="Interactive Dashboard with Plotly",
    showlegend=True,
    height=800,
    width=1200
)

# Save as HTML (interactive)
fig.write_html('plotly_dashboard.html')
print("Interactive dashboard saved as 'plotly_dashboard.html'")

# Also save as static image (requires kaleido: pip install kaleido)
try:
    fig.write_image('plotly_dashboard.png', width=1200, height=800)
    print("Static image saved as 'plotly_dashboard.png'")
except Exception as e:
    print(f"To save static images, install kaleido: pip install kaleido")

# Create a separate animated chart
fig_animated = px.scatter(
    df, 
    x='sales', 
    y='profit',
    animation_frame=df.index,
    size='costs',
    color='costs',
    hover_name=df.index,
    range_x=[df['sales'].min()-10, df['sales'].max()+10],
    range_y=[df['profit'].min()-10, df['profit'].max()+10],
    title='Animated Scatter Plot'
)

fig_animated.write_html('plotly_animated.html')
print("Animated chart saved as 'plotly_animated.html'")
