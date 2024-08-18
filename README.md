# Brute-force AES Decryption

## Overview
This project provides a Python script (`brute_force_aes.py`) to perform a brute-force attack on an AES-encrypted file. The script is designed to decrypt a file encrypted with AES in CBC mode using a weak key, where only the first 16 bits of the 128-bit key are used, and the rest are padded with zeros. The script attempts all possible keys within this reduced key space.

## Features
- **Brute-force Decryption**: Automatically tries all possible keys within the 16-bit key space to decrypt the provided ciphertext.
- **Shannon Entropy Check**: Uses Shannon entropy to identify the correct decryption by analyzing the decrypted data's entropy. Lower entropy typically indicates a successful decryption of text data.

## Files
- `brute_force_aes.py`: The main script that performs the brute-force attack on the AES-encrypted file.

## Usage

### Prerequisites
- Python 3.x
- PyCryptodome library: Install it using pip if you haven't already:
  ```bash
  pip install pycryptodome

Run the script using Python:
python brute_force_aes.py
