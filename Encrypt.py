import cv2
import os
import tkinter as tk
from tkinter import filedialog

def select_image():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
    return file_path

# Open file dialog to select an image
image_path = select_image()
if not image_path:
    print("No image selected. Exiting...")
    exit()

# Load the image
img = cv2.imread(image_path)
if img is None:
    print("Error: Unable to load the image.")
    exit()

# Take user input for the secret message and password
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Create dictionary for ASCII encoding
d = {chr(i): i for i in range(255)}

# Encrypt message into image
n, m, z = 0, 0, 0
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = (n + 1) % img.shape[0]
    m = (m + 1) % img.shape[1]
    z = (z + 1) % 3

# Save encrypted image
encrypted_image_path = os.path.join(os.path.dirname(image_path), "encryptedImage.jpg")
cv2.imwrite(encrypted_image_path, img)
print(f"Encrypted image saved as: {encrypted_image_path}")

# Save password for decryption
with open(os.path.join(os.path.dirname(image_path), "password.txt"), "w") as f:
    f.write(password)
