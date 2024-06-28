import os
import streamlit.components.v1 as components
from json import loads, dumps

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "plotly_events",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("plotly_events", path=build_dir)

def plotly_events(
    plot_fig,
    click_event=True,
    select_event=False,
    hover_event=False,
    override_height=450,
    override_width="100%",
    config={},
    key=None,
):
    component_value = _component_func(
        plot_obj=plot_fig.to_json(),
        override_height=override_height,
        override_width=override_width,
        config=dumps(config),
        key=key,
        click_event=click_event,
        select_event=select_event,
        hover_event=hover_event,
        default="[]",
    )

    return loads(component_value)