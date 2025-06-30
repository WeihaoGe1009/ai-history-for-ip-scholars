import os
import numpy as np
from PIL import Image

def add_noise_to_image(image, std=0.15):
    img_array = np.array(image).astype(np.float32) / 255.0
    noise = np.random.normal(loc=0.0, scale=std, size=img_array.shape)
    noisy = np.clip(img_array + noise, 0.0, 1.0)
    noisy_img = Image.fromarray((noisy * 255).astype(np.uint8))
    return noisy_img

def process_folder_jpg(input_folder, output_folder, std=0.15):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".jpg"):
            img_path = os.path.join(input_folder, filename)
            image = Image.open(img_path).convert("RGB")
            noisy_image = add_noise_to_image(image, std)
            noisy_image.save(os.path.join(output_folder, filename))
            #print(f"Noisy image saved: {filename}")

# Process training and testing folders
process_folder_jpg("../data/stl10_train_images_96x96", "../data/stl10_train_noisy_images_96x96", std=0.15)
process_folder_jpg("../data/stl10_test_images_96x96", "../data/stl10_test_noisy_images_96x96", std=0.15)
