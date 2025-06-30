#performs PCA for simple autoencoder/decoder

# load the pre-trained simple autoencoder model
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Flatten
import os
import numpy as np
from PIL import Image
from sklearn.decomposition import PCA
import pickle

autoencoder = load_model("../models/model_strided_autoencoder.keras")
# checked layer name with autoencoder.summary()

encoder = Model(inputs=autoencoder.input, outputs=autoencoder.get_layer('conv2d_10').output)
flat_output = Flatten()(encoder.output)
flat_encoder = Model(inputs=encoder.input, outputs=flat_output)

# copied load_n_images from train_models.py 
def load_n_images(folder_path, n=5000, target_size=(96, 96)):
    image_list = []
    filenames = sorted([f for f in os.listdir(folder_path) if f.endswith(".jpg")])[:n]

    for filename in filenames:
        img_path = os.path.join(folder_path, filename)
        img = Image.open(img_path).convert("RGB").resize(target_size)
        img_array = np.asarray(img, dtype=np.float32) / 255.0  # Normalize to [0, 1]
        image_list.append(img_array)

    return np.array(image_list)

# Load training data
train_clean_dir = "../data/stl10_train"
x_train_clean = load_n_images(train_clean_dir)

# Extract encoder model up to the bottleneck layer
encoder = Model(inputs=autoencoder.input,
                outputs=autoencoder.get_layer('conv2d_10').output)

# Encode the input images
encoded_images = encoder.predict(x_train_clean, batch_size=32)

# Flatten each encoded image: (24, 24, 16) → (9216,)
flat_encoded = encoded_images.reshape(len(encoded_images), -1)
#print(flat_encoded.shape)  # e.g., (5000, 9216)

# Fit PCA
pca = PCA(n_components=0.95)  # retain 95% of the variance
pca_latents = pca.fit_transform(flat_encoded)


# save required components 
np.save("../models/pca_latents.npy", pca_latents)                     # Compressed
np.save("../models/encoded_shape.npy", np.array([24, 24, 16]))        # Shape hint
with open("../models/pca_model.pkl", "wb") as f:
    pickle.dump(pca, f)                                     # PCA object
decoder.save("../models/decoder_model.keras")                         # Decoder model
