import os, glob, random
from PIL import Image


def get_random_stl10(sub_dir):
    """Return a random PIL Image from the pre-saved STL-10 subset directory."""
    files = (glob.glob(os.path.join(sub_dir, '*.jpg')) +
             glob.glob(os.path.join(sub_dir, '*.jpeg')))
    if not files:
        raise FileNotFoundError(
            f'No images found in {sub_dir!r}. '
            'Run the STL-10 setup cell first.'
        )
    return Image.open(random.choice(files)).convert('RGB')
