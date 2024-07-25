# Steganography-using-Python

### Project Description: Image Encryption and Decryption using Tkinter and OpenCV
#### Overview
This project is a graphical application for encrypting and decrypting messages within image files using the Tkinter library for the GUI and OpenCV for image processing. The primary goal is to securely hide a secret message inside an image, which can later be retrieved using the correct password.

#### Features
1. **Encrypt Message in Image**:
   - Users can input a secret message and select an image file.
   - The message is encoded into the image's pixel values.
   - The user sets a password to secure the encryption process.
   - The encrypted image can be saved to a specified location.

2. **Decrypt Message from Image**:
   - Users can select an encrypted image file.
   - The correct passcode must be entered to decrypt and retrieve the hidden message.
   - The decrypted message is displayed if the correct passcode is provided.

#### How It Works
- **Encryption**:
  - The user inputs a secret message and selects an image file.
  - The application checks if the message length can fit within the image's pixel data.
  - The message characters are converted to their ASCII values and embedded into the image's pixel values.
  - The modified image is saved as a new file.

- **Decryption**:
  - The user selects an encrypted image file and provides a passcode.
  - The application verifies the passcode and retrieves the embedded message from the image's pixel values.
  - The decrypted message is displayed to the user.

#### Technical Details
- **Libraries Used**:
  - `cv2` (OpenCV): For reading and writing image files and manipulating pixel data.
  - `tkinter`: For creating the graphical user interface, including file dialogs and input fields.
  - `os`: For opening the saved encrypted image file.

- **GUI Components**:
  - Entry fields for the secret message, password, and passcode.
  - Buttons for selecting images, encrypting messages, decrypting messages, and saving the encrypted image.
  - Labels for displaying status messages and decrypted text.

- **Image Processing**:
  - The message is embedded in the image by modifying the least significant bits of the pixel values.
  - The message is extracted by reading these bits and converting them back to characters.

#### Usage
1. **Encrypting a Message**:
   - Enter the secret message and a password.
   - Select an image file.
   - The application checks the image's capacity and embeds the message.
   - Save the encrypted image to a desired location.

2. **Decrypting a Message**:
   - Enter the same message length and passcode used during encryption.
   - Select the encrypted image file.
   - If the passcode is correct, the hidden message is displayed.

#### Security Considerations
- The application masks the password and passcode inputs to prevent unauthorized viewing.
- The encrypted message is stored in a non-obvious manner within the image, making it difficult to detect without the proper decryption process.

#### Potential Enhancements
- **Stronger Encryption**: Implementing more advanced encryption algorithms for added security.
- **Image Format Support**: Expanding support for more image formats.
- **Error Handling**: Enhancing error handling for various edge cases and user errors.
- **User Interface**: Improving the GUI for a better user experience.

This project demonstrates a practical application of image processing and basic encryption techniques, providing a secure way to hide and retrieve messages within image files.
