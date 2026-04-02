# Autoencoders & Compression: A Responsive Perspective 

What does this module do, what is autoencoder, what do we learn

---

## What's inside
- `04_autoencoder.ipynb` The interactive Google Colab notebook ([Run on Google Colab](https://colab.research.google.com/github/WeihaoGe1009/ai-history-for-ip-scholars/blob/main/04_autoencoders/04_autoencoder.ipynb))
* It is the main notebook containing
* visual walkthrough of autoencoder reconstruction
* comparison of outputs
* under-the-hood visualization (layer outputs, compressed representation)
* Applications and IP-relevant insights 

- scripts/
Core utilities and training code:

`download_stl10.py`
→ Download and extract STL-10 dataset from Stanford's website.

`preprocess_stl10.py`
→ Parse binary `.bin` files and convert to `.jpg` images in `stl10_train_images_96x96/` and `stl10_test_images_96x96/`.

`add_noise.py`
→ Add Gaussian noise to images in `stl10_train_images_96x96/` and `stl10_test_images_96x96/`, saving results to `stl10_train_noisy_images_96x96/` and `stl10_test_noisy_images_96x96/`.

`train_model.py`
→ Load clean/noisy training images and train multiple autoencoder models:

Flat Convolutional Autoencoder

MaxPooling + UpSampling Autoencoder

Strided Convolution + Transpose Autoencoder (used in our demo)
conv + stride + dense

denoising (noisy input → clean output)

→ Save trained models as .keras files.

- data/

Small demo input set (pre-selected subset from test set):

`stl10_demo_input/`
→ A few clean .jpg images (e.g., 10–20) used for inference and visualization in notebook.

`stl10_demo_noisy/`
→ Corresponding noisy .jpg images.

- models/
Pretrained Keras model files:
* `model_flat_conv_autoencoder.keras`
* `model_maxpool_autoencoder.keras`
* `model_strided_autoencoder.keras`


---

## What You'll learn

## Take-Home Message
 Module 4: Autoencoders & Compression — A Responsible Perspective
### 1. Opening Demonstration: Yes, Autoencoders Can Reconstruct
Show a familiar image reconstructed after encoding/decoding

Acknowledge the discomfort: “This feels too close — and creators have reason to be uneasy.”

### 2.  Why This Happens
Explain: Model learns statistical structure, not pixel memory

Still, reconstructions can appear similar due to the input being used for training

### 3. Real Risk Acknowledgement
Even if not exact copies, output similarity can dilute original work’s value or cause unintentional infringement

### 4. Ethical Use: Draw the Line
* Learning: Internal compression, denoising, feature discovery
* Publishing or Remixing: Needs safeguards and creator respect
* Introduce Ideas (brief, no demo):
* Similarity checking (e.g., perceptual hashing, embedding distance)
* Filters to prevent generation near copyrighted training data

### 5. Positive Applications (Lightweight Demos)
* Compression: Visualize reduced-size representations
* Denoising: Show noisy → clean image
* Anomaly Detection: Outlier image yields high reconstruction error



## Data

## Data Source:

## References

**STL-10 Images** 
Adam Coates, Honglak Lee, Andrew Y. Ng An Analysis of Single Layer Networks in Unsupervised Feature Learning AISTATS, 2011. http://cs.stanford.edu/~acoates/stl10

