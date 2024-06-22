
from PIL import Image
import os
import matplotlib.pyplot as plt

def compress_image(input_path, output_path, target_size):
    quality = 85
    while True:
        try:
            # Open the input image
            img = Image.open(input_path)

            # Compress the image with the current quality setting
            img.save(output_path, "JPEG", quality=quality)

            # Check the size of the compressed image
            compressed_size = os.path.getsize(output_path)

            if compressed_size < target_size:
                print(f"Image compressed successfully to {output_path}!")
                break
            else:
                quality -= 5  # Decrease quality for further compression
                if quality < 5:
                    print("Compression failed: Image cannot be compressed to a smaller size.")
                    break
        except Exception as e:
            print("Error:", e)

def decompress_image(input_path, output_path):
    try:
        # Open the compressed image
        img = Image.open(input_path)

        # Save the image with the same format as the input
        img.save(output_path, "JPEG")

        print(f"Image decompressed successfully to {output_path}!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    input_image = r"C:\Users\gdile\OneDrive\Pictures\pics.jpg"
    compressed_image = r"C:\Users\gdile\OneDrive\Pictures\compressed_image.jpg"  # Use .jpg extension
    decompressed_image = r"C:\Users\gdile\OneDrive\Pictures\decompressed_image.jpg"  # Use .jpg extension

    # Check if input image exists
    if not os.path.exists(input_image):
        print(f"Error: File {input_image} not found.")
    else:
        # Get the size of the original image
        original_size = os.path.getsize(input_image)

        # Set a target size for the compressed image (90% of original size)
        target_size = int(original_size * 0.5)

        # Compress the image
        compress_image(input_image, compressed_image, target_size)

        # Check if compressed image was created successfully
        if os.path.exists(compressed_image):
            # Decompress the compressed image
            decompress_image(compressed_image, decompressed_image)

            # Get the size of the decompressed image
            decompressed_size = os.path.getsize(decompressed_image)

            # Display the sizes of the original, compressed, and decompressed images
            print(f"Original image size: {original_size / 1024:.2f} KB")
            print(f"Compressed image size: {os.path.getsize(compressed_image) / 1024:.2f} KB")
            print(f"Decompressed image size: {decompressed_size / 1024:.2f} KB")

            # Display the images
            fig, axes = plt.subplots(1, 3, figsize=(15, 5))

            # Original Image
            original_img = Image.open(input_image)
            axes[0].imshow(original_img)
            axes[0].set_title("Original Image\nSize: {:.2f} KB".format(original_size / 1024))
            axes[0].axis('off')

            # Compressed Image
            compressed_img = Image.open(compressed_image)
            axes[1].imshow(compressed_img)
            axes[1].set_title("Compressed Image\nSize: {:.2f} KB".format(os.path.getsize(compressed_image) / 1024))
            axes[1].axis('on')

            # Decompressed Image
            decompressed_img = Image.open(decompressed_image)
            axes[2].imshow(decompressed_img)
            axes[2].set_title("Decompressed Image\nSize: {:.2f} KB".format(decompressed_size / 1024))
            axes[2].axis('off')

            plt.show()
        else:
            print(f"Error: Compressed image {compressed_image} not created.")
