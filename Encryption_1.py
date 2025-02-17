import cv2
import numpy as np
import os


def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)


def encode_message(image_path, secret_message, output_path):
    if not os.path.exists(image_path):
        print("❌ Error: File not found. Please check the file path.")
        return

    image = cv2.imread(image_path)
    if image is None:
        print("❌ Error: Could not read the image file. Make sure it's a valid image.")
        return

    binary_message = text_to_binary(secret_message) + '1111111111111110'  

    data_index = 0
    rows, cols, channels = image.shape

    for row in range(rows):
        for col in range(cols):
            pixel = image[row, col]
            for channel in range(3):  
                if data_index < len(binary_message):
                    pixel[channel] = pixel[channel] & ~1 | int(binary_message[data_index])
                    data_index += 1

    cv2.imwrite(output_path, image)
    print(f"✅ Message successfully encoded into {output_path}")


image_path = input("🔹 Enter the path of the image: ").strip()
secret_message = input("🔹 Enter the secret message to hide: ").strip()
output_path = input("🔹 Enter the output image file path: ").strip()


encode_message(image_path, secret_message, output_path)
