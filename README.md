# Ciphertext-Only-Analysis
# Ciphertext-Only Analysis: Brute-force AES Decryption

## Overview
This project demonstrates a ciphertext-only attack on a file that has been encrypted using a weak AES key. The file, `enc_2.hex`, has been encrypted twice:
1. **First Layer**: Monoalphabetic substitution cipher.
2. **Second Layer**: AES encryption in CBC mode using a weak 128-bit key.

The goal of this project is to:
1. **Brute-force the AES encryption** using the known weakness in the key (only the first 16 bits are used, and the rest of the key is padded with zeros).
2. **Identify the correct key** based on Shannon entropy, a measure of randomness, to differentiate between the correct and incorrect decryption attempts.
3. **Save the decrypted output** as `enc_1.hex`, which will be used for further cryptanalysis in subsequent steps.

## Task Breakdown
### Task 1: Brute-force Weak AES
Given the small key space (16 bits), a brute-force attack is feasible. The script attempts all possible 16-bit keys (which are padded to 128 bits) to decrypt the AES layer. The correct key is identified using Shannon entropy to determine which decryption results in a plausible plaintext.

### How Shannon Entropy Helps
Shannon entropy is a measure of the unpredictability or randomness in data. When correctly decrypted, text-based data typically has lower entropy compared to random data. By calculating the entropy of each decryption attempt, the script can filter out the most likely correct key.

## Script Overview
### `brute_force_aes.py`
This Python script performs the brute-force attack on the AES encryption. It does the following:
1. **Reads the encrypted file**: The file `enc_2.hex` is read in binary mode since it contains non-text data.
2. **Extracts the IV and ciphertext**: The initialization vector (IV) is extracted from the first 16 bytes, and the remainder of the file is treated as the ciphertext.
3. **Brute-force decryption**: The script iterates over all possible 16-bit keys (65,536 possibilities), decrypting the ciphertext for each key.
4. **Entropy-based key identification**: For each decryption attempt, Shannon entropy is calculated to determine the randomness of the resulting plaintext. The script identifies and prints the key with the lowest entropy, which is likely the correct key.
5. **Outputs the decrypted data**: Once the correct key is identified, the decrypted data is saved to `enc_1.hex` for further analysis.

### Prerequisites
To run this script, you need:
- **Python 3.x**
- **PyCryptodome**: A Python library for cryptographic operations. Install it using:
  ```bash
  pip install pycryptodome
