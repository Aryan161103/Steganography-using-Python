import cv2
import os
import tkinter as tk
from tkinter import filedialog

# Initialize dictionaries
d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

def encrypt_image():
    msg = entry_msg.get()
    img_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])
    if not img_path:
        label_status.config(text="No image file selected.")
        return

    img = cv2.imread(img_path)
    if img is None:
        label_status.config(text="Image file not found or not an image.")
        return

    password = entry_password.get()
    if not password:
        label_status.config(text="Password is required.")
        return

    height, width, _ = img.shape

    # Ensure the message can fit in the image
    if len(msg) > height * width * 3:
        label_status.config(text="Message is too long for the image.")
        return

    n, m, z = 0, 0, 0
    for char in msg:
        img[n, m, z] = d[char]
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m == width:
                m = 0
                n += 1
                if n == height:
                    break

    output_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")])
    if output_path:
        cv2.imwrite(output_path, img)
        os.system(f"start {output_path}")
        label_status.config(text=f"Message encrypted and saved as {output_path}")
    else:
        label_status.config(text="Save operation cancelled.")

def decrypt_image():
    img_path = filedialog.askopenfilename(title="Select Encrypted Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])
    if not img_path:
        label_status.config(text="No image file selected.")
        return

    img = cv2.imread(img_path)
    if img is None:
        label_status.config(text="Image file not found or not an image.")
        return

    passcode = entry_passcode.get()
    password = entry_password.get()  # Use this for validation if needed

    if passcode != password:
        label_status.config(text="Incorrect passcode.")
        return

    height, width, _ = img.shape
    decrypted_msg = ""
    n, m, z = 0, 0, 0

    # Determine the length of the message to extract
    length_of_message = len(entry_msg.get())
    
    for _ in range(length_of_message):
        decrypted_msg += c[img[n, m, z]]
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m == width:
                m = 0
                n += 1
                if n == height:
                    break

    label_decryption.config(text="Decrypted message: " + decrypted_msg)

# Set up the GUI
window = tk.Tk()
window.title("Image Encryption/Decryption")

# Create and pack widgets
label_msg = tk.Label(window, text="Enter secret message:")
label_msg.pack()

entry_msg = tk.Entry(window)
entry_msg.pack()

label_password = tk.Label(window, text="Enter password:")
label_password.pack()

entry_password = tk.Entry(window, show="*")  # Masking the password input
entry_password.pack()

button_encrypt = tk.Button(window, text="Encrypt Image", command=encrypt_image)
button_encrypt.pack()

label_passcode = tk.Label(window, text="Enter passcode for Decryption:")
label_passcode.pack()

entry_passcode = tk.Entry(window, show="*")  # Masking the passcode input
entry_passcode.pack()

button_decrypt = tk.Button(window, text="Decrypt Image", command=decrypt_image)
button_decrypt.pack()

label_decryption = tk.Label(window, text="")
label_decryption.pack()

label_status = tk.Label(window, text="")
label_status.pack()

# Start the main loop
window.mainloop()
