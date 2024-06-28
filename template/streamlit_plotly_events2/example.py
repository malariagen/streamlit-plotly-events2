import streamlit as st
from streamlit_plotly_events import plotly_events as plotly_events_old
from streamlit_plotly_events2 import plotly_events
import plotly.graph_objects as go

# Sample data
categories = ['Category A', 'Category B', 'Category C']
sub_categories = ['Sub-category 1', 'Sub-category 2', 'Sub-category 3']
data = {
    'Category A': [10, 20, 30],
    'Category B': [20, 15, 25],
    'Category C': [30, 25, 15]
}

# Colors for each sub-category
colors = ['#636EFA', '#EF553B', '#00CC96']

# Create traces
traces = []
for sub_category, values, color in zip(sub_categories, zip(*data.values()), colors):
    traces.append(go.Bar(
        name=sub_category,
        x=categories,
        y=values,
        marker=dict(color=color)
    ))

fig = go.Figure(data=traces)
fig.update_layout(barmode='stack', title='Stacked Bar Chart Example')
obj = st.plotly_chart(fig)
st.text(obj)

st.divider()

config = {
    "displayModeBar": False,  # Disable the mode bar (buttons on top of plot)
    "scrollZoom": False,      # Disable zooming
    "displaylogo": False,     # Optionally, hide the Plotly logo
    "modeBarButtonsToRemove": ["lasso2d", "autoScale2d"],  # Remove specific mode bar buttons
    "toImageButtonOptions": {  # Customize the download plot as image button
        "format": "svg",       # SVG format
        "filename": "custom-plot",  # Filename without extension
        "height": 500,         # Image height in pixels
        "width": 700,          # Image width in pixels
        "scale": 1             # Increase/decrease image resolution
    },
    "yaxis": {
        "fixedrange":True
    },
    "dragmode": False
}

fig.update_layout(
        title={
            'text': f"Pf-HaploAtlas Abacus plot)",
            'y':0.99,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {
                'size': 14,
            }},
        xaxis = dict(tickvals = [], fixedrange=True, zeroline=False),
        yaxis = dict(tickvals = [], fixedrange=True, zeroline=False),
        margin=dict(t=50, b=55, l=0, r=0)
    )

st.title("New updated version")
output = plotly_events(fig, config=config)
st.json(output)

st.divider()

st.title("Old community version")
output = plotly_events_old(fig)
st.json(output)
