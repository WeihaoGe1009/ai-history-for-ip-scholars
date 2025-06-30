# script to download and extract STL-10 from Stanford
# also convert the raw binary to images, training and test sets

import os
import tarfile
import urllib.request
import numpy as np
from PIL import Image

# === Config ===
url = "https://ai.stanford.edu/~acoates/stl10/stl10_binary.tar.gz"
archive_name = "stl10_binary.tar.gz"
extract_folder = "stl10_binary"
output_train_folder = "../data/stl10_train_images_96x96"
output_test_folder = "../data/stl10_test_images_96x96"
resize_to = None  # Set to (64, 64) if you want smaller images

# Class label map (not used unless you want to group)
class_names = [
    "airplane", "bird", "car", "cat", "deer",
    "dog", "horse", "monkey", "ship", "truck"
]

# === Step 1: Download and extract ===
if not os.path.exists(archive_name):
    print("Downloading STL-10...")
    urllib.request.urlretrieve(url, archive_name)

if not os.path.exists(extract_folder):
    print("Extracting dataset...")
    with tarfile.open(archive_name, "r:gz") as tar:
        tar.extractall()

# === Step 2: Parse binary image data ===
def read_images(filepath):
    with open(filepath, "rb") as f:
        images = np.fromfile(f, dtype=np.uint8)
        images = images.reshape(-1, 3, 96, 96)
        images = np.transpose(images, (0, 2, 3, 1))  # Convert to HWC
        return images

def read_labels(filepath):
    with open(filepath, "rb") as f:
        return np.fromfile(f, dtype=np.uint8)

# Load all 5000 images and labels
images_train = read_images(os.path.join(extract_folder, "train_X.bin"))
images_test = read_images(os.path.join(extract_folder, "test_X.bin"))
labels_train = read_labels(os.path.join(extract_folder, "train_y.bin"))  # 1–10 labels
labels_test = read_labels(os.path.join(extract_folder, "test_y.bin"))  # 1–10 labels


# === Step 3: Save images ===
os.makedirs(output_train_folder, exist_ok=True)
os.makedirs(output_test_folder, exist_ok=True)

# avoid zip to prevent misalignment
for i in range(len(labels_train)):
    img_pil = Image.fromarray(images_train[i])
    if resize_to:
        img_pil = img_pil.resize(resize_to)

    filename = f"{i:05d}_class{labels_train[i]}.jpg"
    img_pil.save(os.path.join(output_train_folder, filename))

print(f"Saved {len(images_train)} images to '{output_train_folder}' (resolution: {resize_to or '96x96'})")


for i in range(len(labels_test)):
    img_pil = Image.fromarray(images_test[i])
    if resize_to:
        img_pil = img_pil.resize(resize_to)

    filename = f"{i:05d}_class{labels_test[i]}.jpg"
    img_pil.save(os.path.join(output_train_folder, filename))

print(f"Saved {len(images_test)} images to '{output_test_folder}' (resolution: {resize_to or '96x96'})")

