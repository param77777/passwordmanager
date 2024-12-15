# Password Manager

A simple Password Manager GUI application built using Python's Tkinter library. This app helps users securely store and generate passwords for various websites or services. It allows you to:

- Generate a secure random password.
- Save website credentials (email, password) into a text file.
- Copy the generated password to the clipboard for easy pasting.

## Features

- **Password Generator**: Automatically generates a random password containing letters, symbols, and numbers.
- **Save Password**: Saves the credentials (website, email, and password) to a local text file (`data.txt`).
- **Clipboard Support**: Copies of the generated password are sent to the clipboard for easy use.
- **Error Handling**: Displays an error if missing or incomplete fields.

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- Pyperclip (`pip install pyperclip`)

## How to Use

1. **Generate a Password**:
   - Click on the "Generate Password" button to generate a random password.
   - The generated password will be copied to your clipboard and inserted into the password field.

2. **Save the Credentials**:
   - Enter the website name, your email/username, and the generated password.
   - Click the "Add" button to save the credentials.
   - The credentials will be saved to a file named `data.txt` in your project directory.

3. **Data File**:
   - The credentials will be saved in the format `website|email|password` in `data.txt`.
   - Each entry is appended on a new line.

