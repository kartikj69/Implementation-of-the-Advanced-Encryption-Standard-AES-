from Crypto.Cipher import AES
import base64

def aes_encrypt(key, message):
    # Generate a 16-byte key
    aes_key = hashlib.sha256(key.encode()).digest()[:16]
    cipher = AES.new(aes_key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    encrypted_data = base64.b64encode(cipher.nonce + tag + ciphertext)
    return encrypted_data

def aes_decrypt(key, encrypted_message):
    encrypted_message = base64.b64decode(encrypted_message)
    aes_key = hashlib.sha256(key.encode()).digest()[:16]
    nonce, tag, ciphertext = encrypted_message[:16], encrypted_message[16:32], encrypted_message[32:]
    cipher = AES.new(aes_key, AES.MODE_EAX, nonce)
    decrypted_data = cipher.decrypt(ciphertext)
    return decrypted_data

key = input("Enter the encryption key: ")
message = input("Enter the message to encrypt: ")

encrypted_message = aes_encrypt(key, message)
print("Encrypted message: ", encrypted_message)

decrypted_message = aes_decrypt(key, encrypted_message)
print("Decrypted message: ", decrypted_message.decode())
