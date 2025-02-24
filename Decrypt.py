import cv2
import os
from tkinter import filedialog

def select_image():
    file_path = filedialog.askopenfilename(title="Select the Encrypted Image", filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
    return file_path

# Open file dialog to select the encrypted image
image_path = select_image()
if not image_path:
    print("No image selected. Exiting...")
    exit()

# Load the encrypted image
img = cv2.imread(image_path)
if img is None:
    print("Error: Unable to load the image.")
    exit()

# Read saved password
password_file = os.path.join(os.path.dirname(image_path), "password.txt")
if not os.path.exists(password_file):
    print("Error: Password file not found!")
    exit()

with open(password_file, "r") as f:
    saved_password = f.read().strip()

# Create dictionary for ASCII decoding
c = {i: chr(i) for i in range(255)}

# Decrypt the message
message = ""
n, m, z = 0, 0, 0

# Take user input for the password
pas = input("Enter passcode for decryption: ")

if saved_password == pas:    
    message += c[img[n, m, z]]
    n = (n + 1) % img.shape[0]
    m = (m + 1) % img.shape[1]
    z = (z + 1) % 3
    print("Decrypted message:", message)
else:
    print("ERROR: Incorrect passcode!")
