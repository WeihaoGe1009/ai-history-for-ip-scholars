import io
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Register HEIC/HEIF support (iPhone photos) if the plugin is installed
try:
    from pillow_heif import register_heif_opener
    register_heif_opener()
except ImportError:
    pass

from script.config        import STYLE_OPTIONS, CONTENT_MAX_PX, STYLE_MAX_PX
from script.image_utils   import _pil_from_source, load_image, tensor_to_pil
from script.style_transfer import run_style_transfer
from script.stl10_loader  import get_random_stl10
from script.ui_widgets    import _state, upload_btn, random_btn, style_dd, run_btn, \
                                 status_lbl, result_out


def _bytes_to_pil(content):
    """Convert raw upload bytes to a PIL RGB image, trying multiple decoders."""
    # 1. PIL — covers JPEG, PNG, BMP, GIF, TIFF, WebP, HEIC (with plugin)
    try:
        return Image.open(io.BytesIO(content)).convert('RGB')
    except Exception:
        pass

    # 2. imageio — handles formats PIL misses (e.g. 16-bit TIFFs, some RAW previews)
    try:
        import imageio
        arr = imageio.v3.imread(io.BytesIO(content))
        return Image.fromarray(arr).convert('RGB')
    except Exception:
        pass

    # 3. OpenCV — last resort, very broad format support
    try:
        import cv2
        arr = np.frombuffer(content, dtype=np.uint8)
        bgr = cv2.imdecode(arr, cv2.IMREAD_COLOR)
        if bgr is not None:
            return Image.fromarray(cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB))
    except Exception:
        pass

    raise ValueError('Unrecognised image format. Please upload a JPG, PNG, WebP, or HEIC file.')


def register_handlers(style_library, stl10_sub_dir):
    """Wire up all button/upload callbacks. Call once after the UI is imported."""

    def _set_content(pil_img):
        _state['content_pil'] = pil_img
        status_lbl.value = (f'Input image loaded ({pil_img.width}×{pil_img.height} px). '
                            'Choose a style and click Run Style Transfer.')

    def on_upload(change):
        if not upload_btn.value:
            return
        try:
            # Always use the most recently uploaded file (last in accumulated list)
            val  = upload_btn.value
            info = val[-1] if isinstance(val, (tuple, list)) else list(val.values())[-1]
            raw  = info.get('content', b'')
            content = raw.tobytes() if hasattr(raw, 'tobytes') else bytes(raw)
            _set_content(_bytes_to_pil(content))
        except Exception as exc:
            status_lbl.value = f'Could not load image: {exc}'

    upload_btn.observe(on_upload, names='value')

    def on_random(_):
        status_lbl.value = 'Loading a random STL-10 image ...'
        try:
            _set_content(get_random_stl10(stl10_sub_dir))
        except Exception as exc:
            status_lbl.value = f'Error: {exc}'

    random_btn.on_click(on_random)

    def on_run(_):
        # If state was cleared (e.g. handlers reloaded) but uploads exist, recover the latest
        if _state['content_pil'] is None and upload_btn.value:
            try:
                val  = upload_btn.value
                info = val[-1] if isinstance(val, (tuple, list)) else list(val.values())[-1]
                raw  = info.get('content', b'')
                content = raw.tobytes() if hasattr(raw, 'tobytes') else bytes(raw)
                _set_content(_bytes_to_pil(content))
            except Exception:
                pass

        if _state['content_pil'] is None:
            status_lbl.value = 'Please load an input image first.'
            return

        run_btn.disabled = True

        def _progress(step, total, c_loss, s_loss):
            status_lbl.value = f'Applying style… {step} / {total} steps complete'

        try:
            import os
            path      = os.path.join(style_library, STYLE_OPTIONS[style_dd.value])
            content_t = load_image(_state['content_pil'], CONTENT_MAX_PX)
            style_t   = load_image(path, STYLE_MAX_PX)
            out_t     = run_style_transfer(content_t, style_t, on_progress=_progress)
            _state['result_pil'] = tensor_to_pil(out_t)
            _state['style_pil']  = _pil_from_source(path)
            status_lbl.value = 'Done! Result shown below.'

            with result_out:
                result_out.clear_output(wait=True)
                fig, axes = plt.subplots(1, 3, figsize=(14, 5))
                for ax, img, title in zip(
                    axes,
                    [_state['content_pil'], _state['style_pil'], _state['result_pil']],
                    ['Input', 'Style', 'Stylised'],
                ):
                    ax.imshow(np.array(img))
                    ax.set_title(title, fontsize=13)
                    ax.axis('off')
                plt.tight_layout()
                plt.show()
                plt.close(fig)

        except Exception as exc:
            status_lbl.value = f'Error: {exc}'

        run_btn.disabled = False

    run_btn.on_click(on_run)
