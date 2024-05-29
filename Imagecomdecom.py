# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from PIL import Image
import os
def compress_image(input_path, output_path, quality=85):
    try:
        # Open the input image
        img = Image.open(input_path)

        # Compress the image and save it with the same file type
        img.save(output_path, "JPEG", quality=quality)

        print(f"Image compressed successfully to {output_path}!")
    except Exception as e:
        print("Error:", e)
def decompress_image(input_path, output_path):
    try:
        # Open the compressed image
        img = Image.open(input_path)

        # Save the image with the same format as the input
        img.save(output_path)

        print(f"Image decompressed successfully to {output_path}!")
    except Exception as e:
        print("Error:", e)
if __name__ == "__main__":
    input_image = r"C:\Users\gdile\OneDrive\Pictures\pics.jpg"
    compressed_image = "compressed_image.png"
    decompressed_image = "decompressed_image.png"

    # Compress the image
    compress_image(input_image, compressed_image)

    # Decompress the compressed image
    decompress_image(compressed_image, decompressed_image)
from PIL import Image
import matplotlib.pyplot as plt
def compress_image(input_path, output_path, quality=85):
    try:
        # Open the input image
        img = Image.open(input_path)

        # Compress the image and save it with the same file type
        img.save(output_path, "JPEG", quality=quality)

        print(f"Image compressed successfully to {output_path}!")
    except Exception as e:
        print("Error:", e)
def decompress_image(input_path, output_path):
    try:
        # Open the compressed image
        img = Image.open(input_path)

        # Save the image with the same format as the input
        img.save(output_path)

        print(f"Image decompressed successfully to {output_path}!")
    except Exception as e:
        print("Error:", e)
if __name__ == "__main__":
    input_image = r"C:\Users\gdile\OneDrive\Pictures\pics.jpg"
    compressed_image = "compressed_image.png"
    decompressed_image = "decompressed_image.png"

    # Compress the image
    compress_image(input_image, compressed_image)

    # Decompress the compressed image
    decompress_image(compressed_image, decompressed_image)

    # Display the images
    #fig, axes = plt.subplots(1, 3, figsize=(10, 4))

    input_img = Image.open(input_image)
    compressed_img = Image.open(compressed_image)
    decompressed_img = Image.open(decompressed_image)

    # Original Image
    plt.figure(figsize=(5, 5))
    plt.imshow(input_img)
    plt.title("Original Image")
    plt.axis('off')
    plt.show()

    # Compressed Image
    plt.figure(figsize=(4, 4))
    plt.imshow(compressed_img)
    plt.title("Compressed Image")
    plt.axis('off')
    plt.show()

    # Decompressed Image
    plt.figure(figsize=(5, 5))
    plt.imshow(decompressed_img)
    plt.title("Decompressed Image")
    plt.axis('off')
    plt.show()