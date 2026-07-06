import torch

STYLE_OPTIONS = {
    'Starry Night  (Van Gogh, 1889)': 'starry_night.jpg',
    'The Great Wave (Hokusai, 1831)': 'great_wave.jpg',
    'Kandinsky Abstract (1923)':      'kandinsky_comp8.jpg',
    'Byzantine Mosaic (~6th c.)':     'byzantine_mosaic.jpeg',
}

CONTENT_MAX_PX = 256
STYLE_MAX_PX   = 512
NUM_STEPS      = 300
CONTENT_WEIGHT = 1e5
STYLE_WEIGHT   = 3e10

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
