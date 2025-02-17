import cv2
import numpy as np
import os


def binary_to_text(binary_data):
    chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    return ''.join(chr(int(char, 2)) for char in chars if char != '11111111')


def decode_message(image_path):
    if not os.path.exists(image_path):
        print("❌ Error: File not found. Please check the file path.")
        return

    image = cv2.imread(image_path)
    if image is None:
        print("❌ Error: Could not read the image file. Make sure it's a valid image.")
        return

    binary_message = ""
    rows, cols, channels = image.shape

    for row in range(rows):
        for col in range(cols):
            pixel = image[row, col]
            for channel in range(3):  
                binary_message += str(pixel[channel] & 1)
                if binary_message[-16:] == '1111111111111110':  
                    print("\n🔓 Decoded message:", binary_to_text(binary_message[:-16]))
                    return

    print("❌ No hidden message found.")


image_path = input("🔹 Enter the path of the encoded image: ").strip()


decode_message(image_path)
