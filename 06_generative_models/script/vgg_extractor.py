import torch
import torch.nn as nn
import torchvision.models as models

from script.config import DEVICE


class VGGExtractor(nn.Module):
    """
    Extracts VGG-19 features at fixed layer indices for neural style transfer.

    VGG-19 features layer reference:
        1  -> relu1_1 (style)     6  -> relu2_1 (style)
       11  -> relu3_1 (style)    20  -> relu4_1 (style)
       22  -> relu4_2 (content)  29  -> relu5_1 (style)

    ImageNet normalisation is applied internally; expects [0, 1] input tensors.
    """
    CONTENT_IDX = 22
    STYLE_IDXS  = [1, 6, 11, 20, 29]

    def __init__(self):
        super().__init__()
        vgg = models.vgg19(weights=models.VGG19_Weights.DEFAULT).features
        vgg.eval()
        for p in vgg.parameters():
            p.requires_grad_(False)
        keep      = max(self.CONTENT_IDX, max(self.STYLE_IDXS)) + 1
        self.net  = nn.Sequential(*list(vgg.children())[:keep]).to(DEVICE)
        self.mean = torch.tensor([0.485, 0.456, 0.406]).view(1, 3, 1, 1).to(DEVICE)
        self.std  = torch.tensor([0.229, 0.224, 0.225]).view(1, 3, 1, 1).to(DEVICE)

    def forward(self, x):
        x = (x - self.mean) / self.std
        feats = {}
        for i, layer in enumerate(self.net):
            x = layer(x)
            if i == self.CONTENT_IDX or i in self.STYLE_IDXS:
                feats[i] = x
        return feats


def gram_matrix(feat):
    b, c, h, w = feat.size()
    f = feat.view(b * c, h * w)
    return torch.mm(f, f.t()).div(c * h * w)


_extractor = None


def get_extractor():
    """Return the shared VGGExtractor singleton, downloading weights on first call."""
    global _extractor
    if _extractor is None:
        print('Loading style transfer model ...')
        _extractor = VGGExtractor()
        print('Model ready.')
    return _extractor
