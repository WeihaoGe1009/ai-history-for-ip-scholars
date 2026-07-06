import ipywidgets as widgets

from script.config import STYLE_OPTIONS, NUM_STEPS


_state = {'content_pil': None, 'style_pil': None, 'result_pil': None}

upload_btn = widgets.FileUpload(
    accept='image/*', multiple=False,
    description='Upload image',
    button_style='info',
    layout=widgets.Layout(width='155px'),
)
random_btn = widgets.Button(
    description='Random STL-10',
    button_style='primary',
    icon='random',
    layout=widgets.Layout(width='155px'),
)
style_dd = widgets.Dropdown(
    options=list(STYLE_OPTIONS.keys()),
    description='Style:',
    style={'description_width': '50px'},
    layout=widgets.Layout(width='370px'),
)
run_btn = widgets.Button(
    description='Run Style Transfer',
    button_style='success',
    icon='paint-brush',
    layout=widgets.Layout(width='185px'),
)
status_lbl = widgets.Label(
    value='Step 1: upload an image or pick a random STL-10 example.',
)
progress_bar = widgets.IntProgress(
    value=0, min=0, max=NUM_STEPS,
    description='',
    bar_style='info',
    layout=widgets.Layout(width='500px', visibility='hidden'),
)
progress_lbl = widgets.Label(
    value='',
    layout=widgets.Layout(visibility='hidden'),
)
result_out = widgets.Output()

ui = widgets.VBox([
    widgets.HBox([upload_btn, random_btn]),
    widgets.HBox([style_dd, run_btn]),
    status_lbl,
    progress_bar,
    progress_lbl,
    result_out,
])
