from PIL import Image

def encrypt_image(source_path, encrypted_path, key):
    image = Image.open(source_path)
    pixel_map = image.load()

    img_width, img_height = image.size

    for x in range(img_width):
        for y in range(img_height):
            red, green, blue = pixel_map[x, y]

            # Encrypt by swapping the red and blue channels
            encrypted_pixel = (blue, green, red)

            pixel_map[x, y] = encrypted_pixel

    image.save(encrypted_path)
    print("Encryption complete!")

def decrypt_image(encrypted_path, decrypted_path, key):
    image = Image.open(encrypted_path)
    pixel_map = image.load()

    img_width, img_height = image.size

    for x in range(img_width):
        for y in range(img_height):
            blue, green, red = pixel_map[x, y]

            # Decrypt by swapping the red and blue channels back
            decrypted_pixel = (red, green, blue)

            pixel_map[x, y] = decrypted_pixel

    image.save(decrypted_path)
    print("Decryption complete!")

# File paths
input_image_path = r"C:\Users\IBRAHIM\OneDrive\Desktop\Cyber Security\Task-2\image woo.jpg"
encrypted_image_path = r"C:\Users\IBRAHIM\OneDrive\Desktop\Cyber Security\Task-2\encrypt.jpg"
decrypted_image_path = r"C:\Users\IBRAHIM\OneDrive\Desktop\Cyber Security\Task-2\decrypt.jpg"

# Execute encryption and decryption
encrypt_image(input_image_path, encrypted_image_path, key=None)
decrypt_image(encrypted_image_path, decrypted_image_path, key=None)
