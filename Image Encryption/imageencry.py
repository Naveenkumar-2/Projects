from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)

with open('key.txt', 'wb') as f:
    f.write(key)

print("Key has been generated and saved.")

# Load the key from the file
with open('key.key', 'rb') as f:
    key = f.read()

# Create a Fernet object with the key
fernet = Fernet(key)

# Read the image to be encrypted
with open('img.jpg', 'rb') as f:
    photo = f.read()
    print(photo)

# Encrypt the image
locked_photo = fernet.encrypt(photo)

# Write the encrypted image to a new file
with open('locked_img.jpg', 'wb') as locked_photo_file:
    locked_photo_file.write(locked_photo)

print("Image has been encrypted and saved.")
# Load the key from the file
with open('key.key', 'rb') as f:
    key = f.read()

# Create a Fernet object with the key
fernet = Fernet(key)

# Read the encrypted image
with open('locked_img.jpg', 'rb') as f:
    locked_photo = f.read()

# Decrypt the image
unlocked_photo = fernet.decrypt(locked_photo)

# Write the decrypted image to a new file
with open('unlocked_img.jpg', 'wb') as unlocked_photo_file:
    unlocked_photo_file.write(unlocked_photo)

print("Image has been decrypted and saved.")
