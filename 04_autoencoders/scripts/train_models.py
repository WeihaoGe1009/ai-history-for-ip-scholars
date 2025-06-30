### the code to train three autoencoder models:
### Flat Convolutional Autoencoder,
### MaxPooling + UpSampling Autoencoder,
### Strided Convolution + Transpose Autoencoder 

### make sure you run process_stl10.py before this one,
### so that the images exist in the "../data/stl10_train_images_96x96" directory 
import tensorflow as tf

# make sure we are using GPU and a compatible TensorFlow version
# otherwise training is slow
print("TensorFlow version:", tf.__version__)
print("Built with CUDA:", tf.test.is_built_with_cuda())
print("GPU devices:", tf.config.list_physical_devices('GPU'))

from tensorflow.keras import layers, models

import os
import numpy as np
from PIL import Image

def load_image_folder(folder_path, target_size=(96, 96)):
    image_list = []
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".jpg"):
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path).convert("RGB").resize(target_size)
            img_array = np.asarray(img, dtype=np.float32) / 255.0  # normalize to [0,1]
            image_list.append(img_array)
    return np.array(image_list)

### define three models

# 1. Flat Convolutional Autoencoder (no spatial downsampling)
def flat_conv_autoencoder(input_shape=(96, 96, 3)):
    inputs = layers.Input(shape=input_shape)

    # Encoder
    x = layers.Conv2D(32, 3, activation='relu', padding='same')(inputs)  # 96×96×32
    x = layers.Conv2D(16, 3, activation='relu', padding='same')(x)       # 96×96×16

    # Decoder
    x = layers.Conv2D(32, 3, activation='relu', padding='same')(x)       # 96×96×32
    outputs = layers.Conv2D(3, 3, activation='sigmoid', padding='same')(x)  # 96×96×3

    return models.Model(inputs, outputs, name="flat_conv")

# 2. MaxPooling + UpSampling Autoencoder
def maxpool_autoencoder(input_shape=(96, 96, 3)):
    inputs = layers.Input(shape=input_shape)

    # Encoder
    x = layers.Conv2D(32, 3, activation='relu', padding='same')(inputs)  # 96×96×32
    x = layers.MaxPooling2D(2, padding='same')(x)                         # 48×48×32
    x = layers.Conv2D(16, 3, activation='relu', padding='same')(x)       # 48×48×16
    x = layers.MaxPooling2D(2, padding='same')(x)                         # 24×24×16

    # Decoder
    x = layers.Conv2D(16, 3, activation='relu', padding='same')(x)       # 24×24×16
    x = layers.UpSampling2D(2)(x)                                         # 48×48×16
    x = layers.Conv2D(32, 3, activation='relu', padding='same')(x)       # 48×48×32
    x = layers.UpSampling2D(2)(x)                                         # 96×96×32
    outputs = layers.Conv2D(3, 3, activation='sigmoid', padding='same')(x)  # 96×96×3

    return models.Model(inputs, outputs, name="maxpool")

# 3. Strided Convolution + Transpose Autoencoder
def strided_autoencoder(input_shape=(96, 96, 3)):
    inputs = layers.Input(shape=input_shape)

    # Encoder
    x = layers.Conv2D(32, 3, strides=2, activation='relu', padding='same')(inputs)  # 48×48×32
    x = layers.Conv2D(16, 3, strides=2, activation='relu', padding='same')(x)       # 24×24×16

    # Decoder
    x = layers.Conv2DTranspose(32, 3, strides=2, activation='relu', padding='same')(x)  # 48×48×32
    outputs = layers.Conv2DTranspose(3, 3, strides=2, activation='sigmoid', padding='same')(x)  # 96×96×3

    return models.Model(inputs, outputs, name="strided")


# 4. Strided Convolution + Dense layer Autoencoder with Skip Connections
def dense_autoencoder(input_shape=(96, 96, 3), bottleneck_dim=64):
    input_img = layers.Input(shape=input_shape)

    # Encoder
    x1 = layers.Conv2D(32, (3, 3), activation="relu", padding="same", strides=2)(input_img)  # 48x48
    x2 = layers.Conv2D(64, (3, 3), activation="relu", padding="same", strides=2)(x1)          # 24x24
    x3 = layers.Conv2D(128, (3, 3), activation="relu", padding="same", strides=2)(x2)         # 12x12

    x_flat = layers.Flatten()(x3)
    encoded = layers.Dense(bottleneck_dim, activation="relu", name="bottleneck")(x_flat)

    # Decoder
    x = layers.Dense(12 * 12 * 128, activation="relu")(encoded)

    x = layers.Reshape((12, 12, 128))(x)

    x = layers.Conv2DTranspose(64, (3, 3), strides=2, padding="same", activation="relu")(x)  # 24x24
    x = layers.Concatenate()([x, x2])  # skip connection
    
    x = layers.Conv2DTranspose(32, (3, 3), strides=2, padding="same", activation="relu")(x)  # 48x48
    x = layers.Concatenate()([x, x1])  # skip connection

    x = layers.Conv2DTranspose(16, (3, 3), strides=2, padding="same", activation="relu")(x)  # 96x96

    decoded = layers.Conv2D(3, (3, 3), activation="sigmoid", padding="same")(x)

    inputs = input_img
    outputs = decoded
    return models.Model(inputs, outputs, name="dense")


def train_and_save(x_data, epochs=20, batch_size=64):
    architectures = {
        "flat_conv": flat_conv_autoencoder,
        "maxpool": maxpool_autoencoder,
        "strided": strided_autoencoder, 
        "dense": strided_autoencoder
    }

    results = {}

    for name, builder in architectures.items():
        print(f"\n Training model: {name}")
        model = builder(input_shape=x_data.shape[1:])
        model.compile(optimizer='adam', loss='mse')
        history = model.fit(x_data, x_data, epochs=epochs, batch_size=batch_size, verbose=0)

        decoded_imgs = model.predict(x_data[:5])  # show first 5 reconstructions
        results[name] = (model, decoded_imgs)
        fl_name = "model_"+name+"_autoencoder.keras"
        model.save(fl_name)

    return results


### load all images
images_train = load_image_folder('../data/') 
images = images.astype('float32') / 255.0

### train the models 
results = train_and_save(images, epochs=20)
