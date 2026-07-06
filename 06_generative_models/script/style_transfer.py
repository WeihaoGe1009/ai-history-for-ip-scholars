import torch
import torch.nn as nn
import torch.optim as optim

from script.config import NUM_STEPS, CONTENT_WEIGHT, STYLE_WEIGHT
from script.vgg_extractor import VGGExtractor, get_extractor, gram_matrix


def run_style_transfer(content_tensor, style_tensor,
                       num_steps=NUM_STEPS,
                       content_weight=CONTENT_WEIGHT,
                       style_weight=STYLE_WEIGHT,
                       on_progress=None):
    """
    Gatys et al. (2015) neural style transfer via direct image optimisation.

    Args:
        content_tensor: [0, 1] float tensor, shape (1, 3, H, W)
        style_tensor:   [0, 1] float tensor, shape (1, 3, H', W')
        on_progress:    optional callable(step, total, c_loss, s_loss) called
                        on every step so the caller can update a progress widget.
    Returns:
        Stylised image tensor, same shape as content_tensor.
    """
    ext = get_extractor()

    with torch.no_grad():
        cf = ext(content_tensor)
        sf = ext(style_tensor)

    target_content = cf[VGGExtractor.CONTENT_IDX].detach()
    target_grams   = {i: gram_matrix(sf[i]).detach() for i in VGGExtractor.STYLE_IDXS}

    output    = content_tensor.clone().detach().requires_grad_(True)
    optimizer = optim.Adam([output], lr=0.02)

    for step in range(1, num_steps + 1):
        optimizer.zero_grad()

        feats  = ext(output)
        c_loss = nn.functional.mse_loss(feats[VGGExtractor.CONTENT_IDX], target_content)
        s_loss = sum(
            nn.functional.mse_loss(gram_matrix(feats[i]), target_grams[i])
            for i in VGGExtractor.STYLE_IDXS
        )
        (content_weight * c_loss + style_weight * s_loss).backward()
        optimizer.step()

        with torch.no_grad():
            output.data.clamp_(0, 1)

        if on_progress:
            on_progress(step, num_steps, c_loss.item(), s_loss.item())

    return output.detach()
