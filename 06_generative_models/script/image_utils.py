import os, io
import urllib.request
import torchvision.transforms as transforms
from PIL import Image

from script.config import DEVICE


def _pil_from_source(source):
    """Load a PIL Image from a local path, HTTP(S) URL, raw bytes, or PIL Image."""
    if isinstance(source, (bytes, bytearray, memoryview)):
        return Image.open(io.BytesIO(bytes(source))).convert('RGB')
    if isinstance(source, str) and (source.startswith('http://') or
                                    source.startswith('https://')):
        with urllib.request.urlopen(source) as resp:
            return Image.open(io.BytesIO(resp.read())).convert('RGB')
    if isinstance(source, (str, os.PathLike)):
        return Image.open(source).convert('RGB')
    return source.convert('RGB')


def load_image(source, max_px):
    """Load and resize to max_px on longest edge; return a [0, 1] float tensor."""
    img   = _pil_from_source(source)
    w, h  = img.size
    scale = max_px / max(w, h)
    img   = img.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.LANCZOS)
    return transforms.ToTensor()(img).unsqueeze(0).to(DEVICE)


def tensor_to_pil(t):
    return transforms.ToPILImage()(t.cpu().squeeze(0).clamp(0, 1))
