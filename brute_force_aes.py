import binascii
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def brute_force_aes(ciphertext, iv, key_space):
    for key_int in range(key_space):
        key = key_int.to_bytes(2, byteorder='big') + b'\x00' * 14
        cipher = AES.new(key, AES.MODE_CBC, iv)
        try:
            decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
        except (ValueError, KeyError):
            continue
        entropy = shannon_entropy(decrypted)
        if entropy < 5:  # Adjust threshold if necessary
            print(f"Potential key found: {binascii.hexlify(key)}")
            return decrypted
    return None

def shannon_entropy(data):
    import math
    from collections import Counter
    counter = Counter(data)
    total_len = len(data)
    entropy = -sum(count/total_len * math.log2(count/total_len) for count in counter.values())
    return entropy

if __name__ == "__main__":
    # Read the file in binary mode
    with open('enc_2.hex', 'rb') as f:
        data = f.read().strip()

    # Extract the IV and the ciphertext
    iv = data[:16]
    ciphertext = data[16:]
    
    # Define the key space (16-bit keys, hence 2^16 possibilities)
    key_space = 2**16
    
    # Run brute-force attack
    decrypted_data = brute_force_aes(ciphertext, iv, key_space)
    
    if decrypted_data:
        print("Decryption successful. Saving to enc_1.hex...")
        with open('enc_1.hex', 'wb') as f:
            f.write(binascii.hexlify(decrypted_data))
    else:
        print("Failed to find the correct key.")
      
