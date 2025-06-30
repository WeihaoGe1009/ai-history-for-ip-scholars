# this is the code to train the simplest autoencoder in the demo
# in order to remove noise and sharpen the images
# we train the same model structure three times
# assuming data preprocessing and add_noise are already run

import tensorflow as tf
import os
import numpy as np
from PIL import Image
import pandas as pd
from glob import glob
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from tensorflow.keras import layers, models


# Define paths to the data
train_noisy_dir = "../stl10_train_noisy_images_96x96"
train_clean_dir = "../stl10_train_images_96x96"
test_noisy_dir = "../stl10_test_noisy_images_96x96"
test_clean_dir = "../stl10_test_images_96x96"

# define an image loading helper

def load_n_images(folder_path, n=5000, target_size=(96, 96)):
    image_list = []
    filenames = sorted([f for f in os.listdir(folder_path) if f.endswith(".jpg")])[:n]

    for filename in filenames:
        img_path = os.path.join(folder_path, filename)
        img = Image.open(img_path).convert("RGB").resize(target_size)
        img_array = np.asarray(img, dtype=np.float32) / 255.0  # Normalize to [0, 1]
        image_list.append(img_array)

    return np.array(image_list)

# Load data
x_train_noisy = load_n_images(test_noisy_dir, n=5)
x_train_clean = load_n_images(test_clean_dir, n=5)
x_test_noisy = load_n_images(test_noisy_dir, n=5)
x_test_clean = load_n_images(test_clean_dir, n=5)

print("Test data shape:", x_test_noisy.shape, x_test_clean.shape)

# for systems with smaller RAM, instead of loading the training data data altogether,
# we stream the data with DataFrame

# load the training data
# collect the file paths
noisy_files = sorted(glob(os.path.join(train_noisy_dir, '*.jpg')))
clean_files = sorted(glob(os.path.join(train_clean_dir, '*.jpg')))

# Sanity check
assert len(noisy_files) == len(clean_files)

# Build dataframe
df = pd.DataFrame({
    'noisy': noisy_files,
    'clean': clean_files
})


# Generator for noisy input
noisy_gen = datagen.flow_from_dataframe(
    dataframe=df,
    x_col='noisy',
    y_col=None,
    target_size=(96, 96),
    batch_size=32,
    class_mode=None,
    shuffle=False,
    seed=42
)

# Generator for clean targets
clean_gen = datagen.flow_from_dataframe(
    dataframe=df,
    x_col='clean',
    y_col=None,
    target_size=(96, 96),
    batch_size=32,
    class_mode=None,
    shuffle=False,
    seed=42
)

train_gen = zip(noisy_gen, clean_gen)

def paired_generator_func(noisy_gen, clean_gen):
    while True:
        x_batch = next(noisy_gen)
        y_batch = next(clean_gen)
        yield x_batch, y_batch


# Define denoising autoencoder model

def denoising_autoencoder(input_shape=(96, 96, 3)):
    input_img = layers.Input(shape=input_shape)

    # Encoder
    x = layers.Conv2D(32, (3, 3), activation="relu", padding="same", strides=1)(input_img)
    x = layers.Conv2D(64, (3, 3), activation="relu", padding="same", strides=1)(x)
    x = layers.Conv2D(128, (3, 3), activation="relu", padding="same", strides=1)(x)
    encoded = x

    # Decoder
    x = layers.Conv2DTranspose(64, (3, 3), activation="relu", padding="same", strides=1)(encoded)
    x = layers.Conv2DTranspose(32, (3, 3), activation="relu", padding="same", strides=1)(x)
    decoded = layers.Conv2DTranspose(3, (3, 3), activation="sigmoid", padding="same", strides=1)(x)

    return models.Model(input_img, decoded, name="denoising_autoencoder")

# Compile and train

# phase 1, remove noise
model = denoising_autoencoder()
model.compile(optimizer="adam", loss="mse")

model.fit(
    paired_generator_func(noisy_gen, clean_gen),
    steps_per_epoch=len(noisy_gen),
    epochs=12
)

# phase 2, enhance sharpness
# note: in fact, we trained and saved phase 1 first,
# then train phase 2 and 3 separately.
# Somehow at this stage, we didn't encounter the RAM issue
# therefore we didn't use the DataFrame streaming method to load data

blurred_images  = model.predict(x_train_clean)

model2 = denoising_autoencoder()
model2.compile(optimizer="adam", loss="mse")

model2.fit(
    x=blurred_images,
    y=x_train_clean,
    epochs=10,
    batch_size=32
)

# phase 3, train again from noisy to sharpened output
sharpen_images  = model2.predict(x_train_clean)

model3 = denoising_autoencoder()
model3.compile(optimizer="adam", loss="mse")

model3.fit(
    x=x_train_noisy,
    y=sharpen_images,
    epochs=10,
    batch_size=32
)

# save phase model

model3.save("../models/denoise_sharpen.keras")
